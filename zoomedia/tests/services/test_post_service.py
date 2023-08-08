import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from zoomedia.blog.models import Post
from zoomedia.blog.services.post import create_post , delete_post
import json


@pytest.mark.django_db
def test_create_post(api_client, user1, follow1, profile1, post1 , post2):
    post = create_post(user=user1 , title="sample title" , description="sample description")
    assert post.title == "sample title"
    assert post.description == "sample description"
    assert post.author == user1

@pytest.mark.django_db
def test_delete_post(api_client, user1, follow1, profile1, post1 , post2):
    delete_post(user=user1 , slug = post1.slug)
    assert not Post.objects.filter(author=user1 , slug = post1.slug).exists()
