from pydantic import BaseModel
from typing import List, Optional
from pydantype import convert

class Address(BaseModel):
    street: str
    city: str
    country: str

class Person(BaseModel):
    name: str
    age: int
    address: Address
    hobbies: List[str]
    nickname: Optional[str]

PersonDict = convert(Person)

print("PersonDict structure:")
for field, type_hint in PersonDict.__annotations__.items():
    print(f"{field}: {type_hint}")

# Create a Person instance
person = Person(
    name="John Doe",
    age=30,
    address=Address(street="123 Main St", city="Anytown", country="USA"),
    hobbies=["reading", "swimming"],
    nickname="Johnny"
)

# Convert to dict and verify it matches PersonDict
person_dict = person.model_dump()
assert isinstance(person_dict, dict)
print("\nPerson instance convertted to dict successfully and matches PersonDict structure.")
print(person_dict)