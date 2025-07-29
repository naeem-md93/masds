import os
import dotenv
from langchain_openai import AzureChatOpenAI


dotenv.load_dotenv()


# Azure OpenAI Model
LLM = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
)
