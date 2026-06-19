"""Load base model + LoRA adapters and generate. Requires a GPU."""
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

def main(base, adapters, prompt):
    tok = AutoTokenizer.from_pretrained(base)
    model = AutoModelForCausalLM.from_pretrained(base, device_map="auto",
                                                 torch_dtype=torch.bfloat16)
    model = PeftModel.from_pretrained(model, adapters)
    text = f"### Instruction:\n{prompt}\n\n### Response:\n"
    ids = tok(text, return_tensors="pt").to(model.device)
    out = model.generate(**ids, max_new_tokens=200, do_sample=False)
    print(tok.decode(out[0], skip_special_tokens=True))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    ap.add_argument("--adapters", default="adapters")
    ap.add_argument("--prompt", required=True)
    a = ap.parse_args(); main(a.base, a.adapters, a.prompt)
