import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()  # Loads the .env file
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
