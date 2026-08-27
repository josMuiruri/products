from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Product

# Create your tests here.
class JournalModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='secert',
        )

        cls.product = Product.objects.create(
            author=cls.user,
            title='Test Title',
            slug='Test-Title',
            body='This is a test.',
        )


    def test_product_creation(self):
        self.assertEqual(self.product.author.username, 'testuser')
        self.assertEqual(self.product.title, 'Test Title')


    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Title')

    def test_default_status_is_draft(self):
        self.assertEqual(self.product.status, Product.Status.DRAFT)


    def test_image_is_optional(self):
        field = Product._meta.get_field('image')
        self.assertTrue(field.blank)


    def test_publish_date_is_set(self):
        self.assertIsNotNone(self.product.publish)


    def test_product_can_be_published(self):
        product = self.product
        product.status = Product.Status.PUBLISHED
        product.save()

        self.assertEqual(product.status, Product.Status.PUBLISHED)