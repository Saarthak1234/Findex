from fastapi import APIRouter, HTTPException, status
from app.models import YTVideoInfo
from app.models.requests import VideoInfoRequest
from app.core import get_logger
from app.youtube_utils import get_video_info

router = APIRouter()
logger = get_logger(__name__)


@router.post("/", response_model=YTVideoInfo)
async def video_info_handler(request: VideoInfoRequest):
    url = request.url
    logger.info(f"Received /video-info request for URL: {url}")

    try:
        video_info_obj = get_video_info(url)
        if not video_info_obj:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not fetch video information",
            )
        return video_info_obj

    except Exception as e:
        logger.error(f"Error in /video-info route: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
