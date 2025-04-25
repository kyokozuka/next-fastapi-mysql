from ariadne.asgi import GraphQL
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.interfaces.graphql.schema import schema
from src.interfaces.graphql.context_value import context_value

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


graphql_app = GraphQL(schema=schema, debug=True, context_value=context_value)
app.mount("/graphql", graphql_app)
