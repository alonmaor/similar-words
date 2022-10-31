
from service.words_service import input_words
from routes.api import router as api_router
from models import stats
from database import engine

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(api_router)
origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(stats.Base.metadata.drop_all)
        await conn.run_sync(stats.Base.metadata.create_all)

if __name__ == '__main__':
    word_filepath = '../words_clean.txt'
    input_words(word_filepath)
    print('Successfully created database with dictionary')

    uvicorn.run("main:app", host='127.0.0.1', port=8080, log_level="info", reload=True)
    print('Application has exited')