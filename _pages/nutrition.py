import requests

def get_nutrition_info(food_item):
    # RapidAPI endpoint and parameters
    endpoint = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"
    headers = {
        "X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
        "X-RapidAPI-Key": "2d79bbde22mshed34d34c65d8472p1365cejsn7594c6e54840"
    }
    params = {
        "ingr": food_item
    }
    
    # Send a GET request to the API
    response = requests.get(endpoint, headers=headers, params=params)
    
    # Return the JSON response
    return response.json()

# Example usage
food = "1 apple, 1 banana, 2 cup rice, 1 pound chicken, 10 eggs"
nutrition_info = get_nutrition_info(food)
print(nutrition_info)
