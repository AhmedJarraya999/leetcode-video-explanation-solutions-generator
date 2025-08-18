import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_explanation(problem_text: str) -> str:
    prompt = f"""
    Read the following LeetCode problem and generate:
    1. Step-by-step explanation
    2. Python solution code
    3. Time and space complexity analysis

    Problem:
    {problem_text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()
