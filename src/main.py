from fastapi import FastAPI
from controllers.user_controller import router as user_router
from services.user_service import UserService

app = FastAPI()
app.include_router(user_router)

user_service = UserService()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

