from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.chat_models.openai import ChatOpenAI
from langchain.tools.render import render_text_description

load_dotenv()
from llama_wrapper import LLAMAAPI
llm=ChatOpenAI(openai_api_base="http://localhost:8000/v1", max_tokens=245)

prompt = hub.pull("hwchase17/react")


tools = load_tools(["serpapi", "llm-math"], llm=llm)
prompt = prompt.partial(
    tools=render_text_description(tools),
    tool_names=", ".join([t.name for t in tools]),
)
llm_with_stop = llm.bind(stop=["\nObservation"])


agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),
    }
    | prompt
    | llm_with_stop
    | ReActSingleInputOutputParser()
)
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print(
    agent_executor.invoke(
        {
            "input": "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
        }
    )
)
