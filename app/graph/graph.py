from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    create_complaint_node,
    update_complaint_node,
)
from app.graph.router import route_complaint
from app.graph.state import ComplaintState

builder = StateGraph(ComplaintState)

builder.add_node(
    "create_complaint",
    create_complaint_node,
)

builder.add_node(
    "update_complaint",
    update_complaint_node,
)

builder.add_conditional_edges(
    START,
    route_complaint,
)

builder.add_edge(
    "create_complaint",
    END,
)

builder.add_edge(
    "update_complaint",
    END,
)

graph = builder.compile()
