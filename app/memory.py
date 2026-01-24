# # def init_memory(goal: str) -> dict:
# #     return {
# #         "goal": goal,
# #         "has_responded": False
# #     }

# #“Memory will grow later. Today it exists.”




# # def init_memory(goal: str) -> dict:
# #     return {
# #         "goal": goal,
# #         "has_responded": False,
# #          "completed": False
# #     }



# # memory.py

# # def init_memory(goal):
# #     return {
# #         "goal": goal,
# #         "steps": [],
# #         "completed": False
# #     }



# def init_memory(goal: str) -> dict:
#     print("[MEMORY] Initializing memory")
 
#     return {
#         "goal": goal,
#         "steps": [],
#         "completed": False,
#         "tool_retries": 0
#     }



def init_memory(goal: str) -> dict:
    return {
        "goal": goal,
        "steps": [],
        "completed": False
<<<<<<< HEAD
    }

=======
    }
>>>>>>> main
