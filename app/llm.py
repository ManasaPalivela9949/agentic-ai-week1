# # import requests

# # RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

# # def call_llm(prompt: str) -> str:
# #     response = requests.post(
# #         RENDER_API_URL,
# #         json={"prompt": prompt}
# #     )
# #     return response.json()["response"]



# # import requests
 
# # RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
# # def call_llm(prompt: str) -> str:
# #     print("[LLM] Calling LLM with prompt:", prompt)
# #     response = requests.post(
# #         RENDER_API_URL,
# #         json={"prompt": prompt}
# #     )
# #     result = response.json()["response"]
# #     print("[LLM] Response received")
# #     return result
 
 
# # import requests
# # import os

# # # ✅ Get your API key from environment variables
# # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # # ✅ Correct Groq endpoint
# # GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# # def call_llm(prompt: str) -> str:
# #     print("[LLM] Calling LLM with prompt:", prompt)

# #     headers = {
# #         "Authorization": f"Bearer {GROQ_API_KEY}",
# #         "Content-Type": "application/json"
# #     }

# #     payload = {
# #         "model": "llama-3.1-8b-instant",
# #         "messages": [
# #             {"role": "user", "content": prompt}
# #         ]
# #     }

# #     try:
# #         response = requests.post(
# #             GROQ_ENDPOINT,
# #             headers=headers,
# #             json=payload,
# #             timeout=30  # ✅ avoids hanging requests
# #         )

# #         data = response.json()
# #         print("[DEBUG] Raw API response:", data)

# #         # ✅ Handle errors safely
# #         if "error" in data:
# #             return f"LLM Error: {data['error']['message']}"

# #         # ✅ Safe extraction of text
# #         return data["choices"][0]["message"]["content"]

# #     except requests.exceptions.RequestException as e:
# #         # ✅ Network errors or timeouts
# #         return f"LLM Error: Request failed → {str(e)}"




# # import requests
 
# # RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
# # def call_llm(prompt: str) -> str:
# #     print("[LLM] Calling LLM with prompt:", prompt)
# #     response = requests.post(
# #         RENDER_API_URL,
# #         json={"prompt": prompt}
# #     )
# #     result = response.json()["response"]
# #     print("[LLM] Response received")
# #     return result



# import requests

# RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

# def call_llm(prompt: str) -> str:
#     print("[LLM] Calling LLM with prompt:", prompt)

#     try:
#         response = requests.post(
#             RENDER_API_URL,
#             json={"prompt": prompt},
#             timeout=10
#         )

#         # Check HTTP status
#         if response.status_code != 200:
#             print("[LLM] API error. Status:", response.status_code)
#             print("[LLM] Raw response:", response.text)
#             return "LLM_FAILED"

#         # Try parsing JSON safely
#         try:
#             data = response.json()
#         except ValueError:
#             print("[LLM] Response is not valid JSON")
#             print("[LLM] Raw response:", response.text)
#             return "LLM_FAILED"

#         # Safely get response text
#         result = data.get("response")
#         if not result:
#             print("[LLM] 'response' field missing in JSON")
#             print("[LLM] Full JSON:", data)
#             return "LLM_FAILED"

#         print("[LLM] Response received")
#         return result

#     except requests.exceptions.RequestException as e:
#         print("[LLM] Network or request error:", e)
#         return "LLM_FAILED"



import requests
 
RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
def call_llm(prompt: str) -> str:
    print("[LLM] Calling LLM with prompt:", prompt)
 
    try:
        response = requests.post(
            RENDER_API_URL,
            json={"prompt": prompt},
            timeout=10
        )
 
        if response.status_code != 200:
            print("[LLM] Non-200 response:", response.status_code)
            return "LLM_FAILED"
 
        try:
            data = response.json()
        except Exception:
            print("[LLM] Response not JSON:", response.text)
            return "LLM_FAILED"
 
        if "response" not in data:
            print("[LLM] Missing 'response' key")
            return "LLM_FAILED"
 
        print("[LLM] Response received successfully")
        return data["response"]
 
    except Exception as e:
        print("[LLM] Exception:", str(e))
        return "LLM_FAILED"