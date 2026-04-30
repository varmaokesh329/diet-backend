def calculate_calories(weight, goal):
    if goal == "loss":
        return weight * 25
    elif goal == "gain":
        return weight * 35
    else:
        return weight * 30


def calculate_macros(calories, weight):
    protein = weight * 1.6  # grams
    carbs = (calories * 0.5) / 4
    fiber = weight * 0.3
    return int(protein), int(carbs), int(fiber)


def get_food_grams(food, goal):
    # 🔹 Base portion sizes
    portions = {
        "Chicken": 150,
        "Eggs": 2,  # pieces
        "Paneer": 100,
        "Fish": 150,
        "Tofu": 120,
        "Soya Chunks": 50,

        "Rice": 200,
        "Oats": 60,
        "Chapati": 2,
        "Sweet Potato": 150,

        "Banana": 1,
        "Apple": 1,
        "Orange": 1,

        "Broccoli": 100,
        "Spinach": 100,
        "Carrot": 80,

        "Nuts": 30,
        "Seeds": 20,
        "Lentils": 100
    }

    qty = portions.get(food, 100)

    # 🔥 Adjust based on goal
    if goal == "loss":
        qty = int(qty * 0.8)
    elif goal == "gain":
        qty = int(qty * 1.2)

    return qty


def get_diet_plan(calories, selected_foods, goal):
    plan = {
        "Breakfast": [],
        "Lunch": [],
        "Dinner": [],
        "Snack": []
    }

    protein_foods = ["Chicken", "Eggs", "Paneer", "Fish", "Tofu", "Soya Chunks"]
    carb_foods = ["Rice", "Oats", "Chapati", "Sweet Potato"]
    fruit_foods = ["Banana", "Apple", "Orange"]
    veg_foods = ["Broccoli", "Spinach", "Carrot"]
    fiber_foods = ["Nuts", "Seeds", "Lentils"]

    # 🔹 Assign foods to meals
    for food in selected_foods:

        # ❌ Avoid rice in breakfast/snack
        if food == "Rice":
            plan["Lunch"].append(food)
            continue

        if food in protein_foods:
            plan["Lunch"].append(food)
            plan["Dinner"].append(food)

        elif food in carb_foods:
            plan["Breakfast"].append(food)
            plan["Lunch"].append(food)

        elif food in fruit_foods:
            plan["Breakfast"].append(food)
            plan["Snack"].append(food)

        elif food in veg_foods:
            plan["Lunch"].append(food)
            plan["Dinner"].append(food)

        elif food in fiber_foods:
            plan["Snack"].append(food)

    # 🔥 Default fallback (if user selects nothing)
    if not plan["Breakfast"]:
        plan["Breakfast"] = ["Oats"]

    if not plan["Lunch"]:
        plan["Lunch"] = ["Rice", "Lentils"]

    if not plan["Dinner"]:
        plan["Dinner"] = ["Chapati", "Vegetables"]

    if not plan["Snack"]:
        plan["Snack"] = ["Nuts"]

    # 🔥 Remove duplicates
    for meal in plan:
        plan[meal] = list(set(plan[meal]))

    # 🔥 Convert to grams format
    final_plan = {}

    for meal, foods in plan.items():
        final_plan[meal] = []

        for food in foods:
            qty = get_food_grams(food, goal)

            # Special units
            if food == "Eggs":
                final_plan[meal].append(f"{food} - {qty} pcs")
            elif food == "Chapati":
                final_plan[meal].append(f"{food} - {qty} pcs")
            elif food in ["Banana", "Apple", "Orange"]:
                final_plan[meal].append(f"{food} - {qty} pcs")
            else:
                final_plan[meal].append(f"{food} - {qty} g")

    return final_plan