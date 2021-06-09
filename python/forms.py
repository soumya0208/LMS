from django import forms
from project.models import user,teacher,videoentry,doubt
class UserForm(forms.ModelForm):    
    class Meta:
        model=user
        fields="__all__"
class TeacherForm(forms.ModelForm):    
    class Meta:
        model=teacher
        fields="__all__"
class VideoForm(forms.ModelForm):    
    class Meta:
        model=videoentry
        fields="__all__"
class Doubt1Form(forms.ModelForm):    
    class Meta:
        model=doubt
        fields="__all__"