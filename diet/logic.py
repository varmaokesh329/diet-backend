def calculate_calories(weight, goal):
    if goal == "loss":
        return weight * 25
    elif goal == "gain":
        return weight * 35
    else:
        return weight * 30


def get_diet_plan(calories):
    if calories < 1800:
        return {
            "Breakfast": "Oats + Milk + Fruits",
            "Lunch": "2 Roti + Dal + Salad",
            "Dinner": "Soup + Boiled Eggs",
            "Snack": "Nuts"
        }
    elif calories < 2500:
        return {
            "Breakfast": "4 Eggs + Toast",
            "Lunch": "Rice + Chicken",
            "Dinner": "Chapati + Paneer",
            "Snack": "Banana"
        }
    else:
        return {
            "Breakfast": "6 Eggs + Oats",
            "Lunch": "Rice + Chicken + Dal",
            "Dinner": "Chapati + Chicken",
            "Snack": "Shake"
        }