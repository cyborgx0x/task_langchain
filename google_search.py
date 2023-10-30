import http.client
import json


def Google_Dorking(keyword, num_results=5):
    api_key = "62c6bb0fa4ad2af9a881a2abf578dbb3f1ac1d98"
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({"q": f"{keyword}", "num": num_results})
    headers = {"X-API-KEY": f"{api_key}", "Content-Type": "application/json"}
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result_google = data.decode("utf-8")
    return json.loads(result_google)
