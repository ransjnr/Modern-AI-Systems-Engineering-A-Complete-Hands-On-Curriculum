"""Seeded in-memory SQLite + a read-only executor (blocks non-SELECT)."""
import sqlite3

SCHEMA = """CREATE TABLE IF NOT EXISTS sales (
  id INTEGER PRIMARY KEY, region TEXT, product TEXT,
  units INTEGER, revenue REAL, sale_date TEXT);"""
SEED = [
    ("North", "Widget", 120, 2400.0, "2025-01-10"),
    ("South", "Widget", 80, 1600.0, "2025-01-11"),
    ("North", "Gadget", 50, 3000.0, "2025-02-03"),
    ("East", "Gadget", 30, 1800.0, "2025-02-15"),
    ("South", "Sprocket", 200, 1000.0, "2025-03-01"),
]

def get_conn():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO sales(region,product,units,revenue,sale_date) "
                     "VALUES (?,?,?,?,?)", SEED)
    conn.commit()
    return conn

CONN = get_conn()
SCHEMA_DESC = ("Table sales(id, region, product, units INTEGER, revenue REAL, "
               "sale_date TEXT). Dates are 'YYYY-MM-DD'.")

def run_select(sql: str):
    """Run a READ-ONLY query. Returns (rows, error). Blocks non-SELECT."""
    if not sql.strip().lower().startswith("select"):
        return [], "Rejected: only SELECT statements are allowed."
    try:
        cur = CONN.execute(sql)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()], ""
    except Exception as e:
        return [], f"SQLError: {e}"
