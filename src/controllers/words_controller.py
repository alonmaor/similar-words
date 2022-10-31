from service.words_service import get_similar
from database import async_session

from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1",
    tags=["Words"],
    responses={404: {"description": "Not found"}},
)


@router.get("/similar")
async def similar(word):
    async with async_session() as session:
        async with session.begin():
            similar_words, code = await get_similar(word, session)

    if similar_words is None:
        return {'error': 'Unable to get similar words'}, code

    return {"Words": similar_words}, code

