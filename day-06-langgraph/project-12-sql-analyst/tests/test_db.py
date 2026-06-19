from app.db import run_select

def test_blocks_non_select():
    rows, err = run_select("DROP TABLE sales")
    assert rows == [] and "only SELECT" in err

def test_runs_select():
    rows, err = run_select("SELECT COUNT(*) AS n FROM sales")
    assert err == "" and rows[0]["n"] == 5

def test_reports_error():
    rows, err = run_select("SELECT * FROM nope")
    assert "SQLError" in err
