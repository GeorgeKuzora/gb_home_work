from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.IntegerField(min_value=1)
    qnt = forms.IntegerField(min_value=0)
    image = forms.ImageField()
