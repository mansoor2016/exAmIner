from collections.abc import Callable
from functools import cached_property

from attrs import frozen

TPrompt = str

# Can we put multiple questions into a prompt ?


@frozen
class QuestionPrompt(Callable):
    question: str
    answer: str
    mark_scheme: str

    def _generate_content(self) -> TPrompt:
        return (
            f"Mark the following answer to the question, given the provided"
            f" mark scheme.\n\n"
            f"Question: {self.question}.\n"
            f"Answer: {self.answer}.\n"
            f"Mark scheme: {self.mark_scheme}."
        )

    @cached_property
    def content(self) -> TPrompt:
        return self._generate_content()

    def __call__(self) -> TPrompt:
        return self.content

    def __str__(self) -> TPrompt:
        return self.content
