from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import calculate_calories, calculate_macros, get_diet_plan
import json


# ✅ Home route (for testing)
def home(request):
    return HttpResponse("AI Diet Planner Backend is Running 🚀")


# ✅ Main API
@csrf_exempt
def ai_diet(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # 🔹 Get data from frontend
            weight = float(data.get("weight", 0))
            goal = data.get("goal", "maintain")
            selected_foods = data.get("foods", [])

            # 🔥 Calculate values
            calories = calculate_calories(weight, goal)
            protein, carbs, fiber = calculate_macros(calories, weight)

            # 🔥 Get diet plan with grams
            diet_plan = get_diet_plan(calories, selected_foods, goal)

            # 🔥 Convert to readable text
            plan_text = ""
            plan_text += f"Goal: {goal.upper()}\n"
            plan_text += f"Calories Needed: {int(calories)} kcal\n"
            plan_text += f"Protein: {protein} g\n"
            plan_text += f"Carbs: {carbs} g\n"
            plan_text += f"Fiber: {fiber} g\n\n"

            for meal, items in diet_plan.items():
                plan_text += f"{meal}:\n"
                for item in items:
                    plan_text += f"- {item}\n"
                plan_text += "\n"

            return JsonResponse({"diet": plan_text})

        except Exception as e:
            print("ERROR:", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Send POST request"}, status=400)