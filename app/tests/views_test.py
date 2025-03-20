from django.test import TestCase, Client
from django.urls import reverse
from app.models import User, Teacher, Course, Comment, Topic, CommentSecond
from django.core.files.uploadedfile import SimpleUploadedFile

class UserViewsTest(TestCase):
    def setUp(self):
        """Initialize test data"""
        self.client = Client()
        self.user = User.objects.create(name="testuser", password="testpassword")
        self.teacher = Teacher.objects.create(name="testteacher", password="teacherpassword")
        self.course = Course.objects.create(
            title="Django Course",
            introduce="Learn Django",
            cover_url="test.jpg",
            video_url="test.mp4",
            category="Programming",
            chapter="1"
        )
        self.topic = Topic.objects.create(
            problem="What is Django?",
            answer1="A Python framework",
            answer2="A JavaScript library",
            answer3="A database",
            answer4="A CSS framework",
            answer="A Python framework",
            content="Django is a web framework",
            course_id=self.course.id
        )
        self.comment = Comment.objects.create(
            c_content="Great course!",
            c_username="testuser",
            c_userputong=self.user,
            c_course=self.course
        )

    #  Test user login
    def test_login_user(self):
        response = self.client.post(reverse('login_user'), {'name': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # 302 indicates successful redirection
        self.assertRedirects(response, "/home_user/all/")

    #  Test user registration
    def test_register_user(self):
        response = self.client.post(reverse('reg_user'), {'name': 'newuser', 'pwd': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # 302 indicates successful redirection
        self.assertTrue(User.objects.filter(name="newuser").exists())  # Ensure the user is successfully created

    #  Test user accessing course homepage
    def test_home_user(self):
        self.client.post(reverse('login_user'), {'name': 'testuser', 'password': 'testpassword'})
        response = self.client.get(reverse('home_user', args=['all']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Course")  # Ensure course title appears on the page

    #  Test course details page
    def test_course_detail(self):
        # Login first
        response = self.client.post(reverse('login_user'), {'name': 'testuser', 'password': 'testpassword'})

        # Set Django generated signed cookie
        self.client.cookies['name'] = response.client.cookies['name']

        # Access course details page
        response = self.client.get(reverse('course_detail', args=[self.course.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django")

    #  Test user commenting
    def test_my_comment(self):
        self.client.post(reverse('login_user'), {'name': 'testuser', 'password': 'testpassword'})
        response = self.client.post(reverse('my_comment'), {'course_id': self.course.id, 'comment_text': "Nice course!"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(c_content="Nice course!").exists())

    #  Test user logout
    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 302 indicates redirection to login page

    #  Test teacher registration
    def test_register_teacher(self):
        response = self.client.post(reverse('reg_teacher'), {'name': 'newteacher', 'pwd': 'teacherpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Teacher.objects.filter(name="newteacher").exists())

    #  Test teacher login
    def test_login_teacher(self):
        response = self.client.post(reverse('login_teacher'), {'name': 'testteacher', 'password': 'teacherpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/home_teacher/all/")

    #  Test teacher uploading a course
    def test_upload_course(self):
        # Login as teacher first
        self.client.post(reverse('login_teacher'), {'name': 'testteacher', 'password': 'teacherpassword'})

        # Create virtual files (simulate file upload)
        cover_file = SimpleUploadedFile("cover.jpg", b"file_content", content_type="image/jpeg")
        video_file = SimpleUploadedFile("video.mp4", b"video_content", content_type="video/mp4")

        # Send file upload request
        response = self.client.post(reverse('uploat_course'), {
            'title': 'New Django Course',
            'introduce': 'Django advanced',
            'cover_url': cover_file,  # Passing file object here
            'video_url': video_file,  # Passing file object here
            'category': 'Programming',
            'chapter': '2'
        })

        self.assertEqual(response.status_code, 302)  # 302 indicates successful redirection
        self.assertTrue(Course.objects.filter(title="New Django Course").exists())  # Ensure course is created

    #  Test teacher submitting an examination
    def test_submit_examination(self):
        self.client.post(reverse('login_teacher'), {'name': 'testteacher', 'password': 'teacherpassword'})
        response = self.client.post(reverse('sub_examination', args=[self.course.id]), {
            'problem': 'What is Python?',
            'answer1': 'A programming language',
            'answer2': 'A snake',
            'answer3': 'A web framework',
            'answer4': 'A text editor',
            'answer': 'A programming language',
            'content': 'Python is a general-purpose programming language'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(problem="What is Python?").exists())

    #  Test course deletion
    def test_delete_course(self):
        self.client.post(reverse('login_teacher'), {'name': 'testteacher', 'password': 'teacherpassword'})
        response = self.client.post(reverse('delete_course', args=[self.course.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Course.objects.filter(id=self.course.id).exists())

    #  Test teacher logout
    def test_logout_teacher(self):
        response = self.client.get(reverse('logout_teacher'))
        self.assertEqual(response.status_code, 302)  # 302 indicates successful redirection
