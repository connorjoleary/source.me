import os

def get_env_var(name: str):
    env_var = os.getenv("OPENAI_API_KEY")
    if not env_var:
        raise ValueError(f"Env variable {name} not found.")
    return env_var