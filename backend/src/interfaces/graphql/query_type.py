from ariadne import QueryType

from src.interfaces.graphql.sample.list_sample import resolve_list_sample  # type: ignore
from src.interfaces.graphql.sample.get_sample import resolve_get_sample  # type: ignore

query = QueryType()
query.set_field("listSample", resolve_list_sample)  # type: ignore
query.set_field("getSample", resolve_get_sample)  # type: ignore
