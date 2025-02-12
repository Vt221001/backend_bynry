from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import ServiceRequest
from ..serializers import ServiceRequestSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_service_request(request):
    serializer = ServiceRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_service_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    serializer = ServiceRequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_service_request_status(request, pk):
    try:
        service_request = ServiceRequest.objects.get(pk=pk)
    except ServiceRequest.DoesNotExist:
        return Response({"error": "Service request not found"}, status=404)

    service_request.status = request.data.get('status', service_request.status)
    service_request.save()
    return Response({"message": "Status updated successfully"})
