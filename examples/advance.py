from typing import List, Dict, Optional, Union, Any
from pydantic import BaseModel, Field
from pydantype import conver

print("Welcome to the pydantype Converter Tutorial!")
print("This example will demonstrate various complex cases and how they're handled.")

print("\n1. Simple Model")
class SimpleModel(BaseModel):
    integer_field: int
    string_field: str
    float_field: float
    boolean_field: bool

SimpleDict = conver(SimpleModel)
print(f"SimpleDict annotations: {SimpleDict.__annotations__}")

print("\n2. Nested Model")
class Address(BaseModel):
    street: str
    city: str
    country: str

class NestedModel(BaseModel):
    name: str
    address: Address

NestedDict = conver(NestedModel)
print(f"NestedDict annotations: {NestedDict.__annotations__}")

print("\n3. List Model")
class ListModel(BaseModel):
    items: List[str]

ListDict = conver(ListModel)
print(f"ListDict annotations: {ListDict.__annotations__}")

print("\n4. Dict Model")
class DictModel(BaseModel):
    metadata: Dict[str, Any]

DictDict = conver(DictModel)
print(f"DictDict annotations: {DictDict.__annotations__}")

print("\n5. Optional Model")
class OptionalModel(BaseModel):
    maybe_string: Optional[str]

OptionalDict = conver(OptionalModel)
print(f"OptionalDict annotations: {OptionalDict.__annotations__}")

print("\n6. Union Model")
class UnionModel(BaseModel):
    union_field: Union[int, str, float]

UnionDict = conver(UnionModel)
print(f"UnionDict annotations: {UnionDict.__annotations__}")

print("\n7. Complex Model")
class Department(BaseModel):
    name: str
    code: int

class ComplexModel(BaseModel):
    name: str
    age: int
    address: Address
    departments: List[Department]
    hobbies: List[str]
    metadata: Dict[str, Any]
    nickname: Optional[str]
    status: Union[str, int]

ComplexDict = conver(ComplexModel)
print(f"ComplexDict annotations: {ComplexDict.__annotations__}")

print("\n8. Generic Model")
class GenericModel(BaseModel):
    generic_field: List[Union[int, str]]

GenericDict = conver(GenericModel)
print(f"GenericDict annotations: {GenericDict.__annotations__}")

print("\n9. Recursive Model")
class RecursiveModel(BaseModel):
    value: int
    next: Optional['RecursiveModel'] = None

RecursiveModel.model_rebuild()
RecursiveDict = conver(RecursiveModel)
print(f"RecursiveDict annotations: {RecursiveDict.__annotations__}")

print("\n10. Model with Field constraints")
class ModelWithField(BaseModel):
    constrained_string: str = Field(min_length=3, max_length=50)
    constrained_integer: int = Field(ge=0, le=100)

FieldDict = conver(ModelWithField)
print(f"FieldDict annotations: {FieldDict.__annotations__}")

print("\nTutorial complete! You've seen how pydantype handles various complex cases.")
print("Remember, the resulting TypedDict retains the structure of your Pydantic model,")
print("but doesn't include validation logic. Use it for type hinting and static analysis.")