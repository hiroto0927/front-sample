from fastapi import FastAPI, Request
import time

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

