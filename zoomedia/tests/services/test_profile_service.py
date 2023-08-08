import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from zoomedia.blog.models import Post
from zoomedia.userprofile.services.profile import create_profile
import json


@pytest.mark.django_db
def test_create_profile(api_client, user1, follow1, profile1, post1 , post2):
    profile = create_profile(username=user1.username , bio = "something")
    assert profile.user == user1
    assert profile.bio == "something"

