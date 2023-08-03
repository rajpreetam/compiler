from fastapi import APIRouter, HTTPException, status
from .schemas import SubmissionRequest, SubmissionResponse
from .services.submission_service import submission_service
from core.utils.custom_exceptions import CustomInternalServerException

router = APIRouter(
    prefix='/api/v1/compiler',
    tags=['compiler']
)


@router.get('/')
async def index():
    return {'data': 'Hello World'}


@router.post('/submission', response_model=SubmissionResponse)
async def submission_route(data: SubmissionRequest):
    try:
        return submission_service(data)
    except Exception as e:
        print(f'Error: {e}')
        raise CustomInternalServerException
