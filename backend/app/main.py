from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title="Officina Meccanica API",
    description="Backend API per il sito vetrina dell'officina meccanica",
    version="1.0.0",
    # Swagger e ReDoc disabilitati in produzione
    docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,
)

# ========================
# CORS Middleware
# ========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================
# Router principale
# ========================
app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health_check():
    """Endpoint di health check — usato da Docker e Fly.io"""
    return {"status": "ok"}
