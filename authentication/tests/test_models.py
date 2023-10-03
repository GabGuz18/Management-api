from django.test import TestCase
from django.contrib.auth import get_user_model


data = {
    'email':'test@example.com' ,
    'password':'testpass123'
}

class ModelTest(TestCase):
    def test_create_user_with_email(self):
        user = get_user_model().objects.create_user(
            email=data['email'],
            password=data['password']
        )

        self.assertEqual(user.email, data['email'])
        self.assertTrue(user.check_password(data['password']))
