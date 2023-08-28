# from common.claims_model import List_Claims
import json

from claims.identify_claims_llm import identify_claims
from search.google_search import run_search


def main(file_path: str):
    claim_sources = {}

    with open(file_path, "r") as f:
        transcript = f.read()

    claim_pairs = identify_claims(transcript)
    for claim in claim_pairs.pairs:
        # print(claim)
        if claim.source == "none":
            search_results = run_search(claim.claim)
            claim_sources[claim.claim] = search_results
            # for result in search_results:
            #     print(result)
            #     print()
        else:
            claim_sources[claim.claim] = claim.source

    return claim_sources


claim_sources = main("test/truth/scishow_dna/transcript.txt")
print(json.dumps(claim_sources, indent=2))
