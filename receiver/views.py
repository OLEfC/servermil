from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse


general_data = ""

# Create your views here.
@csrf_exempt
def esp_data(request):
    global general_data
    if request.method == 'POST':
        data = json.loads(request.body)
        general_data = data
        # Process the data received from ESP32
        print(data)
        return JsonResponse({"message": "Data received successfully"})
    elif request.method == 'GET':
        print("general data", general_data)
        return HttpResponse(f"""
            <h1>Data:</h1>
            <pre>{json.dumps(general_data, indent=4)}</pre>
        """)


  