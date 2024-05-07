from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Test
import json

@csrf_exempt
def put_endpoint(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        test = Test.objects.create(test=data['test'])
        return JsonResponse({'id': test.id, 'test': test.test})
    elif request.method == 'GET':
        # Handle GET request, maybe return some information about the endpoint
        return JsonResponse({'info': 'This endpoint is for creating new tests. Please use PUT method to create a test.'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def post_endpoint(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        test = Test.objects.create(test=data['test'])
        return JsonResponse({'id': test.id, 'test': test.test})
    elif request.method == 'GET':
        # Handle GET request, maybe return some information about the endpoint
        return JsonResponse({'info': 'This endpoint is for creating new tests. Please use POST method to create a test.'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_endpoint(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Test not found'}, status=404)

    if request.method == 'DELETE':
        test.delete()
        return JsonResponse({'message': 'Test deleted successfully'})
    elif request.method == 'GET':
        # Handle GET request, maybe return some information about the endpoint
        return JsonResponse({'info': 'This endpoint is for deleting tests. Please use DELETE method to delete a test.'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def get_endpoint(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        return JsonResponse({'id': test.id, 'test': test.test})
    except Test.DoesNotExist:
        return JsonResponse({'error': 'Test not found'}, status=404)
