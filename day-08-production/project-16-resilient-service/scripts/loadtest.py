"""Dependency-free async load test. Run: python scripts/loadtest.py"""
import asyncio, time, httpx

async def hit(client, q):
    r = await client.post("http://localhost:8013/ask", json={"question": q})
    return r.status_code

async def main(n=50):
    qs = ["What is a vector database?"] * n      # identical -> cache should win
    async with httpx.AsyncClient(timeout=30) as c:
        t0 = time.time()
        codes = await asyncio.gather(*(hit(c, q) for q in qs))
        print(f"{n} requests in {time.time()-t0:.2f}s; 200s={codes.count(200)}")

asyncio.run(main())
