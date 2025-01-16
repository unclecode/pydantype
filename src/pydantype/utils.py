from typing import Any, Union, get_origin, get_args
from pydantic import BaseModel

def is_pydantic_model(type_: type) -> bool:
    return isinstance(type_, type) and not isinstance(type_, GenericAlias) and (issubclass(type_, BaseModel))

def is_optional(annotation: Any) -> bool:
    return get_origin(annotation) is Union and type(None) in get_args(annotation)
