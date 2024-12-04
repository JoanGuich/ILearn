# Create your models here.
import json
from time import time
from typing import Any

import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential


class OpenAIFunctionContext:
    """OpenAI model that calls a function on text.
    This class is meant to be subclassed with the following attributes:
    - system_template: str - The system template for the OpenAI API
    - assistant_template: str - The assistant template for the OpenAI API. This should contain a {} where the text should be inserted
    - user_template: str - The user template for the OpenAI API. This should contain a {} where the text should be inserted.
    - function_name: str - The name of the function
    - function_description: str - The description of the function
    - function_schema: dict[str, Any] - The schema of the function
    """

    system_template: str
    assistant_template: str
    user_template: str
    function_name: str
    function_description: str
    function_schema: str

    def __init__(
        self,
        model_name: str,
        temperature: float = 1.0,
        top_p: float = 1.0,
        timer: bool = False,
    ) -> None:
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.timer = timer

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
    def get_function_inputs(self, context: str, text: str) -> dict[str, Any] | None:
        if text == "" or context == "":
            return None

        if self.timer:
            time_start = time()

        response = openai.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_template},
                {
                    "role": "assistant",
                    "content": self.assistant_template.format(context),
                },
                {"role": "user", "content": self.user_template.format(text)},
            ],
            functions=[
                {
                    "name": self.function_name,
                    "description": self.function_description,
                    "parameters": self.function_schema,
                }
            ],
            function_call={"name": self.function_name},
            temperature=self.temperature,
        )

        if self.timer:
            time_end = time()
            print(f"Time: {time_end - time_start:.2f}")

        function_arguments = json.loads(
            response.choices[0].message.function_call.arguments
        )
        return function_arguments

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(4))
    async def aget_function_inputs(
        self, context: str, text: str
    ) -> dict[str, Any] | None:
        """Async version of get_function_inputs"""
        if text == "" or context == "":
            return None

        if self.timer:
            time_start = time()

        response = await openai.chat.completions.acreate(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_template},
                {
                    "role": "assistant",
                    "content": self.assistant_template.format(context),
                },
                {"role": "user", "content": self.user_template.format(text)},
            ],
            functions=[
                {
                    "name": self.function_name,
                    "description": self.function_description,
                    "parameters": self.function_schema,
                }
            ],
            function_call={"name": self.function_name},
            temperature=self.temperature,
        )

        if self.timer:
            time_end = time()
            print(f"Time: {time_end - time_start:.2f}")

        function_arguments = json.loads(
            response.choices[0].message.function_call.arguments
        )
        return function_arguments

    def predict_on_text(self, context: str, text: str) -> list[dict[str, Any]]:
        res = self.get_function_inputs(context, text)
        if res is None:
            return []
        return [res]

    async def async_predict_on_text(
        self, context: str, text: str
    ) -> list[dict[str, Any]]:
        res = await self.aget_function_inputs(text)
        if res is None:
            return []
        return [res]
