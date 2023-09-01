from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from common.claims_model import List_Claims, Claim
from common.utils import get_env_var


def setup_model() -> ChatOpenAI:
    load_dotenv("./keys.env")

    openai_api_key = get_env_var("OPENAI_API_KEY")
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

def deduplicate_claims(claims: list[Claim]) -> set[Claim]:
    return set(claims)

def identify_claims(transcript: str) -> set[Claim]:
    llm = setup_model()
    output_parser = PydanticOutputParser(pydantic_object=List_Claims)
    prompt = setup_prompts_and_messages(output_parser)
    _input = prompt.format_prompt(transcript=transcript)
    output = llm(_input.to_messages())
    claims = output_parser.parse(output.content).pairs

    claims_deduped = deduplicate_claims(claims)

    return claims_deduped
