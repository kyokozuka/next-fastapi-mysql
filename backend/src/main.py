from ariadne.asgi import GraphQL
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.interfaces.graphql.schema import schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    print("Hello World")


app.mount("/graphql", GraphQL(schema=schema, debug=True))
