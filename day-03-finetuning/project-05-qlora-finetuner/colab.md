# Running Project 5 on Google Colab (free GPU)

1. Open https://colab.research.google.com → New notebook.
2. Runtime → Change runtime type → **T4 GPU**.
3. In a cell:
```python
!pip install -q transformers peft bitsandbytes accelerate datasets trl
!git clone https://github.com/ransjnr/tech-giants-sprint.git
%cd tech-giants-sprint/day-03-finetuning/project-05-qlora-finetuner
!python train_qlora.py --config config.yaml
!python inference.py --adapters ./adapters --prompt "What is RAG?"
```
