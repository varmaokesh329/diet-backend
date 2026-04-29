from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_logic import generate_ai_diet

@csrf_exempt
def ai_diet(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            result = generate_ai_diet(data)

            return JsonResponse({"diet": result})

        except Exception as e:
            print("ERROR:", str(e))   # 👈 shows error in terminal
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Send POST request"}, status=400)