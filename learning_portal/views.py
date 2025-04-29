import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact_Us,Create_Account,Courses,Categories,Languages,Quiz,Certificate,My_Learning
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages


def home_view(request):
    template_name = 'learning_portal/home.html'
    members_count = Create_Account.objects.count()
    courses_count = Courses.objects.count()
    categories_count = Categories.objects.count()
    language_count = Languages.objects.count()

    context = {
        'members_count': members_count,
        'courses_count':courses_count,
        'categories_count':categories_count,
        'language_count':language_count
    }

    return render(request,template_name,context)

def about_view(request):
    template_name = 'learning_portal/about.html'
    context = {}
    return render(request,template_name,context)

def contact_us_view(request):
    template_name = 'learning_portal/contact_us.html'

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        contact_us = Contact_Us(name=name, email=email, number=number, message=message)
        contact_us.save()
        return redirect('home_view_urls')

    context = {}
    return render(request,template_name,context)

def login_view(request):
    template_name = 'learning_portal/login.html'
'''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Create_Account.objects.get(email=email)

            if check_password(password,user.password):
                request.session['user_id'] = user.id
                return redirect('app_home_view_urls')

            else:
                messages.error(request, "Your password is incorrect.")
                return redirect('login_view_urls')

        except Create_Account.DoesNotExist:
            messages.error(request, "Your email id is incorrect.")
            return redirect('login_view_urls')
'''
    context = {}
    return render(request,template_name,context)

def create_account_view(request):
    template_name = 'learning_portal/create_acc.html'

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        password = request.POST.get('password')

        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        photo_url = fs.url(filename)

        contact_us = Create_Account(photo=photo, name=name, email=email, number=number, dob=dob, gender=gender, password=password)
        contact_us.save()
        return redirect('login_view_urls')

    context = {}
    return render(request,template_name,context)


def app_home_view(request):
    template_name = 'learning_application/home.html'
    members_count = Create_Account.objects.count()
    courses_count = Courses.objects.count()
    categories_count = Categories.objects.count()
    language_count = Languages.objects.count()

    categories = Categories.objects.all()
    courses = Courses.objects.all()

    for category in categories:
        category.courses_count = Courses.objects.filter(category_id=category.id).count()

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
            context = {
                'user': user,
                'members_count': members_count,
                'courses_count': courses_count,
                'categories_count': categories_count,
                'language_count': language_count,
                'categories': categories,
                'courses':courses
            }
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')
    return render(request, template_name, context)


def app_logout_view(request):
    request.session.flush()
    return redirect('home_view_urls')


def app_about_view(request):
    template_name = 'learning_application/about.html'

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
            context = {'user': user}
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')
    return render(request, template_name, context)


def app_contact_us_view(request):
    template_name = 'learning_application/contact_us.html'

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        contact_us = Contact_Us(name=name, email=email, number=number, message=message)
        contact_us.save()
        return redirect('home_view_urls')

    context = {'user': user}
    return render(request,template_name,context)


def app_courses_details_view(request, course_id):
    template_name = 'learning_application/courses_details.html'
    course = get_object_or_404(Courses, id=course_id)

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
            context = {
                'course': course,
                'user': user
            }
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    return render(request, template_name, context)


def app_course_view(request, course_id):
    template_name = 'learning_application/course.html'
    course = get_object_or_404(Courses, id=course_id)

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)

            My_Learning.objects.get_or_create(
                name=user.name,
                course=course
            )

            context = {
                'course': course,
                'user': user
            }
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    return render(request, template_name, context)


def quiz_view(request, course_id):
    template_name = 'quiz_application/quiz.html'
    course = get_object_or_404(Courses, id=course_id)

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    questions = Quiz.objects.filter(course_id=course_id)

    if request.method == "POST":
        score = 0
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_answer:
                score += 1

        request.session['score'] = score
        return redirect('quiz_result_view_urls', course_id=course_id)

    context = {
        'course': course,
        'user': user,
        'questions': questions
    }

    return render(request, template_name, context)


def quiz_result_view(request, course_id):
    template_name= 'quiz_application/quiz_result.html'
    course = get_object_or_404(Courses, id=course_id)
    score = request.session.get('score', 0)
    status = "Pass" if score > 13 else "Fail"

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
            context = {
                'course': course,
                'user': user,
                'score': score,
                'status': status,
            }
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    return render(request, template_name, context)


def certificate_view(request, course_id):
    template_name = 'quiz_application/certificate.html'

    course = get_object_or_404(Courses, id=course_id)
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('home_view_urls')

    user = get_object_or_404(Create_Account, id=user_id)

    if request.method == "POST":
        name = request.POST.get("name")
        course_name = request.POST.get("course_name")
        certificate_data = request.POST.get("certificate")

        format, imgstr = certificate_data.split(';base64,')
        ext = format.split('/')[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name=f"{ user.name }_{ course.title }_certificate.{ext}")

        Certificate.objects.create(
            name=name,
            course_name=course_name,
            certificate=image_data
        )

        return JsonResponse({"status": "success"})

    context = {
        "user": user,
        "course": course
    }

    return render(request, template_name, context)


def my_learning_view(request):
    template_name = 'learning_application/my_learning.html'
    user_id = request.session.get('user_id')

    try:
        user = Create_Account.objects.get(id=user_id)
        user_learning_records = My_Learning.objects.filter(name=user.name)

        courses = Courses.objects.filter(id__in=user_learning_records.values_list('course', flat=True))

        context = {
            'user': user,
            'courses': courses
        }
        return render(request, template_name, context)

    except Create_Account.DoesNotExist:
        return redirect('home_view_urls')



def delete_course_view(request, course_id):
    user_id = request.session.get('user_id')
    user = Create_Account.objects.get(id=user_id)
    user_name = user.name
    current_course = get_object_or_404(Courses, id=course_id)
    course = My_Learning.objects.get(course=current_course, name= user_name)

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    course.delete()
    return redirect('my_learning_view_urls')

def app_course_categories_view(request,category_id):
    template_name = 'learning_application/course_categories.html'

    courses = Courses.objects.filter(category_id=category_id)
    courses_count = courses.count()
    category = Categories.objects.get(id=category_id)
    print({category.category})

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
            context = {
                'user': user,
                'courses': courses,
                'courses_count':courses_count,
                'category':category
            }
        except Create_Account.DoesNotExist:
            return redirect('home_view_urls')
    else:
        return redirect('home_view_urls')

    return render(request, template_name, context)


def app_account_view(request):
    template_name = 'learning_application/account.html'
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
            context = {'user': user}
        except Create_Account.DoesNotExist:
            return redirect('login_page_urls')
    else:
        return redirect('login_page_urls')

    return render(request, template_name, context)


def app_update_account_view(request, account_id):
    template_name = 'learning_application/update_account.html'

    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = Create_Account.objects.get(id=user_id)
        except Create_Account.DoesNotExist:
            return redirect('login_page_urls')
    else:
        return redirect('login_page_urls')

    account = get_object_or_404(Create_Account, id=account_id)

    if request.method == "POST":
        account.name = request.POST.get("name")
        account.email = request.POST.get("email")
        account.number = request.POST.get("number")
        account.dob = request.POST.get("dob")
        account.gender = request.POST.get("gender")

        new_password = request.POST.get('password')
        if new_password:
            account.password = make_password(new_password)

        if request.FILES.get("photo"):
            account.photo = request.FILES["photo"]

        account.save()
        return redirect("app_account_view_urls")
    context = {"account": account, 'user': user}
    return render(request, template_name, context)


def app_delete_account_view(request, account_id):
    template_name = 'learning_application/delete_account.html'
    account = get_object_or_404(Create_Account, id=account_id)

    if request.method == "POST":
        account.delete()
        return redirect("app_home_view_urls")

    context = {"account": account}

    return render(request, template_name, context)
