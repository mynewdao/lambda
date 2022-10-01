from django import forms
from item.models import Item, ManyImage


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


class CreateImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = ManyImage
        fields = ['image']


CreateImageFormset = forms.modelformset_factory(ManyImage, CreateImageForm)
