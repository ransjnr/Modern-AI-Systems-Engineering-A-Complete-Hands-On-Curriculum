"""QLoRA fine-tuning. Run on a CUDA GPU. Requires: see requirements.txt"""
import argparse, yaml, json
import torch
from datasets import Dataset
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          BitsAndBytesConfig, TrainingArguments)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

def load_rows(path):
    rows = [json.loads(l) for l in open(path)]
    return Dataset.from_list([
        {"text": f"### Instruction:\n{r['instruction']}\n\n### Response:\n{r['response']}"}
        for r in rows])

def main(cfg_path):
    cfg = yaml.safe_load(open(cfg_path))
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                             bnb_4bit_compute_dtype=torch.bfloat16)
    tok = AutoTokenizer.from_pretrained(cfg["base_model"])
    tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        cfg["base_model"], quantization_config=bnb, device_map="auto")
    model = prepare_model_for_kbit_training(model)
    lora = LoraConfig(r=cfg["lora"]["r"], lora_alpha=cfg["lora"]["alpha"],
                      lora_dropout=cfg["lora"]["dropout"],
                      target_modules=cfg["lora"]["target_modules"],
                      task_type="CAUSAL_LM")
    model = get_peft_model(model, lora)
    model.print_trainable_parameters()  # shows the tiny % being trained

    args = TrainingArguments(
        output_dir=cfg["output_dir"], num_train_epochs=cfg["train"]["epochs"],
        per_device_train_batch_size=cfg["train"]["batch_size"],
        learning_rate=cfg["train"]["learning_rate"], logging_steps=1, save_strategy="epoch")
    trainer = SFTTrainer(model=model, args=args, train_dataset=load_rows(cfg["dataset_path"]),
                         dataset_text_field="text", max_seq_length=cfg["train"]["max_seq_len"],
                         tokenizer=tok)
    trainer.train()
    model.save_pretrained(cfg["output_dir"])
    print("Saved LoRA adapters ->", cfg["output_dir"])

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--config", default="config.yaml")
    main(ap.parse_args().config)
