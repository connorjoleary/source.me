import json

from claims.identify_claims_llm import *


class TestOpenAI:
    def test_happy_path(self):
        """
        Test to confirm what we would expect to get from
        the llm when used to identify claims. This
        involves making sure the list of model generated
        claims is not too long, not too short, and mostly
        match up with the claims in truth.
        """
        with open("test/truth/scishow_dna/transcript.txt", "r") as f:
            transcript = f.read()[:658].lower()
        with open("test/truth/scishow_dna/claims.json", "r") as f:
            claims_truth = json.load(f)
        claims_truth = claims_truth[:2]
        model_generated_claims = identify_claims(transcript)

        assert len(model_generated_claims) >= 2
        assert len(model_generated_claims) <= 4

        # a full outer join with a custom comparison operator
        extra_model_generated_claims = []
        for model_claim_obj in model_generated_claims:
            found_claim = False
            model_claim = model_claim_obj.claim.lower()
            assert model_claim in transcript
            for claim_truth in claims_truth:
                claim_truth = claim_truth.lower()
                if claim_truth in model_claim or model_claim in claim_truth:
                    found_claim = True
                    break
            if not found_claim:
                extra_model_generated_claims.append(model_claim)

        assert len(extra_model_generated_claims) <= 1
