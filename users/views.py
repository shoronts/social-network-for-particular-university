from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from .forms import loginForm, techerRegisterForm, companyRegisterForm, studentRegisterForm
from .models import allUsersInfo, recomendationDetails
from django.core.mail import send_mail
from django.http import Http404

# pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class IndexView(TemplateView):

    template_name = 'Users'

    def register(request):
        return render(request, 'users/register.html')


    def teacherRegister(request):
        if request.user.is_authenticated:
            return redirect('profile')

        elif request.method == 'POST':
            form = techerRegisterForm(request.POST)
            if form.is_valid():
                firstName = form.cleaned_data['first_name']
                lastName = form.cleaned_data['last_name']
                id_number = form.cleaned_data['id_number']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                college = form.cleaned_data['college']
                department = form.cleaned_data['department']
                userName = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = User.objects.create_user(first_name = firstName, last_name = lastName, email = email, username = userName, password = password)
                user.save()

                user_information = allUsersInfo(user=user, college=college, department=department, id_number=id_number,phone_number=phone_number, is_teacher = True )
                user_information.save()

                messages.success(request, "Your account is created successfully. Thank you!")
                return redirect('login')

            else:
                form = techerRegisterForm()

        return render(request, 'users/teacherregister.html', {'form' : form})


    def studentRegister(request):
        if request.user.is_authenticated:
            return redirect('profile')

        elif request.method == 'POST':
            form = studentRegisterForm(request.POST)
            if form.is_valid():
                firstName = form.cleaned_data['first_name']
                lastName = form.cleaned_data['last_name']
                id_number = form.cleaned_data['id_number']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                specialization = form.cleaned_data['specialization']
                degree = form.cleaned_data['degree']
                college = form.cleaned_data['college']
                year_of_graduat = form.cleaned_data['year_of_graduat']
                userName = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = User.objects.create_user(first_name = firstName, last_name = lastName, email = email, username = userName, password = password)
                user.save()

                user_information = allUsersInfo(user=user, college=college, id_number=id_number,phone_number=phone_number, specialization=specialization,  degree=degree, year_of_graduat=year_of_graduat, is_student=True)
                user_information.save()

                messages.success(request, "Your account is created successfully. Thank you!")
                return redirect('login')

        else:
            form = studentRegisterForm()

        return render(request, 'users/studentregister.html', {'form' : form})


    def companyRegister(request):
        if request.user.is_authenticated:
            return redirect('profile')

        elif request.method == 'POST':
            form = companyRegisterForm(request.POST)
            if form.is_valid():
                firstName = form.cleaned_data['first_name']
                lastName = form.cleaned_data['last_name']
                id_number = form.cleaned_data['id_number']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']

                specialization = form.cleaned_data['specialization']
                company_size = form.cleaned_data['company_size']
                userName = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = User.objects.create_user(first_name = firstName, last_name = lastName, email = email, username = userName, password = password)
                user.save()

                user_information = allUsersInfo(user=user, id_number=id_number,phone_number=phone_number, specialization=specialization,  company_size=company_size, is_company=True)
                user_information.save()

                messages.success(request, "Your account is created successfully. Thank you!")
                return redirect('login')

        else:
            form = companyRegisterForm()

        return render(request, 'users/companyregister.html', {'form' : form})


    def login(request):
        if request.user.is_authenticated:
            return redirect('profile')

        elif request.method == 'POST':
            form = loginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                if User.objects.get(username=username).is_active:
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        request.session['usernameAll'] = username
                        if 'next' in request.POST:
                            return redirect(request.POST.get('next'))

                        else:
                            return redirect('home')              

                    else:
                        messages.error(request, "Password Dosen't Match")
                        return redirect('login')
                else:
                    messages.error(request, 'Your Account Is Not Activated.')
                    return redirect('login')

        else:
            form = loginForm()

        return render(request, 'users/login.html', {'form':form})


    def logout(request):
        auth.logout(request)
        return redirect('login')


    @login_required
    def profile(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            
            user_profile_update = allUsersInfo.objects.get(user=request.user.id)
            user_mainprofile_update = User.objects.get(pk=request.user.id)

            user_mainprofile_update.first_name = first_name
            user_mainprofile_update.last_name = last_name
            user_mainprofile_update.email = email
            user_mainprofile_update.username = username
            user_mainprofile_update.save()

            user_profile_update.phone_number = phone_number
            user_profile_update.save()

            messages.info(request, 'Your profile is updated')
            return redirect('profile')

        return render(request, 'users/profile.html')

    @login_required
    def recommend(request):
        if request.user.allusersinfo.is_teacher:
            if request.method == 'POST':
                user = request.POST['full_name']
                university_of_graduation = request.POST['university_of_graduation']
                department_and_major = request.POST['department_and_major']
                graduations_degree = request.POST['graduations_degree']
                grade_and_gpa = request.POST['grade_and_gpa']
                studies_student_wishes_to_pursue = request.POST['studies_student_wishes_to_pursue']
                specialization_in_higher_studies = request.POST['specialization_in_higher_studies']
                mobile_number = request.POST['mobile_number']
                email = request.POST['email']

                academic_excellence = request.POST['shoron']
                initiavive_and_motivation = request.POST['shoron1']
                expreeing_ideas = request.POST['shoron2']
                critical_thinking = request.POST['shoron3']
                ability_to_accept_and_utilize_criticism = request.POST['shoron4']
                self_confidence_and_responsibility = request.POST['shoron5']
                ability_to_plan_and_execute_research = request.POST['shoron6']
                acquiring_research_technique = request.POST['shoron7']
                creative_and_originality = request.POST['shoron8']
                linguistic_ikills = request.POST['shoron9']
                general_knowledge = request.POST['shoron10']
                overall_evaluation = request.POST['shoron11']
                note_about_the_applicant = request.POST['shoron12']

                faculty_dean_name = request.POST['faculty_dean_name']
                faculty_dean_signature = request.POST['faculty_dean_signature']
                faculty_dean_date = request.POST['faculty_dean_date']

                recommenders_name = request.POST['recommenders_name']
                academic_position = request.POST['academic_position']
                academic_department = request.POST['academic_department']

                userDetails = User.objects.get(username=user)
                full_name = userDetails.first_name + ' ' + userDetails.last_name

                try:
                    is_already_done = recomendationDetails.objects.all()
                    is_already_done_list = []
                    for x in is_already_done:
                        if x.user == user:
                            is_already_done_list.append(x.slug)
                            
                    url = full_name + str(len(is_already_done_list))

                except:
                        url = full_name + str(1)

                texhersRecommendation = recomendationDetails(
                    url = url,
                    user = user,
                    full_name = full_name,
                    university_of_graduation = university_of_graduation,
                    department_and_major = department_and_major,
                    graduations_degree = graduations_degree,
                    grade_and_gpa = grade_and_gpa,
                    studies_student_wishes_to_pursue = studies_student_wishes_to_pursue,
                    specialization_in_higher_studies = specialization_in_higher_studies,
                    mobile_number = mobile_number,
                    email = email,

                    academic_excellence = academic_excellence,
                    initiavive_and_motivation = initiavive_and_motivation,
                    expreeing_ideas = expreeing_ideas,
                    critical_thinking = critical_thinking,
                    ability_to_accept_and_utilize_criticism = ability_to_accept_and_utilize_criticism,
                    self_confidence_and_responsibility = self_confidence_and_responsibility,
                    ability_to_plan_and_execute_research = ability_to_plan_and_execute_research,
                    acquiring_research_technique = acquiring_research_technique,
                    creative_and_originality = creative_and_originality,
                    linguistic_ikills = linguistic_ikills,
                    general_knowledge = general_knowledge,
                    overall_evaluation = overall_evaluation,
                    note_about_the_applicant = note_about_the_applicant,

                    faculty_dean_name = faculty_dean_name,
                    faculty_dean_signature = faculty_dean_signature,
                    faculty_dean_date = faculty_dean_date,

                    recommenders_name = recommenders_name,
                    academic_position = academic_position,
                    academic_department = academic_department,
                )
                texhersRecommendation.save()
                messages.info(request, 'Recemendation is send. Thank you!!!')
                return redirect('recommendlist')

            else:
                allstudent = allUsersInfo.objects.filter(is_student=True).all()
            return render(request, 'users/recommend.html', {'allstudent':allstudent})
        
        else:
            return redirect('profile')

    @login_required
    def recommendlist(request):
        if request.user.allusersinfo.is_teacher or request.user.allusersinfo.is_student:
            allrecommend = recomendationDetails.objects.all().order_by('-current_date')
            return render(request, 'users/recommendlist.html', {'allrecommend':allrecommend})
            
        else:
            raise Http404

    @login_required
    def recommendlistedit(request, slug):
        if request.user.allusersinfo.is_teacher:
            if request.method == 'POST':
                user = request.POST['user']
                full_name = request.POST['full_name']
                university_of_graduation = request.POST['university_of_graduation']
                department_and_major = request.POST['department_and_major']
                graduations_degree = request.POST['graduations_degree']
                grade_and_gpa = request.POST['grade_and_gpa']
                studies_student_wishes_to_pursue = request.POST['studies_student_wishes_to_pursue']
                specialization_in_higher_studies = request.POST['specialization_in_higher_studies']
                mobile_number = request.POST['mobile_number']
                email = request.POST['email']

                academic_excellence = request.POST['shoron']
                initiavive_and_motivation = request.POST['shoron1']
                expreeing_ideas = request.POST['shoron2']
                critical_thinking = request.POST['shoron3']
                ability_to_accept_and_utilize_criticism = request.POST['shoron4']
                self_confidence_and_responsibility = request.POST['shoron5']
                ability_to_plan_and_execute_research = request.POST['shoron6']
                acquiring_research_technique = request.POST['shoron7']
                creative_and_originality = request.POST['shoron8']
                linguistic_ikills = request.POST['shoron9']
                general_knowledge = request.POST['shoron10']
                overall_evaluation = request.POST['shoron11']
                note_about_the_applicant = request.POST['shoron12']

                faculty_dean_name = request.POST['faculty_dean_name']
                faculty_dean_signature = request.POST['faculty_dean_signature']
                faculty_dean_date = request.POST['faculty_dean_date']

                recommenders_name = request.POST['recommenders_name']
                academic_position = request.POST['academic_position']
                academic_department = request.POST['academic_department']

                student_recommend_update = recomendationDetails.objects.get(slug=slug)

                student_recommend_update.full_name = full_name
                student_recommend_update.university_of_graduation = university_of_graduation
                student_recommend_update.department_and_major = department_and_major
                student_recommend_update.graduations_degree = graduations_degree
                student_recommend_update.grade_and_gpa = grade_and_gpa
                student_recommend_update.studies_student_wishes_to_pursue = studies_student_wishes_to_pursue
                student_recommend_update.specialization_in_higher_studies = specialization_in_higher_studies
                student_recommend_update.mobile_number = mobile_number
                student_recommend_update.email = email

                student_recommend_update.academic_excellence = academic_excellence
                student_recommend_update.initiavive_and_motivation = initiavive_and_motivation
                student_recommend_update.expreeing_ideas = expreeing_ideas
                student_recommend_update.critical_thinking = critical_thinking
                student_recommend_update.ability_to_accept_and_utilize_criticism = ability_to_accept_and_utilize_criticism
                student_recommend_update.self_confidence_and_responsibility = self_confidence_and_responsibility
                student_recommend_update.ability_to_plan_and_execute_research = ability_to_plan_and_execute_research
                student_recommend_update.acquiring_research_technique = acquiring_research_technique
                student_recommend_update.creative_and_originality = creative_and_originality
                student_recommend_update.linguistic_ikills = linguistic_ikills
                student_recommend_update.general_knowledge = general_knowledge
                student_recommend_update.overall_evaluation = overall_evaluation
                student_recommend_update.note_about_the_applicant = note_about_the_applicant

                student_recommend_update.faculty_dean_name = faculty_dean_name
                student_recommend_update.faculty_dean_signature = faculty_dean_signature
                student_recommend_update.faculty_dean_date = faculty_dean_date

                student_recommend_update.recommenders_name = recommenders_name
                student_recommend_update.academic_position = academic_position
                student_recommend_update.academic_department = academic_department

                student_recommend_update.save()
                messages.info(request, 'Recemendation edited. Thank you!!!')
                return redirect('recommendlist')

            else:
                allrecommend = recomendationDetails.objects.get(slug=slug)
                return render(request, 'users/recommendlistedit.html', {'allrecommend':allrecommend})

        else:
            raise Http404

    @login_required
    def recommendlistdelete(request, slug):
        if request.user.allusersinfo.is_teacher:
            recomendationDetails.objects.get(slug=slug).delete()
            return redirect('recommendlist')

        else:
            raise Http404

    @login_required
    def recommendpdf(request, slug):
        template_path = 'users/pdf.html'
        context = {'recommenddata':  recomendationDetails.objects.get(slug=slug)}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="studentrecommendationreport.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
        