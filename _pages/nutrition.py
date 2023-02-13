
import requests


def nutrition_info(ingredients):
    endpoint = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"
    headers = {
        "X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
        "X-RapidAPI-Key": "afae82f074msh729fe72b128081fp1f40f4jsn36bd559b1ce4"
    }
    params = {
        "ingr": ingredients
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response.json()

def ouput(nutrition_info):
    for nutrient in nutrition_info["totalNutrients"].values():
        print("{}: {} {}".format(nutrient["label"], nutrient["quantity"], nutrient["unit"]))

ingredients = input("Enter ingredients separated by commas: ")
nutrition_info = nutrition_info(ingredients)
print(ouput(nutrition_info))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

