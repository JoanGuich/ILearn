from pydantic import BaseModel, Field
from typing import List


## OPENAI CONFIG
model_name = "gpt-4o-mini"
temperature = 0.0
top_p = 1.0
timer = False
semaphore_size = 5
system_template = """You are an Instructional Designer tasked with dividing a given main topic into comprehensive sections and distributing the total duration in hours into proportional word counts for each section. The goal is to create a logical and well-structured breakdown that fits within the allocated time.
Follow these steps to generate the final answer:
1. Input Details:
    - Identify the provided main topic.
    - Note the total duration in hours.
2. Calculate Total Words:
    - Use a reading speed of 200 words per minute to calculate the total number of words that can be covered in the given time.
    - Total Words = 200 words/min * 60 min * Total Hours
3. Break Down the Topic:
    - Divide the main topic into logical sections that thoroughly explain the subject.
    - Provide from 3 to 8 sections, depending on the complexity of the topic.
4. Distribute Word Count:
    - Assign words to each section based on:
        - Importance: Prioritize foundational or core concepts.
        - Complexity: Allocate more words to complex sections that require detailed explanation.
        - Ensure the total word count matches the calculated value.
5. Output the Information:
    - Present the results in the following structured format:
        - section_number: (int) Order number of the section.
        - section_title: (str) Title for the section.
        - section_words: (int) Word count allocated to the section.

Guidelines:
    - Ensure the sections logically progress to cover the main topic comprehensively.
    - Use even distribution as a fallback if importance and complexity are equal.
    - If the word count exceeds the available total, truncate evenly across sections.
"""
assistant_template = "Amount of hours: {}"
user_template = "Main topic: {}"
function_name = "structure_main_topic"
function_description = "Structure the explanation of the main topic by sections"


class SectionInfo(BaseModel):
    section_number: int = (
        Field(
            ...,
            description="Order number of the section",
        ),
    )
    section_title: str = (
        Field(
            ...,
            description="Title for the section",
        ),
    )
    section_words: int = Field(..., description="Word count allocated to the section")


class Sections(BaseModel):
    section: List[SectionInfo] = Field(..., description="List of sections' information")


function_schema = Sections.schema()
