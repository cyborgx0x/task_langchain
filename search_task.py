from typing import Any, Coroutine, Dict, Iterator, List, Optional

import markdown2
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.callbacks.manager import CallbackManagerForLLMRun, Callbacks
from langchain.chains import LLMMathChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import LLMResult
from langchain.schema.messages import BaseMessage
from langchain.schema.output import ChatGenerationChunk
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.utilities import SerpAPIWrapper
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from google_search import Google_Dorking
from llama_wrapper import LLAMAAPI
from llm_gpt import CustomLLM
from retriever import retriever

load_dotenv()


class CustomChatOPENAI(ChatOpenAI):
    def generate(
        self,
        messages: List[List[BaseMessage]],
        stop: List[str] | None = None,
        callbacks: Callbacks = None,
        *,
        tags: List[str] | None = None,
        metadata: Dict[str, Any] | None = None,
        run_name: str | None = None,
        **kwargs: Any,
    ) -> LLMResult:
        return super().generate(
            messages,
            stop,
            callbacks,
            tags=tags,
            metadata=metadata,
            run_name=run_name,
            **kwargs,
        )


# from local_model import llm

# llm = LLAMAAPI(n=1)
search = SerpAPIWrapper(
    serpapi_api_key="03feffb940b52a345fcc39ec463e24d2c11af3fcf2fc87d560df4c6162ed7994"
)


from langchain.tools import tool


class URLRetriever(BaseTool):
    def _run(self, url: str) -> str:
        print(url)
        try:
            html = markdown2.markdown(url)
            raw_url = html.split('"')[1]
        except:
            raw_url = None
        if raw_url:
            return retriever(url=raw_url)

        return retriever(url=url)


class GoogleSearch(BaseTool):
    def _run(self, keyword: str) -> str:
        return Google_Dorking(keyword=keyword)


retriever_tool = URLRetriever(
    name="Summarize From URL",
    func=URLRetriever,
    description="useful for when you need to summarize content from a real URL, input is a URL from Google Search Tool, only url",
)

google_search_tool = GoogleSearch(
    name="Google Search",
    func=GoogleSearch,
    description="useful for when you need to search for a list of url to summarize",
)

tools = [
    google_search_tool,
    retriever_tool,
]

# llm = ChatOpenAI(openai_api_base="http://localhost:8000/v1", max_tokens=4048)
llm = CustomLLM(n=1)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)
from summarize_agent import create_pirate_agent

agent = create_pirate_agent(
    tools=tools,
    llm=llm,
)


template_helper = """Trong vai trò là một người điều tra tội phạm, bạn hãy tìm hiểu thông tin thông qua câu hỏi sau. Sâu đây là các công cụ bạn được quyền sử dụng:
Bạn không được kết luận quá sớm, bạn cần có ít nhất 5 observation để có thể đưa ra câu trả lời cuối cùng bằng tiếng Việt
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times, and must be repeat more than five times to have full comprehensive and detail answer to the problem)
Thought: I now know the final answer
Final Answer: Câu trả lời Tổng hợp từ các observation bằng một danh sách

Hãy nhớ rằng, câu trả lời cuối cùng nên tổng hợp đầy đủ thông tin từ toàn bộ các hành động và suy nghĩ trước. Cung cấp một báo cáo đầy đủ và chi tiết

Question: {input}
{agent_scratchpad}"""


helper_agent = create_pirate_agent(
    tools=tools,
    llm=llm,
    template=template_helper
)

agent.run(
    f"LISA Black Pink"
)


# agent_executor = initialize_agent(
#     [tool],
#     llm,
#     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
#     handle_parsing_errors=True,
# )

# agent_executor.run("What is 438745398475893479 time 29087423453984")
