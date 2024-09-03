import study
import transformers
import langchain as lg

huggingface = lg.huggingface

model_id = "meta-llama/Meta-Llama-3-8B"
pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": study.bfloat16}, device_map="auto")

pipeline("Hey how are you doing today?")

