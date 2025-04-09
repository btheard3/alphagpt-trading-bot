from openai import OpenAI

client = OpenAI()

def review_reflections(reflection_logs: list) -> str:
    """
    Uses GPT to analyze trader mindset and behavior patterns.
    """
    prompt = f"""
    You are a mindset and performance coach for traders.
    Analyze the following trade reflections. Identify common patterns, mindset strengths, weaknesses, and areas for improvement.

    Reflections:
    {reflection_logs}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a mindset and performance coach for traders."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def review_explanations(explanations: list) -> str:
    """
    Uses GPT to summarize and evaluate multiple trade explanations.
    """
    prompt = f"""
    You are an expert options mentor.
    Summarize common themes from the following trade explanations.
    Identify strengths, weaknesses, and improvement opportunities.

    Explanations:
    {explanations}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert options mentor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
