from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import os


HF_TOKEN = os.getenv("HF_TOKEN")


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

User Details:
- Weight: {weight} kg
- Height: {height} cm
- Age: {age}
- Goal: {goal}
- Preferred Foods: {foods}

Requirements:
1. Calculate total daily calories accurately.
2. Show protein, carbs, and fiber targets in grams.
3. Create Breakfast, Lunch, Dinner, and Snacks.
4. Show exact quantity of each food item in grams or pieces.
5. Avoid rice in breakfast and snacks.
6. Use only preferred foods where possible.
7. Keep the plan realistic and healthy.
8. Format the response clearly.

Example Format:

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

            response = requests.post(
                "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
                headers={
                    "Authorization": f"Bearer {HF_TOKEN}"
                },
                json={
                    "inputs": prompt
                },
                timeout=120
            )

            result = response.json()

            print(result)

            if isinstance(result, list):
                generated_text = result[0]["generated_text"]

                return JsonResponse({
                    "diet": generated_text
                })

            elif "error" in result:
                return JsonResponse({
                    "diet": f"AI Loading/Error: {result['error']}"
                })

            else:
                return JsonResponse({
                    "diet": "Unexpected AI response."
                })

        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=500)

    return JsonResponse({
        "message": "Send POST request"
    }, status=400)