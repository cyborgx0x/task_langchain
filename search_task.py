from typing import Any, Coroutine, Dict, Iterator, List, Optional

import markdown2
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


llm = CustomChatOPENAI(
    temperature=0, openai_api_key="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"
)
llm = CustomLLM(n=1)
# llm = LLAMAAPI(n=1)
# Load the tool configs that are needed.
search = SerpAPIWrapper(
    serpapi_api_key="03feffb940b52a345fcc39ec463e24d2c11af3fcf2fc87d560df4c6162ed7994"
)
llm_math_chain = LLMMathChain(llm=llm, verbose=True)

from langchain.tools import tool


class URLRetriever(BaseTool):
    name = "Retrieve From URL"
    description = "useful for when you need to access to a link, input a raw text url"

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
    name = "Google Search"
    description = "useful for when you need to search for information"

    def _run(self, keyword: str) -> str:
        return Google_Dorking(keyword=keyword)


retriever_tool = URLRetriever(
    name="Retrieve From URL",
    func=URLRetriever,
    description="useful when you need to access internet",
)

google_search_tool = GoogleSearch(
    name="Google Search",
    func=GoogleSearch,
    description="useful for when you need to search for information",
)

tools = [retriever_tool, google_search_tool]


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

agent.run(f"Hoang Kim Phu FPT")


# agent_executor = initialize_agent(
#     [tool],
#     llm,
#     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
#     handle_parsing_errors=True,
# )

# agent_executor.run("What is 438745398475893479 time 29087423453984")
