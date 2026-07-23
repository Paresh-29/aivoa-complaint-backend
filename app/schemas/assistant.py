from typing import Any

from pydantic import BaseModel


class AssistantRequest(BaseModel):
    message: str
    complaint: dict[str, Any] | None = None
