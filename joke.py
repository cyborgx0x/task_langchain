from langchain.prompts import ChatPromptTemplate
from llm_gpt import CustomLLM
from local_model import llm
model = CustomLLM(n=1)
model = llm
prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
chain = prompt | model
# chain = prompt | model.bind(stop=["\n"])
print(chain.invoke({"foo": "bears"}))

