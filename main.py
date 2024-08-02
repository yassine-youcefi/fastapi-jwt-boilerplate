from fastapi import FastAPI
from user.views import user_views

app = FastAPI()

app.include_router(user_views.router, prefix="/user")


@app.get("/")
async def read_root():
    return {
        "Application": "FastAPI Boilerplate",
        "Purpose": "This is a boilerplate project for FastAPI with MongoDB.",
        "Author": "YAssine Youcefi",
        }
