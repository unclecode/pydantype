from typing import Any, Union, get_origin, get_args
from pydantic import BaseModel

def is_pydantic_model(obj: Any) -> bool:
    return isinstance(obj, type) and issubclass(obj, BaseModel)

def is_optional(annotation: Any) -> bool:
    return get_origin(annotation) is Union and type(None) in get_args(annotation)