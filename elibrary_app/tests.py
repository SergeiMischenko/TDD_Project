from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.urls.base import resolve

from .models import Catalog
from .views import home


class ElibraryURLTests(SimpleTestCase):
    """Тест URL-адресов"""

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home)


class CatalogModelTests(TestCase):
    """Тест модели Catalog"""

    def setUp(self):
        self.book = Catalog(
            title="First Django Book",
            ISBN="978-1-60309-452-8",
            author="George Ray Charles",
            price="39.95",
            availability="True",
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalog)

    def test_str_representation(self):
        self.assertEqual(str(self.book), "First Django Book")

    def test_saving_and_retrieving_book(self):
        first_book = Catalog()
        first_book.title = "First Django Book"
        first_book.ISBN = "978-1-60309-452-8"
        first_book.author = "George Ray Charles"
        first_book.price = "39.95"
        first_book.availability = "True"
        first_book.save()

        second_book = Catalog()
        second_book.title = "Second Django Book"
        second_book.ISBN = "978-2-60309-459-7"
        second_book.author = "Gernot O'Brien"
        second_book.price = "29.95"
        second_book.availability = "False"
        second_book.save()

        saved_book = Catalog.objects.all()
        self.assertEqual(saved_book.count(), 2)

        first_saved_book = saved_book[0]
        second_saved_book = saved_book[1]
        self.assertEqual(first_saved_book.title, "First Django Book")
        self.assertEqual(second_saved_book.author, "Gernot O'Brien")
