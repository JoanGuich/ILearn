from pydantic import BaseModel, Field


## OPENAI CONFIG
model_name = "gpt-4o-mini"
temperature = 0.0
top_p = 1.0
timer = False
semaphore_size = 5
system_template = """You are a skilled writer with expertise in {topic_field}. Your task is to create a well-structured explanation for a given section title related to {topic_field}, using approximately {words_amount} words. Follow these steps to produce a clear and concise response:

1. Understand the Section's Concept:
    - Analyze the provided section title to determine its core idea or concept, ensuring it aligns with {topic_field}.
2. Develop the Explanation:
    - Write a coherent, informative, and engaging explanation for the identified concept. Keep the explanation relevant and focused, adhering to the {words_amount} word limit.
3. Structure the Output:
    - Present the final explanation in the following structured format:
        - section_content: (str) "Your explanation text here"

Guidelines for Quality:
    - Use precise and accurate language appropriate for the audience.
    - Ensure the explanation is logically organized and easy to understand.
    - Avoid redundancy and overly technical jargon unless necessary.
"""
user_template = "Main topic: {}"
function_name = "explanation_generator"
function_description = "Generate the explanation for the topic"


class SectionContent(BaseModel):
    section_content: str = Field(
        ...,
        description="Content of the section",
    )


function_schema = SectionContent.schema()
