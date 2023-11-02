import json
import re

import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import WebBaseLoader


def retriever(url):
    prompt = f"""Extract a link from following data and return the link only, do not explain or introduce. {url}"""
    payload = json.dumps({"text": prompt})
    headers = {"Content-Type": "application/json", "X-API-Key": ""}
    url = "http://127.0.0.1:8080/langchain"
    response = requests.request("POST", url, headers=headers, data=payload)
    url = response.json()
    try:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
    except Exception as e:
        return "Data is not available, try another link"

    prompt = f"""Tóm tắt nội dung sau một cách chi tiết. Không cần dẫn dắt, không cần giải thích. Sau đây là một phần thông tin: 
    {soup.get_text()[:7000]}
    """
    payload = json.dumps(
        {
            "messages": [
                {
                    "content": "You are a helpful assistant. You will help user summarize data.",
                    "role": "system",
                },
                {"content": soup.get_text()[:7000], "role": "user"},
            ]
        }
    )
    headers = {"Content-Type": "application/json", "X-API-Key": ""}
    url = "http://127.0.0.1:8000/v1/chat/completions"
    response = requests.request("POST", url, headers=headers, data=payload)
    summarize = response.json()
    return summarize
