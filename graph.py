from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents import planner, executor, evaluator


class AgentState(TypedDict):
    query: str
    plan: str
    result: str


workflow = StateGraph(AgentState)

workflow.add_node("Planner", planner)
workflow.add_node("Executor", executor)
workflow.add_node("Evaluator", evaluator)

workflow.set_entry_point("Planner")

workflow.add_edge("Planner", "Executor")
workflow.add_edge("Executor", "Evaluator")
workflow.add_edge("Evaluator", END)

graph = workflow.compile()
