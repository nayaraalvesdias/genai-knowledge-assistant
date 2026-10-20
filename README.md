# genai-knowledge-assistant


python -m uvicorn app.main:app --reload
python -m pytest -v

python -m pip install openai
export OPENAI_API_KEY="paste-your-api-key-here"
python -c 'import os; print("API key configured:", bool(os.getenv("OPENAI_API_KEY")))'