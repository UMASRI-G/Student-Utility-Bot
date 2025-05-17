from tools.llm_setup import llm

def solve_math(problem: str) -> str:
    prompt = f"Solve the following math problem step-by-step: {problem}"
    return llm.invoke(prompt).content