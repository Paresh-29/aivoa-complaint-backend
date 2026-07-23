from typing import Literal

from app.graph.state import ComplaintState


def route_complaint(
    state: ComplaintState,
) -> Literal["create_complaint", "update_complaint"]:
    if state["complaint"] is None:
        return "create_complaint"

    return "update_complaint"
