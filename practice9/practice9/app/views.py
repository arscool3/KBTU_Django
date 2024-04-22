from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

from .models import Test

@csrf_exempt
@require_http_methods(["PUT"])
def put_endpoint(request):
    # Example PUT logic
    data = request.POST  # Assuming form data is sent
    test = data.get('test')
    Test.objects.create(test=test)
    return JsonResponse({"message": "PUT request received"})

@csrf_exempt
@require_http_methods(["POST"])
def post_endpoint(request):
    # Example POST logic
    data = request.POST  # Assuming form data is sent
    test = data.get('test')
    Test.objects.create(test=test)
    return JsonResponse({"message": "POST request received"})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_endpoint(request):
    # Example DELETE logic
    try:
        test_id = request.GET.get('id')
        test = Test.objects.get(pk=test_id)
        test.delete()
        return JsonResponse({"message": "DELETE request received"})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Test object does not exist"}, status=404)

@csrf_exempt
@require_http_methods(["GET"])
def get_endpoint(request):
    # Example GET logic
    tests = Test.objects.all()
    test_data = [{"id": test.id, "test": test.test} for test in tests]
    return JsonResponse({"tests": test_data})
