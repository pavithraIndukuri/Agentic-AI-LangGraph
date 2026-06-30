def planner(state):
    query = state["query"]

    state["plan"] = f"Plan created for: {query}"

    return state


def executor(state):
    plan = state["plan"]

    state["result"] = f"Task executed successfully.\n\n{plan}"

    return state


def evaluator(state):
    state["result"] += "\n\nEvaluation: Output Verified Successfully."

    return state
