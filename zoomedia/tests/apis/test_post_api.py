import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from zoomedia.blog.models import Post
import json


@pytest.mark.django_db
def test_feed_api(api_client, user1, follow1, profile1, post1):
    url_ = reverse("api:blog:feed" )

    response = api_client.get(url_, content_type="application/json")
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data.get('limit') == 10 
