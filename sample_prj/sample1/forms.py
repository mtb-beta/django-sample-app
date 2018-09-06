from django import forms
from sample1.models import MyModel


class MyModelForm(forms.ModelForm):
    
    class Meta:
        model = MyModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
