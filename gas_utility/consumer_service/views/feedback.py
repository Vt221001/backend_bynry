from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import Feedback
from ..serializers import FeedbackSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_feedback(request):
    feedbacks = Feedback.objects.filter(user=request.user)
    serializer = FeedbackSerializer(feedbacks, many=True)
    return Response(serializer.data)
