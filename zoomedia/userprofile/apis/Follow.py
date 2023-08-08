from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from drf_spectacular.utils import extend_schema
from zoomedia.api.mixins import ApiAuthMixin
from zoomedia.api.pagination import  get_paginated_response, LimitOffsetPagination, get_paginated_response_context

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
        except ObjectDoesNotExist as ex:
            return Response(
                {"detail": "Username not Found ! "},
                status=status.HTTP_400_BAD_REQUEST,
            )      
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)         
    @extend_schema(responses=get_profile_serializer)
    def post(self , request,username):
        try:
            query = create_follow(
                src_user = request.user,
                target_username=username
                )
        except ObjectDoesNotExist as ex:
            return Response(
                {"detail": "Username not Found ! "},
                status=status.HTTP_400_BAD_REQUEST,
            )      
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serilaizer = get_profile_serializer(query)
        return Response(serilaizer.data)

     
class FollowerApi( ApiAuthMixin,APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10
    class FilterUsernameSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=255 , required=False)
    class OutputUserSerializer(serializers.Serializer):
        follower = user_serializer()
        class Meta:
            model = Follow
            fields = ('follower',)

    
    @extend_schema(request=FilterUsernameSerializer , responses=OutputUserSerializer)
    def post(self, request  ):
        serializer =self.FilterUsernameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")

        if username is None:
            username=request.user
        try:
            query = get_follower(username=username)
        except ObjectDoesNotExist as ex :
            return Response(
                {"detail": "Username Not Found !"},
                status=status.HTTP_404_NOT_FOUND,
            )     
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serilaizer = self.OutputUserSerializer(query)
        return get_paginated_response_context(
            pagination_class=self.Pagination,
            serializer_class=self.OutputUserSerializer,
            queryset=query,
            request=request,
            view=self,
        )

     
class FollowingApi( ApiAuthMixin,APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 10
    
    class FilterUsernameSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=255 , required=False)
    class OutputUserserializer(serializers.Serializer):
        following = user_serializer()
        class Meta:
            model = Follow
            fields = ('following',)

    @extend_schema(request=FilterUsernameSerializer , responses=OutputUserserializer)
    def post(self, request ):
        serializer =self.FilterUsernameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        if username is None:
            username=request.user
        try:
            query = get_following(username=username)
        except ObjectDoesNotExist as ex :
            return Response(
                {"detail": "Username Not Found !"},
                status=status.HTTP_404_NOT_FOUND,
            )     
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serilaizer = self.OutputUserserializer(query)
        return get_paginated_response_context(
            pagination_class=self.Pagination,
            serializer_class=self.OutputUserserializer,
            queryset=query,
            request=request,
            view=self,
        )