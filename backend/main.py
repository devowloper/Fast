```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import estimator_router, upload_router

app = FastAPI()

app.include_router(upload_router.router)
app.include_router(estimator_router.router)

origins = [
    "http://localhost:5000",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```