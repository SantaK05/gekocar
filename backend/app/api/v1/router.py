from fastapi import APIRouter

from app.api.v1.endpoints import auth, contacts, bookings, admin

api_router = APIRouter()

api_router.include_router(auth.router,      prefix="/auth",      tags=["Auth"])
api_router.include_router(contacts.router,  prefix="/contacts",  tags=["Contacts"])
api_router.include_router(bookings.router,  prefix="/bookings",  tags=["Bookings"])
api_router.include_router(admin.router,     prefix="/admin",     tags=["Admin"])
