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
        payload = json.dumps({"text": url})
        headers = {"Content-Type": "application/json", "X-API-Key": ""}
        url = "http://127.0.0.1:8080/crawl"
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
    except Exception as e:
        return "Data is not available, try another link"

    prompt = f"""Tóm tắt nội dung sau một cách chi tiết. Không cần dẫn dắt, không cần giải thích. Sau đây là một phần thông tin: 
    {data[:7000]}
    """
    payload = json.dumps({"text": prompt})
    headers = {"Content-Type": "application/json", "X-API-Key": ""}
    url = "http://127.0.0.1:8080/langchain"
    response = requests.request("POST", url, headers=headers, data=payload)
    summarize = response.json()
    return summarize
