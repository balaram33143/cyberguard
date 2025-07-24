import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def explain_threat_with_llm(url, threat_score):
    prompt = f"""
You are a cybersecurity assistant. A user visited the URL: {url}.
Threat Score: {threat_score}/100

Explain in simple terms why this URL may be dangerous (e.g., phishing, malware, scam) and what the user should do.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        explanation = response["choices"][0]["message"]["content"]
        return explanation.strip()
    except Exception as e:
        return f"Error generating explanation: {e}"
