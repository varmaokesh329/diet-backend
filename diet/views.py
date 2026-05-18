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
Create a simple Indian diet plan.

Weight: {weight} kg
Height: {height} cm
Age: {age}
Goal: {goal}
Foods: {foods}

Show:
Calories
Protein
Carbs
Fiber
Breakfast
Lunch
Dinner
Snacks

Include grams and pieces.
Avoid rice in breakfast/snacks.
"""

            API_URL = "https://api-inference.huggingface.co/models/distilgpt2"

            headers = {
                "Authorization": f"Bearer {HF_TOKEN}"
            }

            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 120
                }
            }

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=30
            )

            result = response.json()

            print(result)

            if isinstance(result, list):

                generated_text = result[0].get(
                    "generated_text",
                    "No response generated."
                )

                return JsonResponse({
                    "diet": generated_text
                })

            elif "error" in result:

                return JsonResponse({
                    "diet": f"AI Error: {result['error']}"
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