from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def ai_diet(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Simple test response (no OpenAI)
            return JsonResponse({
                "diet": "AI Diet API is working ✅"
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Send POST request"}, status=400)