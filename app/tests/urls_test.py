from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app import views

class URLTests(SimpleTestCase):
    """Test whether Django URL is correctly parsed into view function"""

    def test_login_user_url(self):
        url = reverse('login_user')
        self.assertEqual(resolve(url).func, views.login_user)

    def test_reg_user_url(self):
        url = reverse('reg_user')
        self.assertEqual(resolve(url).func, views.reg_user)

    def test_home_user_url(self):
        url = reverse('home_user', args=['all'])
        self.assertEqual(resolve(url).func, views.home_user)

    def test_course_detail_url(self):
        url = reverse('course_detail', args=[1])
        self.assertEqual(resolve(url).func, views.course_detail)

    def test_my_comment_url(self):
        url = reverse('my_comment')
        self.assertEqual(resolve(url).func, views.my_comment)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout)

    # ✅ 教师相关 URL 测试
    def test_login_teacher_url(self):
        url = reverse('login_teacher')
        self.assertEqual(resolve(url).func, views.login_teacher)

    def test_reg_teacher_url(self):
        url = reverse('reg_teacher')
        self.assertEqual(resolve(url).func, views.reg_teacher)

    def test_home_teacher_url(self):
        url = reverse('home_teacher', args=['all'])
        self.assertEqual(resolve(url).func, views.home_teacher)

    def test_upload_course_url(self):
        url = reverse('uploat_course')
        self.assertEqual(resolve(url).func, views.uploat_course)

    def test_edit_course_url(self):
        url = reverse('edit_course', args=[1])
        self.assertEqual(resolve(url).func, views.edit_course)

    def test_delete_course_url(self):
        url = reverse('delete_course', args=[1])
        self.assertEqual(resolve(url).func, views.delete_course)

    def test_logout_teacher_url(self):
        url = reverse('logout_teacher')
        self.assertEqual(resolve(url).func, views.logout_teacher)
