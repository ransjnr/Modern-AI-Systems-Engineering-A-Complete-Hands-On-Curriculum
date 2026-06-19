from app.graph import route_by_category

def test_routes_billing():
    assert route_by_category({"category": "billing", "clarify_count": 0}) == "billing"

def test_unclear_loops_then_falls_through():
    assert route_by_category({"category": "unclear", "clarify_count": 0}) == "clarify"
    assert route_by_category({"category": "unclear", "clarify_count": 2}) == "general"
