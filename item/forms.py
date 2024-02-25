from django import forms

from .models import Items

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['category','publication','is_combo','book_name','description','price','image']

        # widgets = {
        #     'category' : forms.Select(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        #     'publication' : forms.TextInput(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        #     'is_combo' : forms.CheckboxInput(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        #     'book_name' : forms.TextInput(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        #     'description' : forms.Textarea(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        #     'price' : forms.NumberInput(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        #     'image' : forms.FileInput(attrs={
        #         'class' : "w-full rounded-xl px-6 py-6 border"
        #     }),
        # }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['publication','is_combo','book_name','description','price','image','is_sold']

        widgets = {
            'publication' : forms.TextInput(attrs={
                'class' : "w-full rounded-xl px-6 py-6 border"
            }),
            'book_name' : forms.TextInput(attrs={
                'class' : "w-full rounded-xl px-6 py-6 border"
            }),
            'description' : forms.Textarea(attrs={
                'class' : "w-full rounded-xl px-6 py-6 border"
            }),
            'price' : forms.NumberInput(attrs={
                'class' : "w-full rounded-xl px-6 py-6 border"
            }),
            'image' : forms.FileInput(attrs={
                'class' : "w-full rounded-xl px-6 py-6 border"
            }),
        }