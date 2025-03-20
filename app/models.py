from django.db import models


# Create your models here.
# User
class User(models.Model):
    name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)

    @classmethod
    def create(cls, name, password):
        return cls(name=name, password=password)

    class Meta:
        pass

    def __str__(self):
        return self.name


# Teacher
class Teacher(models.Model):
    name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)

    @classmethod
    def create(cls, name, password):
        return cls(name=name, password=password)

    class Meta:
        pass

    def __str__(self):
        return self.name


# Course
class Course(models.Model):
    title = models.TextField()  # title
    introduce = models.TextField()  # introduction
    cover_url = models.TextField()  # cover
    video_url = models.TextField()  # video address
    category = models.CharField(max_length=16)  # type
    chapter = models.CharField(max_length=16)  # chapter

    @classmethod
    def create(cls, title, introduce, cover_url, video_url, category, chapter):
        return cls(title=title, introduce=introduce, cover_url=cover_url, video_url=video_url, category=category,
                   chapter=chapter)

    class Meta:
        verbose_name = "Course"  # Change table name to English
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# Comment
class Comment(models.Model):
    c_content = models.TextField()
    c_username = models.CharField(max_length=16)
    c_userputong = models.ForeignKey(to="User", on_delete=models.CASCADE)
    c_course = models.ForeignKey(to="Course", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.c_content


# Second-level Comment
class CommentSecond(models.Model):
    cs_content = models.TextField()
    cs_username = models.CharField(max_length=16)
    cs_teacher = models.ForeignKey(to="Teacher", on_delete=models.CASCADE)
    cs_comment = models.ForeignKey(to="Comment", on_delete=models.CASCADE)  # Associate with first-level comment

    class Meta:
        pass

    def __str__(self):
        return self.cs_content


# Exam
class Topic(models.Model):
    problem = models.TextField()  # question
    answer1 = models.TextField()  # answer1
    answer2 = models.TextField()  # answer2
    answer3 = models.TextField()  # answer3
    answer4 = models.TextField()  # answer4
    answer = models.CharField(max_length=16)  # correct answer
    content = models.TextField()  # knowledge point
    course_id = models.TextField()  # course id

    @classmethod
    def create(cls, problem, answer1, answer2, answer3, answer4, answer, content, course_id):
        return cls(problem=problem, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer=answer,
                   content=content, course_id=course_id)

    class Meta:
        pass

    def __str__(self):
        return self.problem
