import openai
import aiofiles
from time import time
from tenacity import retry, stop_after_attempt, wait_random_exponential


class OpenAITextToSpeech:
    """Class to handle text-to-speech conversion using the OpenAI API."""

    def __init__(
        self,
        model_name: str,
        voice: str,
        timer: bool = False,
    ) -> None:
        self.model_name = model_name
        self.voice = voice
        self.timer = timer

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
    def text_to_speech(self, text: str, output_file: str) -> None:
        if not text:
            raise ValueError("Input text cannot be empty.")

        if self.timer:
            time_start = time()

        response = openai.audio.speech.create(
            model=self.model_name,
            voice=self.voice,
            input=text,
        )

        if self.timer:
            time_end = time()
            print(f"Time taken: {time_end - time_start:.2f} seconds")

        # Assuming the response is a binary audio content
        with open(output_file, "wb") as f:
            f.write(response.content)

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
    async def atext_to_speech(self, text: str, output_file: str) -> None:
        """Asynchronous version of text_to_speech."""
        if not text:
            raise ValueError("Input text cannot be empty.")

        if self.timer:
            time_start = time()

        response = await openai.audio.speech.acreate(
            model=self.model_name,
            voice=self.voice,
            input=text,
        )

        if self.timer:
            time_end = time()
            print(f"Time taken: {time_end - time_start:.2f} seconds")

        # Assuming the response is a binary audio content
        async with aiofiles.open(output_file, "wb") as f:
            await f.write(response.content)
