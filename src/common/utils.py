import os


def get_env_var(name: str, required: bool = True):
    env_var = os.getenv("OPENAI_API_KEY")
    if not env_var and required:
        raise ValueError(f"Env variable {name} not found.")
    return env_var
