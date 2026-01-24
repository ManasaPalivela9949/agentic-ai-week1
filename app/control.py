<<<<<<< HEAD
# # def decide_next_step(memory: dict) -> str:
# #     """
# #     Control flow decides what happens next.
# #     """
# #     if not memory["has_responded"]:
# #         return "call_llm"

# #     return "stop"



# # def decide_next_step(memory: dict) -> str:
# #     print("\n[CONTROL] Current memory:", memory)
 
# #     if memory["completed"]:
# #         return "stop"
 
# #     # Step 1: Ask LLM
# #     if len(memory["steps"]) == 0:
# #         print("[CONTROL] First step → CALL LLM")
# #         return "call_llm"
 
# #     # Step 2: Use external tool
# #     if len(memory["steps"]) == 1:
# #         print("[CONTROL] Second step → USE TOOL")
# #         return "use_tool"
 
# #     # Step 3: Stop
# #     print("[CONTROL] All steps done → STOP")
# #     memory["completed"] = True
# #     return "stop"
 



# def decide_next_step(memory: dict) -> str:
#     print("\n[CONTROL] Current memory:", memory)
 
#     if memory["completed"]:
#         return "stop"
 
#     # Step 1: Call LLM
#     if len(memory["steps"]) == 0:
#         print("[CONTROL] First step → CALL LLM")
#         return "call_llm"
 
#     # Step 2: Use tool
#     if len(memory["steps"]) == 1:
#         print("[CONTROL] Second step → USE TOOL")
#         return "use_tool"
 
#     # Handle tool failure
#     last_step = memory["steps"][-1]
#     if last_step == "TOOL_FAILED":
#         if memory["tool_retries"] < 1:
#             memory["tool_retries"] += 1
#             print("[CONTROL] Tool failed → RETRY")
#             return "use_tool"
#         else:
#             print("[CONTROL] Tool failed again → STOP")
#             memory["completed"] = True
#             return "stop"
 
#     # Successful execution → stop
#     print("[CONTROL] Tool succeeded → STOP")
#     memory["completed"] = True
#     return "stop"
 
=======
# def decide_next_step(memory: dict) -> str:
#     if memory["completed"]:
#         return "stop"

#     if len(memory["steps"]) == 0:
#         return "call_llm"

#     memory["completed"] = True
#     return "stop"

>>>>>>> main


def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)
 
    if memory["completed"]:
<<<<<<< HEAD
        return "stop"
 
    # Step 1: Get explanation from LLM
    if len(memory["steps"]) == 0:
        return "call_llm"
 
    # Step 2: Present explanation using tool
    if len(memory["steps"]) == 1:
        return "use_tool"
 
    # Step 3: Stop agent
=======
        print("[CONTROL] completed=True → STOP")
        return "stop"
 
    if len(memory["steps"]) == 0:
        print("[CONTROL] First step → CALL LLM")
        return "call_llm"
 
    if len(memory["steps"]) == 1:
        print("[CONTROL] Second step → USE TOOL")
        return "use_tool"
 
    print("[CONTROL] All steps done → STOP")
>>>>>>> main
    memory["completed"] = True
    return "stop"