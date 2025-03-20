from django.db import migrations

def add_initial_data(apps, schema_editor):
    Teacher = apps.get_model("app", "Teacher")
    User = apps.get_model("app", "User")
    Course = apps.get_model("app", "Course")

    Teacher.objects.create(name="root", password="123")
    User.objects.create(name="aaa", password="123")
    Course.objects.create(title="English Learning",
                          introduce="Learn English well and revitalize China",
                          cover_url="/course_img/aaa.png",
                          video_url="/course_video/d3682232152e0aa2392f91d4f5623ae5.mp4",
                          category="English",
                          chapter="Chapter 1")

class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
