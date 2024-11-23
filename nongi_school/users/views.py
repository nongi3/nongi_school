from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileForm
from .models import SubjectMarks, Subject, Student, Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            prof = p_form.save(commit=False)
            prof.confirmed = False
            prof.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)


def marks_list(request):
    marks = SubjectMarks.objects.all()
    res = []
    for mark in marks:
        if mark.student.profile.user == request.user:
            res.append(mark)
    return render(request, 'users/marks_list.html', {'marks': res})


@login_required
def add_marks(request):
    print('abbabaa')
    if request.method == 'POST':
        mark = request.POST.get('mark')
        subject = request.POST.get('subject')
        student = Student.objects.get(profile=Profile.objects.get(user=request.user))
        SubjectMarks.objects.create(mark=mark, subject=Subject.objects.create(name=subject), student=student)
        return redirect('add_marks')
    else:
        marks = SubjectMarks.objects.all()
        subject = list(Subject.objects.all())
        res = []
        for mark in marks:
            if mark.student.profile.user == request.user:
                res.append(mark)
                if mark.subject.name in [s.name for s in subject]:
                    subject.remove(mark.subject)
        context = {
            'marks': res,
            'subjects': subject
        }
        return render(request, 'users/add_marks.html', context)
