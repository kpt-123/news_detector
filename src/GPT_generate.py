
from openai import OpenAI
api_key="your_key"
def gpt_generate(prompt):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=2048
    )
    return response.choices[0].message.content