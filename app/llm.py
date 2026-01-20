# import requests

# RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

# def call_llm(prompt: str) -> str:
#     response = requests.post(
#         RENDER_API_URL,
#         json={"prompt": prompt}
#     )
#     return response.json()["response"]



import requests
 
RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
def call_llm(prompt: str) -> str:
    print("[LLM] Calling LLM with prompt:", prompt)
    response = requests.post(
        RENDER_API_URL,
        json={"prompt": prompt}
    )
    result = response.json()["response"]
    print("[LLM] Response received")
    return result
 
 

