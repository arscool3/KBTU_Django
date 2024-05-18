from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Route
from app.db import get_db
from sqlalchemy import Session
from app.routes.auth import get_current_user
from app.schemas import RouteResponse

router = APIRouter()


@router.get("/", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def get_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()
    return routes


@router.post("/", response_model=RouteResponse,
             dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def create_route(route: Route, db: Session = Depends(get_db)):
    db.add(route)
    db.commit()
    db.refresh(route)
    return route


@router.get("/{route_id}", response_model=RouteResponse,
            dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def get_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(Route).filter(Route.id == route_id).first()
    if not route:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")
    return route


@router.put("/{route_id}", response_model=RouteResponse,
            dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def update_route(route_id: int, route_data: Route, db: Session = Depends(get_db)):
    route = db.query(Route).filter(Route.id == route_id).first()
    if not route:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")

    route.update(route_data.dict(exclude_unset=True))
    db.commit()
    db.refresh(route)
    return route


@router.delete("/{route_id}",
               dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def delete_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(Route).filter(Route.id == route_id).first()
    if not route:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")

    # Optional: Check user permissions before deletion (e.g., is user an admin?)

    db.delete(route)
    db.commit()
    return {"message": "Route deleted successfully"}
