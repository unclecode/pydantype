# 🚀 PydanType: Pydantic to TypedDict Converter
[![GitHub stars](https://img.shields.io/github/stars/unclecode/PyDanType.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/unclecode/PyDanType/stargazers/)
![GitHub forks](https://img.shields.io/github/forks/unclecode/PyDanType.svg?style=social&label=Fork&maxAge=2592000)
![GitHub watchers](https://img.shields.io/github/watchers/unclecode/PyDanType.svg?style=social&label=Watch&maxAge=2592000)
![License](https://img.shields.io/github/license/unclecode/PyDanType)

Convert your Pydantic models to TypedDict with ease! 🎉

## 🌟 Motivation

Recently, Google Gemini introduced the ability to generate structured output, but here's the catch: unlike many environments that accept Pydantic models, they require TypeDict. It was tricky for me since I had a lot of Pydantic models in other projects, and I figured I wasn’t the only one. So, I created a simple utility that converts any Pydantic model to TypeDict, making it compatible with Gemini. Hopefully, this helps you as well! 💡

That's when this utility was born! Now you can:
1. Define your models in Pydantic (with all its validation goodness) 👍
2. Convert them to TypedDict when needed (for APIs like Gemini) 🔄
3. Enjoy the benefits of both! 🎊

## 🚀 Quick Start

Try it out instantly in our Colab notebook:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GAzvhDxhMbeBP48bXFWyrS5SoLjLxufc#scrollTo=welcome_markdown)

Install the package:

```bash
pip install pip install git+https://github.com/unclecode/pydantype.git
```

Use it in your code:

```python
from pydantic import BaseModel
from pydantype import convert

class MyModel(BaseModel):
    name: str
    age: int

MyTypedDict = convert(MyModel)
```

## 🌈 Gemini 1.5 Pro Example

Here's how you can use this utility with Google's Gemini 1.5 Pro:

```python
import google.generativeai as genai
from pydantic import BaseModel
from typing import List
from pydantype import convert

class Recipe(BaseModel):
    recipe_name: str
    ingredients: str

class RecipeList(BaseModel):
    recipes: List[Recipe]

RecipeListDict = convert(RecipeList)

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
from pydantype import convert

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

PersonDict = convert(Person)

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

Happy coding! 🎈🎊 