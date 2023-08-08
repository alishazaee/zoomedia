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

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

class ProfileApi(ApiAuthMixin,APIView):


    @extend_schema(responses=get_profile_detail_serializer , request=get_profile_detail_serializer)
    def put(self , request):
        serializer = get_profile_detail_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = update_profile(
                username = request.user.username,
                bio=serializer.validated_data.get('bio'),
                )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serilaizer = get_profile_detail_serializer(query)
        return Response(serilaizer.data)
     
        
         
    
    @extend_schema(responses=get_profile_detail_serializer)
    def get(self,request):
        user = request.user
        try:
            query = get_profile_detail(user=user)
        
        except Profile.DoesNotExist as ex:
            return Response(
                {"detail": "profile not found!  - " + str(ex)},
                status=status.HTTP_404_NOT_FOUND,
            )
          
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serilaizer = get_profile_detail_serializer(query)
        return Response(serilaizer.data)
