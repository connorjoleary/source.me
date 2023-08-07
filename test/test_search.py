from search.google_search import *

class TestGoogleSearch:
    def test_happy_path(self):
        query = "eating silver turns you blue"
        res = run_search(query)
        assert len(res) == 3
