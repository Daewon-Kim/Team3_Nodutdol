# Team3_Nodutdol

# install
%pip install -U openai

# install AzuerOpenAI and packages
from openai import AzureOpenAI

from config_azure import (
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY
)

client = AzureOpenAI(
  azure_endpoint = AZURE_OPENAI_ENDPOINT,
  api_key = AZURE_OPENAI_KEY,  
  api_version = AZURE_OPENAI_API_VERSION
)