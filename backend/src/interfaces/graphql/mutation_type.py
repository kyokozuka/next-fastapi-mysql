from ariadne import MutationType
from src.interfaces.graphql.sample.new_sample import (
    resolve_new_sample,  # type: ignore
)
from src.interfaces.graphql.sample.update_sample import (
    resolve_update_sample,  # type: ignore
)
from src.interfaces.graphql.sample.delete_sample import (
    resolve_delete_sample,  # type: ignore
)


mutation = MutationType()
mutation.set_field("newSample", resolve_new_sample)  # type: ignore
mutation.set_field("updateSample", resolve_update_sample)  # type: ignore
mutation.set_field("deleteSample", resolve_delete_sample)  # type: ignore
