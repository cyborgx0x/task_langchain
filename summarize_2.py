from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import GPT4All
from langchain.prompts import PromptTemplate

from search_task import CustomChatOPENAI
from text import text2

llm = CustomChatOPENAI(
    openai_api_base="http://localhost:8000/v1", max_tokens=4048, temperature=0
)

template = """What is top 10 important keywords from following text?: 
```
{article}
```
Answer: Let's think step by step.
"""

prompt = PromptTemplate(template=template, input_variables=["article"])


callbacks = [StreamingStdOutCallbackHandler()]

# from local_model import llm

llm_chain = LLMChain(prompt=prompt, llm=llm)


article = text2

llm_chain.run(article)
