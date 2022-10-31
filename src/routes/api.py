from fastapi import APIRouter
from controllers import stats_controller, words_controller

router = APIRouter()
router.include_router(stats_controller.router)
router.include_router(words_controller.router)