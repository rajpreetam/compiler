from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from compiler.routers import router as compiler_router
from accounts.routers import router as auth_router
from .utils.custom_exceptions import CustomInternalServerException
from .utils.custom_response import custom_response

app = FastAPI()


@app.exception_handler(CustomInternalServerException)
async def custom_internal_server_exception_handler(
    request: Request,
    exc: CustomInternalServerException
):
    return custom_response(
        success=False,
        status_code=exc.status_code,
        data=None,
        message=exc.detail
    )


origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(compiler_router)
app.include_router(auth_router)


@app.get('/', tags=['Root'])
async def index():
    return {
        'success': True,
        'status_code': status.HTTP_200_OK,
        'data': {
            'version': '1.0.2'
        },
        'message': 'Welcome to compiler api'
    }
