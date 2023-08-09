# source.me
Uses AI to identify claims made in media.

## Use Case
John is recommended a youtube video by Jane, but he knows that the videos Jane watches are sometimes full of made up facts. Using source.me, John can generate a list of the claims which the video makes, and see what Google thinks the sources to those claims are.

## Setup

1. create `keys.env` file
   1. reach out to the code owner for instructions.
1. Setup Python Env
   1. run `python -m venv .venv` to create a virtual env
   1. run `source .venv/bin/activate` to source from it (note: if you are using vscode there should be a alert which pops up allowing you to source from it) 
   1. run `pip install -r src/requirements.txt`

## Testing
1. run `pip install -r test/requirements.txt`
1. run `pytest`


### Format code
Whenever you push code, there should be a linter check which runs.
If that check fails you should simply be able to run `black . && isort .` to resolve it. These commands automatically format your code.
