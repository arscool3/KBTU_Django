from fastapi import Depends, FastAPI
from controlers import user_routes, paper_routers, tag_routes, field_routes, favorite_routes, comment_routes
import models
from db import engine

app = FastAPI(debug=True)
models.Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(paper_routers.router)
app.include_router(tag_routes.router)
app.include_router(field_routes.router)
app.include_router(favorite_routes.router)
app.include_router(comment_routes.router)

