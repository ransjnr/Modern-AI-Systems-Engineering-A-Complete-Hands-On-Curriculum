import pytest
from pydantic import ValidationError
from app.schemas import SupportTicket, Category

def test_valid_ticket():
    t = SupportTicket(customer_name="Ama", contact="unknown", order_id="8842",
                      category="refund", summary="faulty cable")
    assert t.category == Category.refund

def test_invalid_category():
    with pytest.raises(ValidationError):
        SupportTicket(customer_name="Ama", contact="x", order_id="1",
                      category="nope", summary="s")
