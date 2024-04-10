from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from myapp2.models import Product

from .forms import ImageUploadForm, ProductForm


def image_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageUploadForm()
    return render(request, "myapp4/image_upload.html", {"form": form})


def product_upload(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            qnt = form.cleaned_data["qnt"]
            image = form.cleaned_data["image"]
            product = Product(
                title=title,
                description=description,
                price=price,
                qnt=qnt,
                image=image,
            )
            product.save()
            # fs = FileSystemStorage()
            # fs.save(image.name, image)
    else:
        form = ProductForm()
    return render(request, "myapp4/product_upload.html", {"form": form})
