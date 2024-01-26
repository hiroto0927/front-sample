from fastapi import FastAPI, Request, APIRouter
import time
from app.users.router import router as users_router

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(str(process_time))
    return response


@app.get("/")
def root():
    return {"message": "Hello World"}


router = APIRouter(prefix="/api")

router.include_router(users_router)

app.include_router(router)
