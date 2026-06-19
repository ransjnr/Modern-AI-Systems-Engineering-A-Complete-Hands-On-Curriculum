# Project 5 — QLoRA Fine-Tuner (BioHealth assistant tone)

Fine-tune a small base model with **QLoRA** (4-bit quantisation + LoRA adapters) so it
adopts a desired style/domain — cheaply, on a single GPU.

> ⚠️ Requires a CUDA GPU. Use Google Colab (free T4) if you don't have one — see `colab.md`.

## Install (GPU machine / Colab)
```bash
pip install -r requirements.txt
```

## Train
```bash
python train_qlora.py --config config.yaml
# writes LoRA adapters to ./adapters/
```

## Inference
```bash
python inference.py --adapters ./adapters --prompt "Explain what a vector database is."
```

## How QLoRA works (in one breath)
The base model's weights are frozen and loaded in 4-bit. Tiny trainable low-rank
matrices (LoRA adapters) are inserted into attention layers. You train only those —
a fraction of a percent of the parameters — so it fits on one small GPU.
