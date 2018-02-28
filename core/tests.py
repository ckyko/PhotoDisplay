from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from base64 import b64encode

from .views import index, image


class IndexTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_index(self):
        request = self.factory.get(reverse('core:index'))
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_post_index(self):
        request = self.factory.post(reverse('core:index'))
        response = index(request)
        self.assertEqual(response.status_code, 405)


class ImageTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_image(self):
        request = self.factory.get(reverse('core:image'))
        response = image(request)
        self.assertEqual(response.status_code, 405)

    def test_post_without_image(self):
        request = self.factory.post(reverse('core:image'))
        response = image(request)
        self.assertEqual(response.status_code, 400)

    def test_post_with_image(self):

        # For getting the image string with base64 encode
        with open('core/image.jpeg', 'rb') as img:
            image_data = img.read()
            image_encode = b64encode(image_data)
            image_str = image_encode.decode('utf-8')

        with open('core/image.jpeg', 'rb') as img:
            request = self.factory.post(reverse('core:image'), {'image': img})

        response = image(request)
        page = response.content.decode('utf-8')
        self.assertIn(image_str, page)
        self.assertEqual(response.status_code, 200)

