from fastapi import FastAPI
from src.controllers.user_controller import user_router
from src.config.settings import Settings
# from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


app = FastAPI()
settings = Settings()

# Initialize repositories
# user_repository = UserRepository(settings.database_uri)

# Initialize services
# user_service = UserService(user_repository)

# Include routers
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

