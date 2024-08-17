import os

import google.generativeai as genai
import typing_extensions as typing
import google.generativeai as genai
from pydantic import BaseModel
from typing import List
from pydantype import convert_pydantype
from dotenv import load_dotenv
load_dotenv()

print("Example: Using TypedDict and Pydantic with Google Generative AI (Gemini 1.5 Pro)")

# Part 1: Using TypedDict directly
print("\nPart 1: Using TypedDict directly")

class Recipe(typing.TypedDict):
    recipe_name: str
    ingredients: str

# Set up the model with TypedDict schema
model_typeddict = genai.GenerativeModel('gemini-1.5-pro',
                                        generation_config={
                                            "response_mime_type": "application/json",
                                            "response_schema": List[Recipe]
                                        })

prompt = "List 3 popular cookie recipes"

response_typeddict = model_typeddict.generate_content(prompt)
print("Response using TypedDict:")
print(response_typeddict.text)

# Part 2: Using Pydantic and converting to TypedDict
print("\nPart 2: Using Pydantic and converting to TypedDict")

class RecipePydantic(BaseModel):
    recipe_name: str
    ingredients: str

class RecipeList(BaseModel):
    recipes: List[RecipePydantic]

# Convert Pydantic models to TypedDict
RecipeDict = convert_pydantype(RecipePydantic)
RecipeListDict = convert_pydantype(RecipeList)

# Set up the model with converted Pydantic schema
model_pydantic = genai.GenerativeModel('gemini-1.5-pro',
                                       generation_config={
                                           "response_mime_type": "application/json",
                                           "response_schema": RecipeListDict
                                       })

response_pydantic = model_pydantic.generate_content(prompt)
print("Response using converted Pydantic model:")
print(response_pydantic.text)

print("\nComparison:")
print("As you can see, both approaches produce the same structure of response.")
print("The advantage of using Pydantic is that you can define more complex models")
print("with validation, default values, and other features, and then convert them")
print("to TypedDict for use with APIs that require it, like Gemini 1.5 Pro.")