from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class PollsUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(PollsUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Password Confirmation"

class PollsAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(PollsAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["password"].widget.attrs["placeholder"] = "Password"

