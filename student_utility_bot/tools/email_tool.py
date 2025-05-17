from tools.llm_setup import llm

def generate_email(context: str) -> str:
    prompt = f"Write a formal leave application email for the following request: {context}"
    response = llm.invoke(prompt)
    print("Email tool output:", response.content)
    return response.content