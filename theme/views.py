from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
# from .forms import contactForm
from django.core.mail import send_mail
from .models import usersIdeas


class IndexView(TemplateView):

    template_name = 'Theme'

    def home(request):
        if request.method == 'POST':
            user = request.user.username
            first_name = request.user.first_name
            last_name = request.user.last_name
            comment = request.POST['comment']
            
            usercomment = usersIdeas(user=user, first_name=first_name, last_name=last_name, comment=comment)
            usercomment.save()
            messages.info(request, 'Your comment is published.')
            return redirect('home')
        
        else:
            allcomment = usersIdeas.objects.all()

        return render(request, 'theme/home.html', {'allcomment':allcomment})

    def about(request):
        return render(request, 'theme/about.html')

    def contact(request):
        return render(request, 'theme/contact.html')
