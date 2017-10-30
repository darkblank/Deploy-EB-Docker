import django
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


# class UserForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput
#     )
#     age = forms.IntegerField()
#
#     def clean_username(self):
#         data = self.cleaned_data['username']
#         if User.objects.filter(username=data).exists():
#             raise forms.ValidationError('Username already exists')
#         else:
#             return data
#
#     def clean_password2(self):
#         password = self.cleaned_data['password']
#         password2 = self.cleaned_data['password2']
#         if password != password2:
#             raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
#         return password2
#
#     def clean(self):
#         if self.is_valid():
#             setattr(self, 'signup', self._signup)
#
#     def _signup(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         age = self.cleaned_data['age']
#         return User.objects.create_user(
#             username=username,
#             password=password,
#             age=age,
#         )

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ('password1', 'password2')
        for field in class_update_fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = (
            'username',
            'nickname',
            'password1',
            'password2',
            'img_profile',
            'age',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nickname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class LoginForm(forms.Form):
    """
    is_valid()에서 주어진 username/password를 사용한 authenticate실행
    성공시 login(request)메서드를 사용할 수 있음
    """
    username = forms.CharField(
        widget=forms.TextInput
    )
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        self.user = authenticate(username=username, password=password)
        if not self.user:
            raise forms.ValidationError('Invalid login credentials')
        else:
            setattr(self, 'login', self._login)

    def _login(self, request):
        """
        django.contrib.auth.login(request)를 실행

        :param request: django.contrib.auth.login()에 주어질 HttpRequest객체
        :return: None
        """
        return django.contrib.auth.login(request, self.user)
