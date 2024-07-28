import torch
import os
from langchain.chains import LLMChain
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM

model_id = "gpt2-medium"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=100
)

template = """ Question: {question}
    Answer: Let's think step by step.
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
local_llm = HuggingFacePipeline(pipeline=pipeline)
llm_chain = LLMChain(prompt=prompt, llm=local_llm)
question = "What is the capital of England?"
print(llm_chain.run(question))