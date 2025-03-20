import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.test import TestCase
from app.models import User, Teacher, Course, Comment, CommentSecond, Topic

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="testuser", password="testpassword")

    def test_create_user(self):
        """Test whether the user is successfully created"""
        self.assertEqual(self.user.name, "testuser")
        self.assertEqual(self.user.password, "testpassword")

    def test_user_str(self):
        """Test the string representation of the user"""
        self.assertEqual(str(self.user), "testuser")


class TeacherModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(name="testteacher", password="testpassword")

    def test_create_teacher(self):
        """Test whether the teacher is successfully created"""
        self.assertEqual(self.teacher.name, "testteacher")
        self.assertEqual(self.teacher.password, "testpassword")

    def test_teacher_str(self):
        """Test the string representation of the teacher"""
        self.assertEqual(str(self.teacher), "testteacher")


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Django Basics",
            introduce="Introduction to Django",
            cover_url="http://example.com/cover.jpg",
            video_url="http://example.com/video.mp4",
            category="Web Development",
            chapter="1"
        )

    def test_create_course(self):
        """Test whether the course is successfully created"""
        self.assertEqual(self.course.title, "Django Basics")
        self.assertEqual(self.course.introduce, "Introduction to Django")
        self.assertEqual(self.course.cover_url, "http://example.com/cover.jpg")
        self.assertEqual(self.course.video_url, "http://example.com/video.mp4")
        self.assertEqual(self.course.category, "Web Development")
        self.assertEqual(self.course.chapter, "1")

    def test_course_str(self):
        """Test the string representation of the course"""
        self.assertEqual(str(self.course), "Django Basics")


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="testuser", password="testpassword")
        self.course = Course.objects.create(
            title="Django Basics",
            introduce="Introduction to Django",
            cover_url="http://example.com/cover.jpg",
            video_url="http://example.com/video.mp4",
            category="Web Development",
            chapter="1"
        )
        self.comment = Comment.objects.create(
            c_content="This is a comment",
            c_username="testuser",
            c_userputong=self.user,
            c_course=self.course
        )

    def test_create_comment(self):
        """Test whether the comment is successfully created"""
        self.assertEqual(self.comment.c_content, "This is a comment")
        self.assertEqual(self.comment.c_username, "testuser")
        self.assertEqual(self.comment.c_userputong, self.user)
        self.assertEqual(self.comment.c_course, self.course)

    def test_comment_str(self):
        """Test the string representation of the comment"""
        self.assertEqual(str(self.comment), "This is a comment")


class CommentSecondModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(name="testteacher", password="testpassword")
        self.user = User.objects.create(name="testuser", password="testpassword")
        self.course = Course.objects.create(
            title="Django Basics",
            introduce="Introduction to Django",
            cover_url="http://example.com/cover.jpg",
            video_url="http://example.com/video.mp4",
            category="Web Development",
            chapter="1"
        )
        self.comment = Comment.objects.create(
            c_content="This is a comment",
            c_username="testuser",
            c_userputong=self.user,
            c_course=self.course
        )
        self.comment_second = CommentSecond.objects.create(
            cs_content="This is a second-level comment",
            cs_username="testteacher",
            cs_teacher=self.teacher,
            cs_comment=self.comment
        )

    def test_create_second_comment(self):
        """Test whether the second-level comment is successfully created"""
        self.assertEqual(self.comment_second.cs_content, "This is a second-level comment")
        self.assertEqual(self.comment_second.cs_username, "testteacher")
        self.assertEqual(self.comment_second.cs_teacher, self.teacher)
        self.assertEqual(self.comment_second.cs_comment, self.comment)

    def test_comment_second_str(self):
        """Test the string representation of the second-level comment"""
        self.assertEqual(str(self.comment_second), "This is a second-level comment")


class TopicModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(
            problem="What is Django?",
            answer1="A Python framework",
            answer2="A JavaScript library",
            answer3="A database",
            answer4="A CSS framework",
            answer="A Python framework",
            content="Django is a Python web framework.",
            course_id="1"
        )

    def test_create_topic(self):
        """Test whether the topic is successfully created"""
        self.assertEqual(self.topic.problem, "What is Django?")
        self.assertEqual(self.topic.answer1, "A Python framework")
        self.assertEqual(self.topic.answer2, "A JavaScript library")
        self.assertEqual(self.topic.answer3, "A database")
        self.assertEqual(self.topic.answer4, "A CSS framework")
        self.assertEqual(self.topic.answer, "A Python framework")
        self.assertEqual(self.topic.content, "Django is a Python web framework.")
        self.assertEqual(self.topic.course_id, "1")

    def test_topic_str(self):
        """Test the string representation of the topic"""
        self.assertEqual(str(self.topic), "What is Django?")
