from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI(openai_api_base="http://localhost:8000/v1", max_tokens=4048, temperature=0)

template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
print(llm_chain.run(question))
