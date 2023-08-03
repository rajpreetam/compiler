from fastapi import FastAPI, status
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware
from compiler.routers import router as compiler_router
from .config import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


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


@app.get('/')
async def index():
    return {
        'success': True,
        'status_code': status.HTTP_200_OK,
        'data': {
            'version': '1.0.1'
        },
        'message': 'Welcome to compiler api'
    }
