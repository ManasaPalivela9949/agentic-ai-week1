<<<<<<< HEAD
# # #ORCHESTRATOR
# # from app.control import decide_next_step
# # from app.llm import call_llm
# # from app.memory import init_memory

# # def run_agent(goal: str):
# #     memory = init_memory(goal)

# #     print("Agent started")
# #     print("Goal:", goal)

# #     step = decide_next_step(memory)

# #     if step == "call_llm":
# #         response = call_llm(goal)
# #         print("LLM Response:", response)

# #     print("Agent finished")



# # from app.control import decide_next_step
# # from app.llm import call_llm
# # from app.memory import init_memory
# # from app.tools import fetch_joke_tool
 
# # def run_agent(goal: str):
# #     memory = init_memory(goal)
 
# #     print("\n[AGENT] Starting agent")
# #     print("[AGENT] Goal:", goal)
 
# #     while True:
# #         print("\n[AGENT] Loop iteration started")
# #         step = decide_next_step(memory)
# #         print("[AGENT] Control decided:", step)
 
# #         if step == "call_llm":
# #             response = call_llm(goal)
# #             memory["steps"].append(response)
# #             print("[AGENT] LLM Response:", response)
 
# #         elif step == "use_tool":
# #             result = fetch_joke_tool()
# #             memory["steps"].append(result)
# #             print("[AGENT] Tool Result:", result)
 
# #         elif step == "stop":
# #             print("[AGENT] Agent stopped cleanly")
# #             break


# # Practice 

# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import init_memory
# from app.tools import fetch_product_price_tool  # here changed the logic fatch joke to product prices

# def run_agent(goal: str):
#     memory = init_memory(goal)
 
#     print("\n[AGENT] Starting agent")
#     print("[AGENT] Goal:", goal)
 
#     while True:
#         print("\n[AGENT] Loop iteration started")
#         step = decide_next_step(memory)
#         print("[AGENT] Control decided:", step)
 
#         if step == "call_llm":
#             response = call_llm(goal)
#             memory["steps"].append(response)
#             print("[AGENT] LLM Response:", response)
 
#         elif step == "use_tool":
#             result = fetch_product_price_tool() # here changed the logic fatch joke to product prices
#             memory["steps"].append(result)
#             print("[AGENT] Tool Result:", result)
 
#         elif step == "stop":
#             print("[AGENT] Agent stopped cleanly")
#             break

from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import market_explainer_tool
=======
# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import init_memory

# def run_agent(goal: str):
#     memory = init_memory(goal)

#     print("Agent started")
#     print("Goal:", goal)

#     while True:
#         step = decide_next_step(memory)

#         if step == "call_llm":
#             response = call_llm(goal)
#             memory["steps"].append(response)
#             print("LLM Response:", response)

#         elif step == "stop":
#             print("Agent stopped")
#             break




from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import print_tool
>>>>>>> main
 
def run_agent(goal: str):
    print("\n[AGENT] Starting agent")
    memory = init_memory(goal)
 
<<<<<<< HEAD
    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)
 
    while True:
        print("\n[AGENT] Loop iteration")
=======
    while True:
        print("\n[AGENT] Loop iteration started")
>>>>>>> main
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)
 
        if step == "call_llm":
<<<<<<< HEAD
            response = call_llm(goal)
            memory["steps"].append(response)
            print("[AGENT] LLM Response:", response)
 
        elif step == "use_tool":
            result = market_explainer_tool(memory["steps"][-1])
            memory["steps"].append(result)
            print("[AGENT] Tool executed")
 
        elif step == "stop":
            print("[AGENT] Agent stopped cleanly")
            break
=======
            print("[AGENT] Calling LLM")
            response = call_llm(goal)
            memory["steps"].append(response)
 
        elif step == "use_tool":
            print("[AGENT] Using tool")
            result = print_tool(memory["steps"][-1])
            memory["steps"].append(result)
 
        elif step == "stop":
            print("[AGENT] STOP → exiting loop")
            break
 
    print("[AGENT] Agent finished")
>>>>>>> main
