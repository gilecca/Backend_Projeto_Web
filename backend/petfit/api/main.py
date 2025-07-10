from fastapi import FastAPI
from fastapi.security import HTTPBearer
from petfit.api.routes import comment_route, post_route, user_route
from petfit.api.openapi_tags import openapi_tags
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="petfit API",
    description="API backend do petfit com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Lázaro Eduardo", "email": "lazaro@exemplo.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
    redirect_slashes=True,
)

origins = [
    "http://localhost:5173",  # Vite local
    "https://frontclean.vercel.app",  # Produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # lista de origens confiáveis
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique ["GET", "POST"]
    allow_headers=["*"],
)


@app.get("/")
def ola():
    return {"olá": "fastapi"}


app.include_router(user_route.router, prefix="/users", tags=["Users"])
app.include_router(post_route.router, prefix="/posts", tags=["Posts"])
app.include_router(comment_route.router, prefix="/comments", tags=["Comments"])