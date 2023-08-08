from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema
from django.urls import reverse

from zoomedia.api.pagination import  get_paginated_response, LimitOffsetPagination, get_paginated_response_context
from rest_framework.pagination import PageNumberPagination

from ..models import Post 
from zoomedia.api.mixins import ApiAuthMixin
from ..serializer import postserializer
from ..selectors.post import *
from ..services.post import *
class PostApi(ApiAuthMixin , APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10
    
    @extend_schema(
        responses=postserializer,
        request=postserializer,
    )
    def post(self, request):
        serializer = postserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_post(
                user=request.user,
                description=serializer.validated_data.get("description"),
                title=serializer.validated_data.get("title"),
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(postserializer(query, context={"request":request}).data)


    
    
class PostDetailApi(ApiAuthMixin , APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10
    
    @extend_schema(
        responses=postserializer
    )
    def get(self, request , slug):
        try:
            query = post_detail(slug=slug, user=request.user)
        except Exception as ex:
            return Response(
                {"detail": " Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = postserializer(query)

        return Response(serializer.data) 
    

    def delete(self,request , slug):
        try:
             delete_post(slug=slug, user=request.user)
        except ObjectDoesNotExist as ex:
            return Response(
                {"detail": "Post Not Found - "},
                status=status.HTTP_400_BAD_REQUEST,
            )


        except Exception as ex:
            return Response(
                {"detail": " Error Deleting - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )


        return Response(status=status.HTTP_204_NO_CONTENT) 
