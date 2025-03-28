from ariadne import (
    # MutationType,
    load_schema_from_path,  # type: ignore
    make_executable_schema,
)
from src.interfaces.graphql.query_type import query

from src.interfaces.graphql.mutation_type import mutation

type_defs = load_schema_from_path("schemas")
# mutation = MutationType()

schema = make_executable_schema(type_defs, query, mutation)
