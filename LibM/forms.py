from pyexpat import model
from tkinter import Widget
from django import forms
from . models import Books,Category

#  نسوي هاي الكلاس ونستخدم الفورم بيه حته نكدر نضيف شغلات من الفرونت
class Bookforme(forms.ModelForm):
     class Meta:
        model = Books
        #fields = '__all__'  # any fields in model came to here
        fields= [
                 'title',
                 'author',
                 'photo_book',
                 'photo_author',
                 'pages',
                 'price',
                 'retal_price_day',
                 'retal_period',
                 'status',
                 'catagery',
                ] 
        widgets={

            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput({'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class':'form-control'}),
            'retal_period': forms.NumberInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'catagery': forms.Select(attrs={'class':'form-control'}),
            
            }

class Categeryforme(forms.ModelForm):
    class Meta:
        model = Category
        #fields = '__all'  # any fields in model came to here

        fields =[
            'name',
            ]

        Widgets={
                'name':forms.TextInput(attrs={'class':'form-control'}),
                }

