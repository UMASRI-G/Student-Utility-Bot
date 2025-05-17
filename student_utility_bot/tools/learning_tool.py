from tools.llm_setup import llm

def learning_path(subject: str) -> str:
    prompt = f"Create a personalized 30-day learning plan for a student to master: {subject}"
    return llm.invoke(prompt).content
