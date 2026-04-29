def generate_ai_diet(data):
    weight = float(data["weight"])
    height = float(data["height"])
    age = int(data["age"])
    goal = data["goal"]
    foods = data["foods"]

    # Calories calculation
    calories = weight * 30

    if goal == "loss":
        calories -= 400
    elif goal == "gain":
        calories += 400

    protein = round(weight * 1.6)
    carbs = round((calories * 0.5) / 4)
    fiber = round(weight * 0.3)

    # Helper functions
    def has(food):
        return food in foods

    # Meal Plan
    breakfast = []
    lunch = []
    snacks = []
    dinner = []

    # BREAKFAST
    if has("Eggs"):
        breakfast.append("Eggs: 3")
    if has("Oats"):
        breakfast.append("Oats: 50g")
    if has("Banana"):
        breakfast.append("Banana: 1")

    # LUNCH
    if has("Chicken"):
        lunch.append("Chicken: 150g")
    if has("Rice"):
        lunch.append("Rice: 100g")
    if has("Chapati"):
        lunch.append("Chapati: 2")
    if has("Vegetables") or has("Broccoli") or has("Spinach"):
        lunch.append("Vegetables: 100g")

    # SNACKS
    if has("Apple"):
        snacks.append("Apple: 1")
    if has("Orange"):
        snacks.append("Orange: 1")
    if has("Nuts"):
        snacks.append("Nuts: 20g")

    # DINNER
    if has("Paneer"):
        dinner.append("Paneer: 150g")
    elif has("Chicken"):
        dinner.append("Chicken: 150g")

    if has("Carrot") or has("Spinach"):
        dinner.append("Vegetables: 100g")

    # Final output
    return f"""
🔥 DAILY TARGET
Calories: {calories} kcal
Protein: {protein} g
Carbs: {carbs} g
Fiber: {fiber} g

🍳 BREAKFAST
{chr(10).join(breakfast) if breakfast else "Custom selection needed"}

🍛 LUNCH
{chr(10).join(lunch) if lunch else "Custom selection needed"}

🥜 SNACKS
{chr(10).join(snacks) if snacks else "Custom selection needed"}

🍽️ DINNER
{chr(10).join(dinner) if dinner else "Custom selection needed"}
"""