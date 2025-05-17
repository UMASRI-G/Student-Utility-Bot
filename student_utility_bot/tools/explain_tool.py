from tools.llm_setup import llm

def explain_concept(topic: str) -> str:
    prompt = f"Explain the following concept to a student in simple terms: {topic}"
    return llm.invoke(prompt).content
