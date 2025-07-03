# app/ai_analysis.py
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def analyze_headlines(headlines):
    prompt = "Analyze each of the following headlines and say whether it's Positive, Neutral, or Negative for the stock market:\n\n"
    for h in headlines:
        prompt += f"- {h['title']}\n"
    prompt += "\nGive response like:\n[{'title': '...', 'sentiment': 'Positive', 'confidence': 87, 'reason': '...'}, ...]"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content
