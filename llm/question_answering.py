import os
# from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub

hf_token = os.environ.get('HUGGING_FACE_TOKEN')

template = """ Question: {question}
    Answer: Let's think step by step.
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt,
                        llm=HuggingFaceHub(repo_id='google/flan-t5-xl',
                            model_kwargs={
                                "temperature":0, "max_length": 64
                            }               
                    )             
)

question = "What is the capital of England?"
print(llm_chain.run(question))