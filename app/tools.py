
# # Tools will be added in Week 2


# # import requests
 
# # def fetch_joke_tool() -> str:
# #     print("[TOOL] Calling external Joke API")
 
# #     response = requests.get(
# #         "https://official-joke-api.appspot.com/random_joke",
# #         timeout=5
# #     )
 
# #     if response.status_code != 200:
# #         print("[TOOL] API failed")
# #         return "TOOL_FAILED"
 
# #     data = response.json()
# #     joke = f"{data['setup']} — {data['punchline']}"
 
# #     print("[TOOL] Joke fetched successfully")
# #     return joke




# # import requests
# # import random
 
# # def fetch_joke_tool() -> str:
# #     print("[TOOL] Calling external Joke API")
 
# #     # Simulate failure sometimes (for learning)
# #     if random.choice([True, False]):
# #         print("[TOOL] Simulated tool failure")
# #         return "TOOL_FAILED"
 
# #     response = requests.get(
# #         "https://official-joke-api.appspot.com/random_joke",
# #         timeout=5
# #     )
 
# #     if response.status_code != 200:
# #         print("[TOOL] API error")
# #         return "TOOL_FAILED"
 
# #     data = response.json()
# #     joke = f"{data['setup']} — {data['punchline']}"
# #     print("[TOOL] Joke fetched successfully")
# #     return joke
 




# import requests
# import random


# # -------------------------
# # Formatting Tool
# # -------------------------
# def format_product_output(product: dict) -> str:
#     """
#     Formats product data into a clean, readable structure
#     """
#     return (
#         "\n🛒 Product Details\n"
#         "----------------------\n"
#         f"📦 Name     : {product['title']}\n"
#         f"💰 Price    : ₹{product['price']}\n"
#         f"⭐ Rating   : {product['rating']} / 5\n"
#         f"🏷️ Category : {product['category']}\n"
#     )


# # -------------------------
# # Product Price Tool
# # -------------------------
# def fetch_product_price_tool() -> str:
#     print("[TOOL] Calling Product Price API")

#     # Simulate failure sometimes (for learning)
#     if random.choice([True, False]):
#         print("[TOOL] Simulated tool failure")
#         return "TOOL_FAILED"

#     try:
#         response = requests.get(
#             "https://fakestoreapi.com/products/1",
#             timeout=5
#         )

#         if response.status_code != 200:
#             print("[TOOL] API error")
#             return "TOOL_FAILED"

#         data = response.json()

#         product = {
#             "title": data.get("title", "N/A"),
#             "price": data.get("price", "N/A"),
#             "rating": data.get("rating", {}).get("rate", "N/A"),
#             "category": data.get("category", "N/A")
#         }

#         print("[TOOL] Product data fetched successfully")

#         # Apply formatter tool
#         return format_product_output(product)

#     except Exception as e:
#         print("[TOOL] Exception occurred:", e)
#         return "TOOL_FAILED"


 
def market_explainer_tool(text: str) -> str:
    print("\n[TOOL] MARKET EXPLANATION:")
    print(text)
    return "EXPLANATION_PRESENTED"
 


