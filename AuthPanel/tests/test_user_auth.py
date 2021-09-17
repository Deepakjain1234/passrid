from django.test import TestCase
from django.urls import reverse

class UserBaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('userLoginRegister')

        return super().setUp()

class UserRegisterTest(UserBaseTest):
    def test_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AuthPanel/user.html')
        