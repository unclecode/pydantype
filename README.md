# 🚀 Pydantic to TypedDict Converter

Convert your Pydantic models to TypedDict with ease! 🎉

## 🌟 Motivation

Ever felt stuck between the awesome validation of Pydantic and the need for TypedDict? You're not alone! 🤝

When I saw Google's Gemini 1.5 Pro API requiring TypedDict for response schemas, I thought, "Why not have the best of both worlds?" 🤔💡

That's when this utility was born! Now you can:
1. Define your models in Pydantic (with all its validation goodness) 👍
2. Convert them to TypedDict when needed (for APIs like Gemini) 🔄
3. Enjoy the benefits of both! 🎊

## 🚀 Quick Start

Install the package:

```bash
pip install pydantic-to-typeddict
```

Use it in your code:

```python
from pydantic import BaseModel
from pydantic_to_typeddict import convert_pydantic_to_typeddict

class MyModel(BaseModel):
    name: str
    age: int

MyTypedDict = convert_pydantic_to_typeddict(MyModel)
```

## 🌈 Gemini 1.5 Pro Example

Here's how you can use this utility with Google's Gemini 1.5 Pro:

```python
import google.generativeai as genai
from pydantic import BaseModel
from typing import List
from pydantic_to_typeddict import convert_pydantic_to_typeddict

class Recipe(BaseModel):
    recipe_name: str
    ingredients: str

class RecipeList(BaseModel):
    recipes: List[Recipe]

RecipeListDict = convert_pydantic_to_typeddict(RecipeList)

model = genai.GenerativeModel('gemini-1.5-pro',
                              generation_config={
                                  "response_mime_type": "application/json",
                                  "response_schema": RecipeListDict
                              })

prompt = "List 3 popular cookie recipes"
response = model.generate_content(prompt)
print(response.text)
```

## 🎨 General Example

Here's a more general example showcasing various Pydantic features:

```python
from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_to_typeddict import convert_pydantic_to_typeddict

class Address(BaseModel):
    street: str
    city: str
    country: str = Field(default="Unknown")

class Person(BaseModel):
    name: str
    age: int
    address: Address
    hobbies: List[str] = []
    nickname: Optional[str] = None

PersonDict = convert_pydantic_to_typeddict(Person)

# PersonDict is now a TypedDict with the same structure as Person
```

## 🛠 Features

- Converts simple and complex Pydantic models 🏗
- Handles nested models, lists, and dictionaries 🔄
- Supports optional fields and unions 🤝
- Preserves type hints for better static analysis 🔍

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. 🙌

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding! 🎈🎊 Remember, with great power comes great responsibility... to write awesome, type-safe code! 💪💻