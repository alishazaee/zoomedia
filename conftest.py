import pytest
from rest_framework.test import APIClient
from zoomedia.userprofile.models import Profile
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from zoomedia.tests.factories import (
        UserFactory,
        ProfileFactory,
        FollowFactory,
        PostFactory,
        )


@pytest.fixture
def api_client(user1):
    # user = get_user_model().objects.create_user(username = "testy",email='testy_user@js.com', password='pass@1test')

    client = APIClient()
    refresh = RefreshToken.for_user(user1)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def user1():
    return UserFactory()

@pytest.fixture
def user2():
    return UserFactory()

@pytest.fixture
def follow1(user1 , user2):
    return FollowFactory(follower = user1, following = user2)

@pytest.fixture
def post1(user1):
    return PostFactory(author=user1)

@pytest.fixture
def post2(user2):
    return PostFactory(author=user2)


@pytest.fixture
def profile1(user1):
    return ProfileFactory(user=user1)

@pytest.fixture
def profile2(user2):
    return ProfileFactory(user=user2)