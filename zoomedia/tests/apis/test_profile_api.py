import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from zoomedia.blog.models import Post
import json


@pytest.mark.django_db
def test_profile_account_api_returning_200(api_client, user1, follow1, profile1, post1):
    url_ = reverse("api:profile:account" )
    response = api_client.get(url_, content_type="application/json")
    assert response.status_code == 200



