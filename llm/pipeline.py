import torch
import os
from langchain.chains import LLMChain
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM


hf_token = os.environ.get('HUGGING_FACE_TOKEN')
model_id='google/flan-t5-small'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id, load_in_8bit=True, device_map='auto')

pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=128
)

template = """ Question: {question}
    Answer: Let's think step by step.
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
local_llm = HuggingFacePipeline(pipeline=pipeline)
llm_chain = LLMChain(prompt=prompt,
                     llm = local_llm
        )

question = "What is the capital of England?"
print(llm_chain.run(question))