import google.generativeai as genai

def generate_research_report(topic, web_content, api_key, report_length):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a professional research analyst.

Write a structured research report on the given topic.

FORMAT:

1. Executive Summary
2. Key Findings
3. Important Insights
4. Advantages and Disadvantages
5. Conclusion

Rules:
- Use headings exactly as above
- Use bullet points where needed
- Do NOT merge everything into one paragraph
- Keep it clear and professional
- Only use provided sources

Report Length:
{report_length}

If Report Length is:
- Short: Write approximately 300–500 words.
- Medium: Write approximately 700–900 words.
- Detailed: Write approximately 1200–1800 words.

Topic:
{topic}

Sources:
{web_content}
"""

    response = model.generate_content(prompt)
    return response.text