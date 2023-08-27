import os
from typing import List

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from pydantic import BaseModel, Field


class Claim(BaseModel):
    claim: str = Field(
        description="an exact quote from the transcript in which the claim is made"
    )
    source: str = Field(
        description="the source provided for the claim or the word none if none are given"
    )


class List_Claims(BaseModel):
    pairs: List[Claim]


def setup_model() -> ChatOpenAI:
    load_dotenv("./keys.env")

    openai_api_key = os.getenv("OPENAI_API_KEY")
    return ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-4")


def setup_prompts_and_messages(output_parser):
    system_message = SystemMessagePromptTemplate.from_template(
        "You are a helpful assistant that, when given a video transcript, identifies the claims made and any sources provided"
    )
    human_message = HumanMessagePromptTemplate.from_template(
        """
    {transcript}

    {format_instructions}
    """
    )
    format_instructions = output_parser.get_format_instructions()

    prompt = ChatPromptTemplate(
        messages=[system_message, human_message],
        input_variables=["transcript"],
        partial_variables={"format_instructions": format_instructions},
    )
    return prompt


def identify_claims(transcript: str) -> List_Claims:
    llm = setup_model()
    output_parser = PydanticOutputParser(pydantic_object=List_Claims)
    prompt = setup_prompts_and_messages(output_parser)
    _input = prompt.format_prompt(transcript=transcript)
    output = llm(_input.to_messages())
    return output_parser.parse(output.content)
