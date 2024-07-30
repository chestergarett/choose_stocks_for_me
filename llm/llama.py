from transformers import pipeline
import torch
import os
from dotenv import load_dotenv

load_dotenv()

model_id = os.environ.get('LLAMA_FILEPATH')
pipe = pipeline(
    'text-generation',
    model=model_id,
    model_kwargs={'torch_dtype': torch.bfloat16},   
)

messages = [{'role': 'user', 'content': 'How to cure cancer'}]
outputs = pipe(
    messages,
    max_new_tokens=256,
    do_sample=False,
)

assistant_response = outputs[0]['generated_text'][-1]['content']
print(assistant_response)