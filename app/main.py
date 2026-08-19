from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routers.mail import router

app = FastAPI(
    title="SMTP Mail API"
)

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:8080",
        "https://opulexfinancials.com/"
        ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.include_router(router)


@app.get("/")
def home():

    return {

        "message": "SMTP Mail API is running."
    }


    