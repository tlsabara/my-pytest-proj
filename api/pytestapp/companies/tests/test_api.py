from unittest import TestCase
from django.test import Client
from django.test import reverse

class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_empty_list(self):
        client = Client()
        companies_url = reverse('companies-list')


