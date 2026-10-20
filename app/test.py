
import asyncio
import time


async def fetch_answer(name: str) -> str:
    print(f"Starting {name}")
    await asyncio.sleep(2)  # Simulates network waiting
    print(f"Finished {name}")
    return f"Answer from {name}"


async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_answer("request-A"),
        fetch_answer("request-B"),
        fetch_answer("request-C"),
    )

    print(results)
    print(f"Elapsed: {time.perf_counter() - start:.2f}s")


asyncio.run(main())
