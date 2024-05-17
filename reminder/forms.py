from django import forms
from .models import CustomUser, Task
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper




class Signup(UserCreationForm):
    email = forms.EmailField(max_length=100, required= True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method= "Post"
        

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Title','Task_body','time', 'Done']

    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method= "Post"

