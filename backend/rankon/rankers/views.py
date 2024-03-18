from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from . import models, serializers


class RankerView(APIView, PageNumberPagination):
    def get(self, request):
        try:
            rankers = models.Ranker.objects.all().order_by('-vote')
            if rankers.exists():
                result = self.paginate_queryset(rankers, request, view=self)
                serializer = serializers.RankerSerializer(result, many=True)
                response = self.get_paginated_response(serializer.data)
                response.status_code = status.HTTP_200_OK
                return response

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RankerVoteAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            ranker_id = request.data.get('pk')
            if not ranker_id:
                ranker_id = kwargs.get('pk')

            ranker = models.Ranker.objects.get(user=ranker_id)
            ranker.vote += 1
            ranker.save()
            return Response({"message": "Vote incremented successfully"}, status=status.HTTP_200_OK)

        except models.Ranker.DoesNotExist:
            return Response({"error": "Ranker not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
