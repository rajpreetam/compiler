#gunicorn -w 4 -k uvicorn.workers.UvicornWorker core.main:app --reload
uvicorn core.main:app --reload