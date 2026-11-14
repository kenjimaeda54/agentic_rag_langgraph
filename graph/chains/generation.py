import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter
from pydantic import SecretStr

load_dotenv()

APIKEY_OPENROUTER = os.environ.get("OPEN_ROUTER_API_KEY","")

llm = ChatOpenRouter(
     api_key=SecretStr(APIKEY_OPENROUTER),
     model="z-ai/glm-5.3-flash"
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "human",
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer the question. "
            "If you don't know the answer, just say that you don't know. "
            "Use three sentences maximum and keep the answer concise.\n"
            "Question: {question} \nContext: {context} \nAnswer:",
        )
    ]
)

generation_chain = prompt | llm

