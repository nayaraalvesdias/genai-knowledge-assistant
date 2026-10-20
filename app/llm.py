from openai import AsyncOpenAI


async def generate_answer(question: str) -> str:
    async with AsyncOpenAI(
        timeout=30.0,
        max_retries=1,
    ) as client:
        response = await client.responses.create(
             model="gpt-4o-mini",
            instructions=(
                "You are a helpful technical assistant. "
                "Give accurate, concise explanations. "
                "If you are uncertain, say so."
            ),
            input=question,
            max_output_tokens=500,
        )

    return response.output_text

