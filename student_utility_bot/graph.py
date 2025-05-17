from langgraph.graph import StateGraph
from typing import TypedDict
from agent import agent_executor

class GraphState(TypedDict):
    user_input: str
    result: str

def input_node(state: GraphState) -> GraphState:
    return {"user_input": state["user_input"]}

def agent_node(state: GraphState) -> GraphState:
    result = agent_executor.run(state["user_input"])
    return {"user_input": state["user_input"], "result": result}

def output_node(state: GraphState) -> GraphState:
    return state

def build_graph():
    workflow = StateGraph(GraphState)
    workflow.add_node("input", input_node)
    workflow.add_node("agent", agent_node)
    workflow.add_node("output", output_node)

    workflow.set_entry_point("input")
    workflow.add_edge("input", "agent")
    workflow.add_edge("agent", "output")
    workflow.set_finish_point("output")

    return workflow.compile()
