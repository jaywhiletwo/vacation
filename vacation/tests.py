from django.test import TestCase
from vacation.views import upload_image
from django.http import HttpRequest


class UploadTestCase(TestCase):
    def setUp(self):
        self.request = HttpRequest()

    def test_upload_picture(self):
        response = upload_image(self.request)
        self.assertEqual(response.status_code, 200)

