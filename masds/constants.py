import os
import dotenv
from langchain_openai import AzureChatOpenAI

from . import utils

dotenv.load_dotenv()


# Azure OpenAI Model
LLM = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_MODEL_NAME")
)


# DataBase
DB = {} if not os.path.exists("./.masds_cache/db.json") else utils.read_json_file("./.masds_cache/db.json")
