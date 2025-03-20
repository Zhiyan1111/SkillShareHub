from django.shortcuts import render,redirect,HttpResponse
from app.models import User,Teacher,Course,Comment,Topic,CommentSecond
import time,json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

import os

import smtplib
from email.mime.text import MIMEText



def send(request,msg_to):
    code = str(random.randint(1000, 9999))
    with open("code.txt","w",encoding="utf-8")as f:
        f.write(code)




#user_login
def login_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user_objs = User.objects.filter(name=name).filter(password=password)
        print(user_objs)
        if user_objs.exists():
            user_obj = user_objs.first()
            print(user_obj)
            response = redirect("/home_user/all/")
            response.set_signed_cookie("name", name)
            request.session['islogin'] = True
            return response
        else:
            msg = "Login failed"
            return render(request, "login_user.html",{"msg":msg})
    return render(request, "login_user.html")


def reg_user(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pwd")

        # **Using get_or_create() method**
        user_obj, created = User.objects.get_or_create(name=name, defaults={"password": password})

        if not created: # Username already exists
            msg = "Username already taken"
            return render(request, "reg_user.html", {"msg": msg})  # 返回注册页面，并显示错误信息

        # **User created successfully**
        time.sleep(0.5)
        return redirect("/login_user/")

    return render(request, "reg_user.html")


# Create your views here.
def home_user(request,category):
    user_name = request.get_signed_cookie("name")
    if category == "all":  # all
        result = Course.objects.all()
        print(len(result))
    else:
        result = Course.objects.filter(category__icontains=category)
    # result = Course.objects.filter(category="1")
    paginator = Paginator(result, 12)

    if request.method == "GET":
        # Get the value of the page parameter after the url. The home page does not display the page parameter. The default value is 1
        page = request.GET.get('page')
        try:
            video_li = paginator.page(page)
        # todo: Be careful about catching exceptions
        except PageNotAnInteger:
            # If the requested number of pages is not an integer, return the first page.
            video_li = paginator.page(1)
        except InvalidPage:
            # If the requested page does not exist, redirect the page
            return HttpResponse('Unable to find the content of the page')
        except EmptyPage:
            # If the requested page number is not within the legal page range, return the last page of the result.
            video_li = paginator.page(paginator.num_pages)
    return render(request,"home_user.html",{"video_li":video_li,"user_name":user_name,"category":category})


#course_detail
def course_detail(request,id):
    user_name = request.get_signed_cookie("name")
    comments = Comment.objects.filter(c_course_id=id)
    obj = Course.objects.filter(id=id).first()

    return render(request,"course_detail.html",{"obj":obj,"user_name":user_name,"comments":comments})




def my_comment(request):
    if request.method == "POST":
        c_course_id = request.POST.get("course_id")
        c_content = request.POST.get("comment_text")

        c_username = request.get_signed_cookie("name")
        c_user_id = User.objects.filter(name=c_username).first().id
        print(c_user_id)

        Comment.objects.create(c_content=c_content,c_course_id=c_course_id,c_userputong_id=c_user_id,c_username=c_username)

    return redirect(f"/course_detail/{c_course_id}/")


def my_comment_guanli(request):

    if request.method == "POST":

        cs_course_id = request.POST.get("course_id2")
        cs_comment_id = request.POST.get("comment_id")
        cs_content = request.POST.get("comment_text2")

        cs_ug_name = request.get_signed_cookie("name")
        cs_user_id = Teacher.objects.filter(name=cs_ug_name).first().id
        print(cs_user_id)

        CommentSecond.objects.create(cs_content=cs_content, cs_teacher_id=cs_user_id, cs_username=cs_ug_name,
                                     cs_comment_id=cs_comment_id)

    return redirect(f"/teacher_course_detail/{cs_course_id}/")

import random

def home_test(request,id):
    user_name = request.get_signed_cookie("name")
    problem = random.choice(Topic.objects.filter(course_id=id))
    if request.method == "POST":
        result = ""

        answer = request.POST.get(str(problem.id))
        # print("problem.answer:",problem.answer)
        print(problem.id)
        print("answer:",answer)
        if answer == problem.answer:
            result = "Correct answer"
        else:
            result = "wrong answer"
        print(result)
        response = redirect(f"/test_detail/{problem.id}/")
        response.set_signed_cookie("result", result)
        return response
    return render(request,"home_test.html",{"user_name":user_name,"problem":problem,"id":id})




#Details page
def test_detail(request,id):
    user_name = request.get_signed_cookie("name")
    obj = Topic.objects.filter(id=id).first()
    result = request.get_signed_cookie("result")
    return render(request,"test_detail.html",{"topic":obj,"user_name":user_name,"result":result})




def logout(request):
    response = redirect("/login_user/")
    response.set_signed_cookie("name", "123")
    return response
# =============Teacher================

#Teacher login
def login_teacher(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user_objs = Teacher.objects.filter(name=name).filter(password=password)
        print(user_objs)
        if user_objs.exists():
            user_obj = user_objs.first()
            print(user_obj)
            response = redirect("/home_teacher/all/")
            response.set_signed_cookie("name", name)
            request.session['islogin'] = True
            return response
        else:
            msg = "Login failed"
            return render(request, "login_teacher.html",{"msg":msg})
    return render(request, "login_teacher.html")


# # register
# def reg_teacher(request):
#     msg = ""
#     if request.method == "POST":
#         name = request.POST.get("name")
#         password = request.POST.get("pwd")
#         # code = request.POST.get("code")
#         # with open("code.txt", "r", encoding="utf-8")as f2:
#         #     email_code = f2.read().strip()
#         # if code == email_code:
#         obj = Teacher.create(name, password)
#         obj.save()
#         time.sleep(0.5)
#         return redirect("/login_teacher/")
#         # else:
#         #     msg = "Verification code error"
#         # return render(request, "reg_teacher.html",{"msg":msg})
#     print("register")
#     return render(request, "reg_teacher.html")


# register
def reg_teacher(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pwd")

        # **Use get_or_create() to avoid duplication**
        teacher_obj, created = Teacher.objects.get_or_create(name=name, defaults={"password": password})

        if not created: # Username already exists
            msg = "Username already taken"
            return render(request, "reg_teacher.html", {"msg": msg})

        time.sleep(0.5)
        return redirect("/login_teacher/")

    return render(request, "reg_teacher.html")

# Create your views here.
def home_teacher(request,category):
    user_name = request.get_signed_cookie("name")
    if category == "all":  # all
        result = Course.objects.all()
        print(len(result))
    else:
        result = Course.objects.filter(category__icontains=category)
    paginator = Paginator(result, 12)

    if request.method == "GET":
        # Get the value of the page parameter after the url. The home page does not display the page parameter. The default value is 1
        page = request.GET.get('page')
        try:
            video_li = paginator.page(page)
        # todo: Be careful about catching exceptions
        except PageNotAnInteger:
            # If the requested number of pages is not an integer, return the first page.
            video_li = paginator.page(1)
        except InvalidPage:
            # If the requested page does not exist, redirect the page
            return HttpResponse('Unable to find the content of the page')
        except EmptyPage:
            # If the requested page number is not within the legal page range, return the last page of the result.
            video_li = paginator.page(paginator.num_pages)
    return render(request,"home_teacher.html",{"video_li":video_li,"user_name":user_name,"category":category})

from django.conf import settings
def uploat_course(request):
    BASE_DIR = settings.STATICFILES_DIRS[0]
    user_name = request.get_signed_cookie("name")
    if request.method == "POST":
        title = request.POST.get("title")
        introduce = request.POST.get("introduce")
        # cover_url = request.POST.get("cover_url")
        cover_obj = request.FILES.get('cover_url')
        print(cover_obj)
        f = open(BASE_DIR + '/course_img/' + cover_obj.name, 'wb')
        for chunk in cover_obj.chunks():
            f.write(chunk)
        f.close()

        # video_url = request.POST.get("video_url")
        video_obj = request.FILES.get('video_url')
        f2 = open(BASE_DIR + '/course_video/' + video_obj.name, 'wb')
        for chunk2 in video_obj.chunks():
            f2.write(chunk2)
        f2.close()
        category = request.POST.get("category")
        chapter = request.POST.get("chapter")

        obj = Course.create(title, introduce,'/course_img/' + cover_obj.name,'/course_video/' + video_obj.name,category,chapter)
        obj.save()
        time.sleep(0.5)
        return redirect("/home_teacher/all/")

    return render(request, "uploat_course.html",{"user_name":user_name})


def edit_course(request,id):
    user_name = request.get_signed_cookie("name")
    obj = Course.objects.filter(id=id).first()
    if request.method == "POST":
        title = request.POST.get('title')
        introduce = request.POST.get('introduce')
        cover_url = request.POST.get('cover_url')
        video_url = request.POST.get('video_url')
        category = request.POST.get('category')
        chapter = request.POST.get('chapter')

        obj.title = title
        obj.introduce = introduce
        obj.cover_url = cover_url
        obj.video_url = video_url
        obj.category = category
        obj.chapter = chapter

        obj.save()
        return redirect("/home_teacher/all/")
    return render(request, "edit_course.html", {"obj": obj, "user_name": user_name})



#course detail
def teacher_course_detail(request,id):
    user_name = request.get_signed_cookie("name")
    comments = Comment.objects.filter(c_course_id=id)
    obj = Course.objects.filter(id=id).first()

    return render(request,"teacher_course_detail.html",{"obj":obj,"user_name":user_name,"comments":comments})



def sub_examination(request, id):
    if request.method == "POST":
        user_name = request.get_signed_cookie("name")
        problem = request.POST.get("problem")
        answer1 = request.POST.get("answer1")
        answer2 = request.POST.get("answer2")
        answer3 = request.POST.get("answer3")
        answer4 = request.POST.get("answer4")
        answer = request.POST.get("answer")
        content = request.POST.get("content")

        # **删除已有的考试（如果存在相同的 course_id）**
        Topic.objects.filter(course_id=id).delete()

        # **插入新的考试**
        Topic.objects.create(
            problem=problem,
            answer1=answer1,
            answer2=answer2,
            answer3=answer3,
            answer4=answer4,
            answer=answer,
            content=content,
            course_id=id  # Make sure course_id still exists
        )

        return redirect("/home_teacher/all/")
    # return render(request, "sub_examination.html", {"user_name": user_name})


def logout_teacher(request):
    response = redirect("/login_teacher/")
    response.set_signed_cookie("name", "123")
    return response

def delete_course(request, id):
    user_name = request.get_signed_cookie("name") # Get the logged in user name
    obj = Course.objects.filter(id=id).first()  # Get the course object to be deleted

    if obj:
        # **Delete stored cover and video files**
        cover_path = os.path.join(settings.MEDIA_ROOT, obj.cover_url)  # Splice cover path
        video_path = os.path.join(settings.MEDIA_ROOT, obj.video_url)  # Stitching video path

        # **Delete cover file**
        if os.path.exists(cover_path):
            os.remove(cover_path)

        # **Delete video files**
        if os.path.exists(video_path):
            os.remove(video_path)

        # **Delete a course from the database**
        obj.delete()

    return redirect("/home_teacher/all/")  # Return to the course list page after deletion