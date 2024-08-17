from __future__ import annotations
from typing import get_args, get_origin, Any, Union, List, Dict, Optional, Type, ForwardRef
from typing_extensions import TypedDict
from pydantic import BaseModel

from .utils import is_pydantic_model, is_optional

def convert_type(annotation: Any, processed_models: set = None) -> Any:
    if processed_models is None:
        processed_models = set()

    if isinstance(annotation, ForwardRef):
        return annotation.__forward_arg__

    if is_pydantic_model(annotation):
        if annotation.__name__ in processed_models:
            return f"ForwardRef('{annotation.__name__}Dict')"
        processed_models.add(annotation.__name__)
        return conver(annotation, processed_models)
    
    origin = get_origin(annotation)
    if origin is None:
        return annotation
    
    args = get_args(annotation)
    
    if origin is Union:
        non_none_args = [arg for arg in args if arg is not type(None)]
        if len(non_none_args) == 1:
            return Optional[convert_type(non_none_args[0], processed_models)]
        return Union[tuple(convert_type(arg, processed_models) for arg in non_none_args)]
    
    if origin in (list, List):
        item_type = convert_type(args[0], processed_models) if args else Any
        return List[item_type]
    
    if origin in (dict, Dict):
        key_type = convert_type(args[0], processed_models) if len(args) > 0 else Any
        value_type = convert_type(args[1], processed_models) if len(args) > 1 else Any
        return Dict[key_type, value_type]
    
    if hasattr(origin, '__origin__'):  # Handle subscripted generics
        converted_args = tuple(convert_type(arg, processed_models) for arg in args)
        return origin[converted_args]
    
    return annotation

def conver(model: Type[BaseModel], processed_models: set = None) -> Type[TypedDict]:
    if not is_pydantic_model(model):
        raise ValueError(f"Expected a Pydantic model, got {type(model)}")

    if processed_models is None:
        processed_models = set()
    
    fields = {}
    for name, field in model.model_fields.items():
        converted_type = convert_type(field.annotation, processed_models)
        fields[name] = converted_type
    
    return TypedDict(f"{model.__name__}Dict", fields)