from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def table(request):
    product_obj = Product.objects.all()
    return render(request, "table.html", {"product_obj": product_obj})


def add_product(request):
    return render(request, "product.html")


def ragistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exists")
            return redirect("/")
        else:
            User.objects.create(name=name, email=email, password=password)
            messages.success(request, "Registrations Successful!")
            return redirect("/login/")


def login_user(request):
    if request.method == "POST":
        user = User.objects.get(email=request.POST["email"])
        if check_password(request.POST["password"], user.password):
            request.session["logged"] = True
            request.session["id"] = user.id
            request.session["username"] = user.name
            request.session["email"] = user.email
            return redirect("/table/")
        else:
            messages.warning(request, "Invalid Email or Password")
            return redirect("/login/")


def delete(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect("/table/")


def product(request):
    if request.method == "POST":
        title = request.POST["name"]
        description = request.POST["email"]
        product_image = request.FILES.get("image")
        Product.objects.create(
            title=title, description=description, product_image=product_image
        )
        messages.success(request, "Product Add Successful!")
        return redirect("/table/")


def update(request, uid):
    user_obj = Product.objects.get(id=uid)
    return render(request, "update.html", {"user_obj": user_obj})


def update_product(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        title = request.POST["title"]
        description = request.POST["description"]
        product_image = request.FILES.get("image")
        product_obj = Product.objects.get(id=uid)
        product_obj.title = title
        product_obj.description = description

        if product_image:
            product_obj.product_image = product_image

        product_obj.save()
        return redirect("/table/")
