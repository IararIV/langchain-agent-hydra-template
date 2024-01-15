import warnings
from pydantic import BaseModel, Field

from langchain_community.utils.openai_functions import (
    convert_pydantic_to_openai_function,
)
from langchain_core.prompts import ChatPromptTemplate


class Answer(BaseModel):
    task: str = Field(description="name of the task")
    reason: str = Field(description="reason why it was choosen")


class Router:
    def __init__(self, llm, prompt, parser, description) -> None:
        warnings.warn(
            "The 'Router' class is planned to be refactored to extend the 'Runnable' class from langchain core in the future.",
            FutureWarning
        )
        
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", prompt), 
            ("user", "{input}")]
        )
        self.parser = parser
        self.description = description
        
        self.openai_functions = [convert_pydantic_to_openai_function(Answer, description=description)]
    
    def invoke(self, input: dict) -> dict:
        return (self.prompt | self.llm.bind(functions=self.openai_functions) | self.parser).invoke(input)
