from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from .models import allmessage


class IndexView(TemplateView):

    template_name = 'Message'

    @login_required
    def message(request):
        allusers = User.objects.exclude(username=request.user.username).all()
        return render(request, 'message/message.html', {'allusers':allusers})

    @login_required
    def sinmessage(request, slug):
        if request.method == 'POST':
            user = request.user.username
            if slug == user:
                return redirect('singlemessage', slug= slug)

            else:
                message  = request.POST['message']
                allmessagesave = allmessage(user=user, user1=slug, message=message)
                allmessagesave.save()
                return redirect('singlemessage', slug= slug)

        else:
            allmessageuser = User.objects.exclude(username=request.user.username).all()
            alltextmessage = allmessage.objects.all()
        
        return render(request, 'message/singlemessage.html', {'allusers':allmessageuser, 'slug':slug, 'alltextmessage': alltextmessage})