
# # from app.agent import run_agent

# from app.agent import run_agent

# if __name__ == "__main__":
#     goal = "Explain what is AI"
#     run_agent(goal)





# # if __name__ == "__main__":
# #     goal = "Summarize recent AI news"
# #     run_agent(goal)


# # from app.agent import run_agent
 
# # if __name__ == "__main__":
# #     goal = "Explain why humor helps in communication"
# #     run_agent(goal)



# # from app.agent import run_agent
 
# # if __name__ == "__main__":
# #     goal = "Explain what is AI"
# #     run_agent(goal)


# # from app.agent import run_agent
 
# # if __name__ == "__main__":
# #     goal = "Explain why humor improves communication"
# #     run_agent(goal)


# from app.agent import run_agent
 
# if __name__ == "__main__":
#     goal = "Product prices from Amazon"
#     run_agent(goal)



# from app.agent import run_agent
 
# if __name__ == "__main__":

#     goal = "Explain inflation in very simple terms"
#     goal = "Explain how stock prices move"

#     run_agent(goal)



'''
Assignment on Build an agent that explains a college notice
in simple language
'''

from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import read_notice_tool


def run_agent(goal: str):
    memory = init_memory(goal)

    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)

    while True:
        step = decide_next_step(memory)
        print("[CONTROL] Next step:", step)

        if step == "read_notice":
            notice = read_notice_tool("notice.txt")
            memory["notice"] = notice
            memory["steps"].append("read_notice")

        elif step == "explain_notice":
            prompt = f"""
Explain the following college notice in very simple language
so that students can easily understand:

{memory['notice']}
"""
            explanation = call_llm(prompt)
            memory["explanation"] = explanation
            memory["steps"].append("explain_notice")

        elif step == "present_explanation":
            print("\n📢 Simple Explanation:")
            print(memory["explanation"])
            memory["steps"].append("present_explanation")

        elif step == "stop":
            print("\n[AGENT] Agent stopped cleanly")
            break


if __name__ == "__main__":
    run_agent("Explain a college notice in simple language")

