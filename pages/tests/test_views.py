from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTests(TestCase):
    """
    Tests for `HomeView` view
    """

    def test_with_get_request_to_home(self):
        """
        Test a GET request directed to the `pages:home` view
        """
        client = Client()
        url = reverse('pages:home')
        template = 'pages/home.html'
        response = client.get(url)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)
        self.assertEqual(response.context['page_name'], 'home')
        self.assertEqual(response.context['page_title'], 'Home')
