import os

from openai import OpenAI


def main():  # pragma: no cover
    os.environ["OPENAI_API_KEY"] = ""
    client = OpenAI()

    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": "Say this is a test"}]
    )
    print(completion.choices[0].message.content)
