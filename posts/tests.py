from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="Message Board Tests")

    def test_model_content(self):
        self.assertEqual(self.post.text, "Message Board Tests")

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Message Board Tests")