
def create_content_prompt(topic, content_type, tone, length):

    return f"""
You are an expert AI content generator.

Create content based on these requirements:

Topic: {topic}
Content Type: {content_type}
Tone: {tone}
Length: {length}

Instructions:
- Stay focused on the topic.
- Follow the requested content type.
- Use the requested tone.
- Make the content clear and engaging.
- Use correct grammar.
- Return only the generated content.
"""
