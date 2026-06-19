from enum import Enum
from pydantic import BaseModel, Field

class Category(str, Enum):
    billing = "billing"
    technical = "technical"
    refund = "refund"
    other = "other"

class SupportTicket(BaseModel):
    """Structured representation of a free-text support message."""
    customer_name: str = Field(..., description="Full name of the customer")
    contact: str = Field(..., description="Phone or email if present, else 'unknown'")
    order_id: str = Field(..., description="Order id if present, else 'unknown'")
    category: Category
    summary: str = Field(..., description="One-sentence summary of the issue")
