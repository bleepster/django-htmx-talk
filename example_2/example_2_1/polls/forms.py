from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class PollsUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(PollsUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Password Confirmation"

class PollsAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(PollsAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["password"].widget.attrs["placeholder"] = "Password"

