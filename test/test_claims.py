from claims.identify_claims_llm import *


class TestOpenAI:
    def test_happy_path(self):
        with open("test/truth/scishow_dna/transcript.txt", "r") as f:
            transcript = f.read()[:658]
        identify_claims(transcript)
