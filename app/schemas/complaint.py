from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ComplaintCreate(BaseModel):
    customer_name: str | None = None
    product_name: str | None = None
    product_strength: str | None = None
    batch_number: str | None = None

    manufacturing_date: date | None = None
    expiry_date: date | None = None

    complaint_type: str | None = None
    complaint_description: str | None = None
    quantity_affected: str | None = None

    severity: str | None = None
    priority: str | None = None

    suggested_action: str | None = None
    risk_assessment: str | None = None

    complaint_source: str | None = None
    uploaded_file: str | None = None


class ComplaintResponse(ComplaintCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
