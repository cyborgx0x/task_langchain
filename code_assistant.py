from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema.output_parser import StrOutputParser
from langchain.utilities import PythonREPL

template = """Write some python code to solve the user's problem. 

Return only python code in Markdown format, e.g.:

```python
....
```"""
prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])
from local_model import llm

# model = ChatOpenAI()
model = llm


def _sanitize_output(text: str):
    return text.split("```")[1]


chain = prompt | model | StrOutputParser() | _sanitize_output | PythonREPL().run


chain.invoke({"input": "print Hello World"})
