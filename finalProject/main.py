from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware


from app.routes.bus import router as bus_router
from app.routes.booking import router as booking_router
from app.routes.routes import router as routes_router
from app.routes.schedule import router as schedule_router
from app.routes.seats import router as seats_router
from app.routes.auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(auth_router, prefix="/user", tags=["users"])
app.include_router(bus_router, prefix="/bus", tags=["bus"])
app.include_router(booking_router, prefix="/booking", tags=["booking"])
app.include_router(routes_router, prefix="/routes", tags=["routes"])
app.include_router(schedule_router, prefix="/schedule", tags=["schedule"])
app.include_router(seats_router, prefix="/seat", tags=["seat"])
