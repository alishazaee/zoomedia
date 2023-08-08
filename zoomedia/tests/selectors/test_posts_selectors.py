import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from zoomedia.blog.models import Post
from zoomedia.blog.selectors.post import post_list , post_detail
import json


@pytest.mark.django_db
def test_get_post_list(api_client, user1, follow1, profile1, post1 , post2):
    posts= post_list(user=user1)
    assert posts.count() == 2
    
@pytest.mark.django_db
def test_filter_author_post_list(api_client, user1, follow1, profile1, post1 , post2):
    posts= post_list( filters = {"author__in" : user1.username}, user=user1)
    assert posts.count() == 1

@pytest.mark.django_db
def test_returned_post_detail(api_client, user1, follow1, profile1, post1 , post2):
    post= post_detail(user=user1 , slug=post1.slug)
    assert post1.slug == post.slug

