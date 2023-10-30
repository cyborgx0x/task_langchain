from operator import itemgetter

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.vectorstores import FAISS
from llm_gpt import CustomLLM
import requests
# vectorstore = FAISS.from_texts(
#     ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
# )
# retriever = vectorstore.as_retriever()
def retriever(*x, **y):
    requests.get('')
    return 'harrison worked at kensho'

template = """Answer the question based only on the following context:
harrison worked at kensho

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = CustomLLM(n=1)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke("where did harrison work?")

)