from django.test import TestCase
from django.urls import reverse
from .models import BookData
import json

# Create your tests here.

class BookTest(TestCase):
    def setUp(self):
        BookData.objects.create(name="How to add", author="Wen", date="2007-08-09", price="10")
        BookData.objects.create(name="Who knows", author="Jack", date="2012-12-12", price="8.6")
        BookData.objects.create(name="Test3", author="Wen", date="2001-04-12", price="5.5")
        BookData.objects.create(name="Test4", author="Abc", date="2020-06-12", price="10")
        BookData.objects.create(name="Test4", author="Ben", date="2005-03-02", price="11.6")

    def testbooklist(self):
        response = self.client.get(reverse("book_list"))

        data = response.json()
        print(f"list:{data}")

    def testauthorfilter(self):
        self.client.get(reverse("author_name", kwargs={"author_name": "Wen"}))
        response = self.client.get(reverse("author_filter"))

        data = response.json()
        print(f"filter:{data}")

    def testdelname(self):
        self.client.get(reverse("del_book_name", kwargs={"d_name": "Test3"}))
        response = self.client.get(reverse("book_list"))

        data = response.json()
        print(f"del_n:{data}")

    def testdelauthor(self):
        self.client.get(reverse("del_book_author", kwargs={"d_author": "Jack"}))
        response = self.client.get(reverse("book_list"))

        data = response.json()
        print(f"del_a:{data}")

    def testdelname_m(self):
        self.client.get(reverse("del_book_name_m", kwargs={"d_name": "Test4", "d_num": 1}))
        response = self.client.get(reverse("book_list"))

        data = response.json()
        print(f"del_n_m:{data}")

    def testdelauthor_m(self):
        self.client.get(reverse("del_book_author_m", kwargs={"d_author": "Wen", "d_num": 2}))
        response = self.client.get(reverse("book_list"))

        data = response.json()
        print(f"del_a_m:{data}")

    def testupdatebook(self):
        self.client.get(reverse("update_book_data", kwargs={"u_id": 1, "u_name": "How to add more", "u_author": "Wen", "u_date": "2007-08-09", "u_price": "15.99"}))
        response = self.client.get(reverse("book_list"))

        data = response.json()
        print(f"update:{data}")