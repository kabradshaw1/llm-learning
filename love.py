import torch
import transformers
import numpy as np
import re
from datasets import load_dataset

model_id = "meta-llama/Meta-Llama-3-8B"
pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")

pipeline("Hey how are you doing today?")