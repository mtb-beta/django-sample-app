from django.test import TestCase

from sample1.models import MyModel

class ViewTest(TestCase):
    def test_get_form_view(self):
        response = self.client.get('/')
        self.assertContains(response, 'form page')

    def test_get_post_view(self):
        response = self.client.get('/post/', {'name': 'test_name'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(MyModel.objects.filter(name='test_name'))

    def test_post_post_view(self):
        self.assertFalse(MyModel.objects.filter(name='test_name'))
        response = self.client.post('/post/', {'name': 'test_name'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/success/')
        self.assertTrue(MyModel.objects.filter(name='test_name'))

    def test_success_view(self):
        response = self.client.get('/success/')
        self.assertContains(response, '成功しました')
