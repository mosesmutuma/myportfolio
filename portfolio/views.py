from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')


def resume(request):
    return render(request, 'portfolio/resume.html')

# portfolio/views.py

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} <{email}>:\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,  # from
                ['mosesmutuma709@gmail.com'],  # 🔁 Replace with your recipient
                fail_silently=False,
            )

            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = ContactForm()

    return render(request, 'portfolio/contacts.html', {'form': form})