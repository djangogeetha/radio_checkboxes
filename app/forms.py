from django import forms

g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('api','API'),('sql','SQL')]

class RegistrationForm(forms.Form):
    Name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)