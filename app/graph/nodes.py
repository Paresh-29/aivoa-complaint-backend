from app.ai.groq_client import create_complaint, update_complaint
from app.graph.state import ComplaintState


def create_complaint_node(state: ComplaintState) -> ComplaintState:
    state["complaint"] = create_complaint(
        state["message"],
    )

    return state


def update_complaint_node(state: ComplaintState) -> ComplaintState:
    state["complaint"] = update_complaint(
        complaint=state["complaint"],
        message=state["message"],
    )

    return state
