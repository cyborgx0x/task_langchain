import json
from typing import Any, List, Mapping, Optional

import requests
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM


class CustomLLM(LLM):
    n: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        payload = json.dumps({"text": prompt, "stop": stop})
        headers = {"Content-Type": "application/json", "X-API-Key": ""}
        url = "http://127.0.0.1:8000/langchain"
        response = requests.request("POST", url, headers=headers, data=payload)
        if stop:
            return response.json().split(stop[0])[0]
        else:
            return response.json()

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}


