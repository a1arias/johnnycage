from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from johnnycage.models import Page

def create_page(name, content):
    Page.objects.create(name=name, content=content)

class PageCrudTests(TestCase):
    def test_create_page(self):
        """
        Creating a page should cause no errors.
        """
        p = Page(name='home', content='Test page')
        p.save()
        self.assertEqual(p.pk, 1)

    def test_create_multiple_pages(self):
        """
        Creating 3 pages should result in 3 pages stored in the database.
        """
        create_page(name="test1", content="Test page 1")
        create_page(name="test2", content="Test page 2")
        create_page(name="test3", content="Test page 3")
        page_count = Page.objects.count()
        self.assertEqual(page_count, 3)

    def test_delete_page_with_multiple_pages(self):
        """
        Deleting a page should remove the correct page from the database.
        """
        create_page(name="test1", content="Test page 1")
        create_page(name="test2", content="Test page 2")
        create_page(name="test3", content="Test page 3")
        page3 = Page.objects.get(name="test3")
        page3.delete()
        pages = Page.objects.all()
        self.assertEqual(pages.count(), 2)
        for p in pages:
            self.assertNotEqual(p.name, "test3")

    def test_page_update_is_applied(self):
        """
        Updating a page should persist.
        """
        create_page(name="test1", content="Test page 1")
        p = Page.objects.get(name="test1")
        p.name = "test1updated"
        p.save()
        p = Page.objects.first()
        self.assertEqual(p.name, "test1updated")


class HomePageViewTests(TestCase):
    def test_index_view_is_rendered_with_home_page_content(self):
        create_page(name="home", content="test home page")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test home page")
