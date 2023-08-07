from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from drf_spectacular.utils import extend_schema
from zoomedia.api.mixins import ApiAuthMixin

from zoomedia.api.pagination import get_paginated_response, LimitOffsetPagination

from zoomedia.userprofile.selectors.profile import *
from zoomedia.userprofile.services.follow import *
from zoomedia.userprofile.services.profile import *

from rest_framework.permissions import IsAuthenticated
from ..serializers import *

class FollowApi( ApiAuthMixin,APIView):
    
    @extend_schema(request=None , responses=None)
    def delete(self, request ,username ):
        src_user=request.user
        try:
            delete_follow(src_user=src_user, target_username= username)
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)         
    @extend_schema(responses=get_profile_detail)
    def post(self , request,username):
        try:
            query = create_follow(
                src_user = request.user,
                target_username=username
                )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serilaizer = get_profile_detail(query)
        return Response(serilaizer.data)
     
        
        