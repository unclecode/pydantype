import unittest
from typing import List, Dict, Optional, Union, Any, ForwardRef
from pydantic import BaseModel, Field
from pydantype import convert

class Address(BaseModel):
    street: str
    city: str
    country: str

class Department(BaseModel):
    name: str
    code: int

class SimpleModel(BaseModel):
    integer_field: int
    string_field: str
    float_field: float
    boolean_field: bool

class NestedModel(BaseModel):
    name: str
    address: Address

class ListModel(BaseModel):
    items: List[str]

class DictModel(BaseModel):
    metadata: Dict[str, Any]

class OptionalModel(BaseModel):
    maybe_string: Optional[str]

class UnionModel(BaseModel):
    union_field: Union[int, str, float]

class ComplexModel(BaseModel):
    name: str
    age: int
    address: Address
    departments: List[Department]
    hobbies: List[str]
    metadata: Dict[str, Any]
    nickname: Optional[str]
    status: Union[str, int]

class GenericModel(BaseModel):
    generic_field: List[Union[int, str]]

class RecursiveModel(BaseModel):
    value: int
    next: Optional['RecursiveModel'] = None

RecursiveModel.model_rebuild()

class ModelWithField(BaseModel):
    constrained_string: str = Field(min_length=3, max_length=50)
    constrained_integer: int = Field(ge=0, le=100)

class TestConverter(unittest.TestCase):

    def assert_typeddict_field(self, typeddict, field_name, expected_type):
        self.assertIn(field_name, typeddict.__annotations__)
        self.assertEqual(typeddict.__annotations__[field_name], expected_type)

    def test_simple_model(self):
        SimpleDict = convert(SimpleModel)
        self.assert_typeddict_field(SimpleDict, 'integer_field', int)
        self.assert_typeddict_field(SimpleDict, 'string_field', str)
        self.assert_typeddict_field(SimpleDict, 'float_field', float)
        self.assert_typeddict_field(SimpleDict, 'boolean_field', bool)

    def test_nested_model(self):
        NestedDict = convert(NestedModel)
        self.assert_typeddict_field(NestedDict, 'name', str)
        self.assertTrue(isinstance(NestedDict.__annotations__['address'], type))

    def test_list_model(self):
        ListDict = convert(ListModel)
        self.assertTrue(ListDict.__annotations__['items'].__origin__ is list)
        self.assertEqual(ListDict.__annotations__['items'].__args__[0], str)

    def test_dict_model(self):
        DictDict = convert(DictModel)
        self.assertTrue(DictDict.__annotations__['metadata'].__origin__ is dict)
        self.assertEqual(DictDict.__annotations__['metadata'].__args__[0], str)
        self.assertEqual(DictDict.__annotations__['metadata'].__args__[1], Any)

    def test_optional_model(self):
        OptionalDict = convert(OptionalModel)
        self.assertTrue(OptionalDict.__annotations__['maybe_string'].__origin__ is Union)
        self.assertEqual(OptionalDict.__annotations__['maybe_string'].__args__, (str, type(None)))

    def test_union_model(self):
        UnionDict = convert(UnionModel)
        self.assertTrue(UnionDict.__annotations__['union_field'].__origin__ is Union)
        self.assertEqual(set(UnionDict.__annotations__['union_field'].__args__), {int, str, float})

    def test_complex_model(self):
        ComplexDict = convert(ComplexModel)
        self.assert_typeddict_field(ComplexDict, 'name', str)
        self.assert_typeddict_field(ComplexDict, 'age', int)
        self.assertTrue(isinstance(ComplexDict.__annotations__['address'], type))
        self.assertTrue(ComplexDict.__annotations__['departments'].__origin__ is list)
        self.assertTrue(isinstance(ComplexDict.__annotations__['departments'].__args__[0], type))
        self.assertTrue(ComplexDict.__annotations__['hobbies'].__origin__ is list)
        self.assertEqual(ComplexDict.__annotations__['hobbies'].__args__[0], str)
        self.assertTrue(ComplexDict.__annotations__['metadata'].__origin__ is dict)
        self.assertEqual(ComplexDict.__annotations__['metadata'].__args__[0], str)
        self.assertEqual(ComplexDict.__annotations__['metadata'].__args__[1], Any)
        self.assertTrue(ComplexDict.__annotations__['nickname'].__origin__ is Union)
        self.assertEqual(ComplexDict.__annotations__['nickname'].__args__, (str, type(None)))
        self.assertTrue(ComplexDict.__annotations__['status'].__origin__ is Union)
        self.assertEqual(set(ComplexDict.__annotations__['status'].__args__), {str, int})

    def test_generic_model(self):
        GenericDict = convert(GenericModel)
        self.assertTrue(GenericDict.__annotations__['generic_field'].__origin__ is list)
        self.assertTrue(GenericDict.__annotations__['generic_field'].__args__[0].__origin__ is Union)
        self.assertEqual(set(GenericDict.__annotations__['generic_field'].__args__[0].__args__), {int, str})

    def test_recursive_model(self):
        RecursiveDict = convert(RecursiveModel)
        self.assert_typeddict_field(RecursiveDict, 'value', int)
        self.assertTrue(RecursiveDict.__annotations__['next'].__origin__ is Union)
        
        # Check that the first argument is the RecursiveModelDict
        self.assertEqual(RecursiveDict.__annotations__['next'].__args__[0].__name__, 'RecursiveModelDict')
        
        # Check that the second argument is NoneType
        self.assertEqual(RecursiveDict.__annotations__['next'].__args__[1], type(None))

    def test_model_with_field(self):
        FieldDict = convert(ModelWithField)
        self.assert_typeddict_field(FieldDict, 'constrained_string', str)
        self.assert_typeddict_field(FieldDict, 'constrained_integer', int)

if __name__ == '__main__':
    unittest.main()