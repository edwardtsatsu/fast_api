from fastapi import FastAPI
from src.controllers.user_controller import user_router
from src.config.db import get_db
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService

app = FastAPI()

# Initialize database
db = get_db()
user_repository = UserRepository(db)

# Initialize services
user_service = UserService(user_repository)

# Include routers
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

