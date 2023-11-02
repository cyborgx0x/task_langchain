import http.client
import json

import requests


def Google_Dorking(keyword, num_results=10):
    api_key = "62c6bb0fa4ad2af9a881a2abf578dbb3f1ac1d98"
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({"q": f"{keyword}", "num": num_results})
    headers = {"X-API-KEY": f"{api_key}", "Content-Type": "application/json"}
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result_google = data.decode("utf-8")
    prompt = f"""
extract a list of link from following data for me, return in format of: url: title, desc. do not explain
{result_google}
"""
    payload = json.dumps({"text": prompt})
    headers = {"Content-Type": "application/json", "X-API-Key": ""}
    url = "http://127.0.0.1:8080/langchain_markdown"
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()
