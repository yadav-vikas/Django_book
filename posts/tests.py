from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):#driver function
        Post.objects.create(text = "test if it works")

    def test_text_content(self):#test function
        """This is different database than we created on previous where we stored data in
        this database has model name PostModelTest
        it contains only one data id=1---- text "test if it works"
        """
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,"test if it works")

class HomePageViewTest(TestCase):
    """Time for our next group of tests. The first test looked at the model but now we want evaluate
the homepage itself:
• does it actually exist and return a HTTP 200 response?
• does it use HomePageView as the view?
• does it use home.html as the template?

    Args:
        TestCase ([any]): [testcase]
    """
    def setUp(self):#driver function
        Post.objects.create(text="another test")

    def test_view_url_exits_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))#reverse is similar like redirect instead it just returns url as  string
        self.assertEqual(resp.status_code,200)
        
    def test_view_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
