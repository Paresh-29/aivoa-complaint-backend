import uuid
from datetime import date, datetime

from sqlalchemy import Date, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    customer_name: Mapped[str] = mapped_column(
        String(255),
    )

    product_name: Mapped[str] = mapped_column(
        String(255),
    )

    batch_number: Mapped[str] = mapped_column(
        String(100),
    )

    manufacturing_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    expiry_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    complaint_type: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    complaint_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    quantity_affected: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    severity: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    suggested_action: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    risk_assessment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    source_type: Mapped[str] = mapped_column(
        String(50),
    )

    uploaded_file: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
