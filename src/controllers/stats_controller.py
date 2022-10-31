from fastapi import APIRouter
from database import async_session

from service.stats_service import get_words_count, get_total_requests, get_avg_processing_time


router = APIRouter(
    prefix="/api/v1",
    tags=["Stats"],
    responses={404: {"description": "Not found"}},
)


@router.get("/stats")
async def stats():
    words_count, code = get_words_count()
    if words_count is None:
        return {'msg': 'Could not get the words count'}, code

    async with async_session() as session:
        async with session.begin():
            total_requests, code = await get_total_requests(session)

            if total_requests is None:
                return {'msg': 'Could not get total requests count'}, code

    async with async_session() as session:
        async with session.begin():
            avg_proc_time, code = await get_avg_processing_time(session)
            if avg_proc_time is None:
                return {'msg': 'Could not get average request processing time.'}, code

    return {'totalWords': words_count,
            'totalRequests':total_requests,
            'avgProcessingTimeNs':avg_proc_time}, code