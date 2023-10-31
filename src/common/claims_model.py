from pydantic import BaseModel, Field


class Claim(BaseModel):
    claim: str = Field(
        description="an exact quote from the transcript in which the claim is made"
    )
    source: str = Field(
        description="the source provided for the claim or the word none if none are given"
    )

    def __hash__(self):
        return hash((self.claim, self.source))


class List_Claims(BaseModel):
    pairs: list[Claim]
