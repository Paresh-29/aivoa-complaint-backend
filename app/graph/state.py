from typing import Any, TypedDict


class ComplaintState(TypedDict):
    complaint: dict[str, Any] | None
    message: str
