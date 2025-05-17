from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

from tools.email_tool import generate_email
from tools.explain_tool import explain_concept
from tools.learning_tool import learning_path
from tools.math_tool import solve_math

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

tools = [
    Tool(name="Email Generator", func=generate_email, description="Draft student emails"),
    Tool(name="Concept Explainer", func=explain_concept, description="Explain academic concepts"),
    Tool(name="Learning Planner", func=learning_path, description="Create personalized study plans"),
    Tool(name="Math Solver", func=solve_math, description="Solve math problems step-by-step"),
]

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
