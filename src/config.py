from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from google import genai

from dotenv import load_dotenv; load_dotenv()
from os import getenv


BOT_TOKEN=getenv('BOT_TOKEN')
API_KEY=getenv('API_KEY')
AI_MODEL=getenv('AI_MODEL')
REQUEST_SIGNATURE=getenv('REQUEST_SIGNATURE', "")


BOT = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

CLIENT = genai.Client(api_key=API_KEY)


async def generate_response(text: str) -> str:
    try:
        response = CLIENT.models.generate_content(
            model=f"models/{AI_MODEL}",
            contents=f"{text}\n\n\n{REQUEST_SIGNATURE}"
        )
    except Exception as e:
        if "429" in str(e):
            return "e:429"
        return "e:*"

    return response.text