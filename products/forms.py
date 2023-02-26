from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=255)
    price = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()


class ReviewCreateform(forms.Form):
    text = forms.CharField(max_length=355)