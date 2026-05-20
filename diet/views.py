from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import google.generativeai as genai


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def home(request):
    return HttpResponse("AI Diet Planner Backend is Running 🚀")


@csrf_exempt
def ai_diet(request):

    if request.method == "POST":

        try:

            data = json.loads(request.body)

            weight = data.get("weight")
            height = data.get("height")
            age = data.get("age")
            goal = data.get("goal")
            foods = data.get("foods")

            prompt = f"""
You are an expert AI nutritionist.

Create a personalized Indian diet plan.

USER DETAILS:
- Weight: {weight} kg
- Height: {height} cm
- Age: {age}
- Goal: {goal}
- Preferred Foods: {foods}

IMPORTANT RULES:
1. Calculate accurate calories.
2. Show protein, carbs, and fiber in grams.
3. Show exact quantity of each food item.
4. Use grams or pieces.
5. Avoid rice in breakfast and snacks.
6. Use only selected foods where possible.
7. Keep meals realistic and healthy.
8. Give Breakfast, Lunch, Dinner, and Snacks.
9. Format clearly.

Example format:

Goal: Weight Loss

Calories Needed: 1900 kcal

Protein: 120g
Carbs: 220g
Fiber: 30g

Breakfast:
- Oats - 60g
- Banana - 1 piece

Lunch:
- Rice - 150g
- Chicken - 120g

Dinner:
- Chapati - 2
- Paneer - 100g

Snacks:
- Nuts - 20g
"""

            response = model.generate_content(prompt)

            return JsonResponse({
                "diet": response.text
            })

        except Exception as e:

            return JsonResponse({
                "error": str(e)
            }, status=500)

    return JsonResponse({
        "message": "Send POST request"
    }, status=400)