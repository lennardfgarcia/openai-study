#!/usr/bin/env python3

"""
Module: ingredients.py
Created by: Lennard Garcia
Date: 2025-07-29
"""

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

  print(f"Ingredients: {ingredients}" )

# show the result
print(recipeGeneratorMC(ingredients))

