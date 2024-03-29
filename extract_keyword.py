from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain

# Schema
schema = {
    "properties": {
        "name": {"type": "string"},
        "height": {"type": "integer"},
        "hair_color": {"type": "string"},
    },
    "required": ["name", "height"],
}

# Input
inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde."""

# Run chain
# llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
from local_model import llm
chain = create_extraction_chain(schema, llm)
chain.run(inp)

