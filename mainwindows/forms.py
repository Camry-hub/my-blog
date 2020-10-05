from .models import stati
from django.forms import ModelForm, TextInput, Textarea
class StatiForm(ModelForm):
        class Meta:
            model = stati
            fields = ["title", "content"]
            widgets = {
                "title": TextInput(attrs= {
                    "class" : "form-control",
                    "placeholder":"Ввод"
                }),
                "content":Textarea(attrs={
                    "class" : "form-control",
                    "placeholder":"Введите статью"
                })
            }