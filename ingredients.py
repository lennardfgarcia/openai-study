#!/usr/bin/env python3

"""
Module: ingredients.py
Created by: Lennard Garcia
Date: 2025-07-29
"""

from openai import OpenAI

# initialize the OpenAI client first
client = OpenAI()

# create the required variables
ingredients = []

# create a prompt that will accept ingredients until the user enters "X"
while True:
  ingredient = input("Type the ingredients that you want. Type 'x' when you're finished: ")
  if ingredient.lower() == 'x':
    break

  ingredients.append(ingredient)


# create a function that uses the model to process the ingredients
def recipeGeneratorMC(ingredients):

  messages = []

  for ingredient in ingredients:
    messages.append({"role":"user","content": ingredient})

  messages.append({"role":"user","content":"You are a Minecraft player, and you are wondering what can be build with the ingredients given"})

  response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = messages,
    max_tokens = 300,
    temperature = 0.9
  )
  return response.choices[0].message.content

# show the result
print(recipeGeneratorMC(ingredients))

