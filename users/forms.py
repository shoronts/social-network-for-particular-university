from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class loginForm(forms.Form):
    username = forms.CharField(label="Username",
        error_messages = {'required' : 'Enter a valid Username.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Username',
            'class' : 'form-control'
            })
    )

    password = forms.CharField(label = "Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Password',
            'class' : 'form-control'
            })
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username = data).exists():
            raise ValidationError("Username Dosen't Match")
        return data


        

class techerRegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name",
        error_messages = {'required' : 'Enter your First Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'First Name',
            'class' : 'form-control'
            })
    )


    last_name = forms.CharField(label="Last Name",
        error_messages = {'required' : 'Enter your Last Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Last Name',
            'class' : 'form-control'
            })
    )

    username = forms.CharField(label="Userame",
        error_messages = {'required' : 'Enter your Userame.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Userame',
            'class' : 'form-control'
            })
    )

    id_number = forms.CharField(label="ID Number",
        error_messages = {'required' : 'Enter your ID Number.'},
        max_length = 50,
        widget = forms.NumberInput( attrs = {
            'placeholder' : 'ID Number',
            'class' : 'form-control'
            })
    )

    email = forms.EmailField(label="Email",
        error_messages = {'required' : 'Enter a valid Email.'},
        max_length = 50,
        widget = forms.EmailInput( attrs = {
            'placeholder' : 'Email',
            'class' : 'form-control'
            })
    )

    phone_number = forms.CharField(label="Phone Number",
        error_messages = {'required' : 'Enter your Phone Number.'},
        max_length = 50,
        widget = forms.NumberInput( attrs = {
            'placeholder' : 'Phone Number',
            'class' : 'form-control'
            })
    )

    password = forms.CharField(label = "Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Password',
            'class' : 'form-control'
            })
    )

    confirm_password = forms.CharField(label = "Confirm Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Confirm Password',
            'class' : 'form-control'
            })
    )

    college = forms.CharField(label="College",
        error_messages = {'required' : 'Enter your College.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'College',
            'class' : 'form-control'
            })
    )

    department = forms.CharField(label="Department",
        error_messages = {'required' : 'Enter your Department.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Department',
            'class' : 'form-control'
            })
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username = data).exists():
            raise ValidationError("A user with this username already exists!")
        return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email = data).exists():
            raise ValidationError("A user with this Email already exists!")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                error = "Password Did not Match!!"
                self.add_error('password', error)
                self.add_error('confirm_password', error)




class companyRegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name",
        error_messages = {'required' : 'Enter your First Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'First Name',
            'class' : 'form-control'
            })
    )


    last_name = forms.CharField(label="Last Name",
        error_messages = {'required' : 'Enter your Last Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Last Name',
            'class' : 'form-control'
            })
    )

    username = forms.CharField(label="Userame",
        error_messages = {'required' : 'Enter your Userame.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Userame',
            'class' : 'form-control'
            })
    )

    id_number = forms.CharField(label="ID Number",
        error_messages = {'required' : 'Enter your ID Number.'},
        max_length = 50,
        widget = forms.NumberInput( attrs = {
            'placeholder' : 'ID Number',
            'class' : 'form-control'
            })
    )

    email = forms.EmailField(label="Email",
        error_messages = {'required' : 'Enter a valid Email.'},
        max_length = 50,
        widget = forms.EmailInput( attrs = {
            'placeholder' : 'Email',
            'class' : 'form-control'
            })
    )

    phone_number = forms.CharField(label="Phone Number",
        error_messages = {'required' : 'Enter your Phone Number.'},
        max_length = 50,
        widget = forms.NumberInput( attrs = {
            'placeholder' : 'Phone Number',
            'class' : 'form-control'
            })
    )

    password = forms.CharField(label = "Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Password',
            'class' : 'form-control'
            })
    )

    confirm_password = forms.CharField(label = "Confirm Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Confirm Password',
            'class' : 'form-control'
            })
    )

    specialization = forms.CharField(label="Specialization",
        error_messages = {'required' : 'Enter your Specialization.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Specialization',
            'class' : 'form-control'
            })
    )

    company_size = forms.CharField(label="Company Size",
        error_messages = {'required' : 'Enter your Company Size.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Company Size',
            'class' : 'form-control'
            })
    )    


    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username = data).exists():
            raise ValidationError("A user with this username already exists!")
        return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email = data).exists():
            raise ValidationError("A user with this Email already exists!")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                error = "Password Did not Match!!"
                self.add_error('password', error)
                self.add_error('confirm_password', error)




class studentRegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name",
        error_messages = {'required' : 'Enter your First Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'First Name',
            'class' : 'form-control'
            })
    )


    last_name = forms.CharField(label="Last Name",
        error_messages = {'required' : 'Enter your Last Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Last Name',
            'class' : 'form-control'
            })
    )

    username = forms.CharField(label="Userame",
        error_messages = {'required' : 'Enter your Userame.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Userame',
            'class' : 'form-control'
            })
    )

    id_number = forms.CharField(label="ID Number",
        error_messages = {'required' : 'Enter your ID Number.'},
        max_length = 50,
        widget = forms.NumberInput( attrs = {
            'placeholder' : 'ID Number',
            'class' : 'form-control'
            })
    )

    email = forms.EmailField(label="Email",
        error_messages = {'required' : 'Enter a valid Email.'},
        max_length = 50,
        widget = forms.EmailInput( attrs = {
            'placeholder' : 'Email',
            'class' : 'form-control'
            })
    )

    phone_number = forms.CharField(label="Phone Number",
        error_messages = {'required' : 'Enter your Phone Number.'},
        max_length = 50,
        widget = forms.NumberInput( attrs = {
            'placeholder' : 'Phone Number',
            'class' : 'form-control'
            })
    )

    password = forms.CharField(label = "Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Password',
            'class' : 'form-control'
            })
    )

    confirm_password = forms.CharField(label = "Confirm Password",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Confirm Password',
            'class' : 'form-control'
            })
    )

    specialization = forms.CharField(label="Specialization",
        error_messages = {'required' : 'Enter your Specialization.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Specialization',
            'class' : 'form-control'
            })
    )

    degree = forms.CharField(label="Degree",
        error_messages = {'required' : 'Enter your Degree.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Degree',
            'class' : 'form-control'
            })
    )

    year_of_graduat = forms.DateField(label="Year of Graduat",
        widget = forms.DateInput( attrs = {
            'class' : 'form-control',
            'type' : 'date'
            })
    )

    college = forms.CharField(label="College",
        error_messages = {'required' : 'Enter your College.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'College',
            'class' : 'form-control'
            })
    )


    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username = data).exists():
            raise ValidationError("A user with this username already exists!")
        return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email = data).exists():
            raise ValidationError("A user with this Email already exists!")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                error = "Password Did not Match!!"
                self.add_error('password', error)
                self.add_error('confirm_password', error)
        