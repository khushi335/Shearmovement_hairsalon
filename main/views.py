from django.shortcuts import render, redirect
from .models import About, TeamMember, Service,ServicePrice,Appointment, GalleryImage
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    about = About.objects.first()
    services = Service.objects.all()
    team_members = TeamMember.objects.all()
    prices = ServicePrice.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Subject: {subject}\n\n"
            f"Message:\n{message}"
        )

        # Send to Admin
        send_mail(
            subject=f"New Contact Form: {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        # Confirmation to User
        send_mail(
            subject="Thanks for contacting us!",
            message="Thank you for reaching out to Shear Movement Salon. We will get back to you soon.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect('home')

    context = {
        'about': about,
        'services': services,
        'team_members': team_members,
        'prices': prices
    }
    return render(request, 'main/index.html', context)

def about(request):
    about = About.objects.first()  # Get the first About record
    team_members = TeamMember.objects.all()

    context = {
        'about': about,
        'team_section': {
            'subtitle': 'Our Barber Team',
            'title': 'Meet Our Hair Cut Expert Barber',
        },
        'team_members': team_members,
    }
    return render(request, 'main/about.html', context)
    
def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'main/gallery.html', {'images': images})

def service(request):
    services = Service.objects.all()
    return render(request, 'main/service.html', {'services': services})

def price(request):
    services = ServicePrice.objects.all()
    return render(request, 'main/price.html', {'services': services})

def team(request):
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members,
    }
    return render(request, 'main/team.html', context)

# def gallery(request):
#     return render(request, 'main/portfolio.html')

def blog(request):
    return render(request, 'main/blog.html')

def single(request):
    return render(request, 'main/single.html')

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         admin_message = f'New Message from Name: {name} Email: ({email})\n\nSubject: {subject}\n\n Message: {message}'
#         user_message = f'Dear {name},\n\nThanks for contacting Shear Movement.\n\nWe received your message:\n\n{message}\n\nWe will get back to you shortly.\n\nThanks,\nShear Movement Team'

#         send_mail(
#             f'Contact Form: {subject}',
#             admin_message,
#             settings.EMAIL_HOST_USER,
#             [settings.CONTACT_EMAIL],  # Admin email
#             fail_silently=False,
#         )

#         send_mail(
#             'We received your message - Shear Movement',
#             user_message,
#             settings.EMAIL_HOST_USER,
#             [email],  # User email
#             fail_silently=False,
#         )

#         messages.success(request, 'Your message has been sent successfully.')
#         return redirect('contact')

#     return render(request, 'main/contact.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Admin notification
        admin_message = (
            f"New message from:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n\n"
            f"Subject: {subject}\n\n"
            f"Message:\n{message}"
        )

        # Auto-reply to user
        user_message = (
            f"Dear {name},\n\n"
            f"Thanks for contacting Shear Movement.\n\n"
            f"We received your message:\n\n{message}\n\n"
            f"We will get back to you shortly.\n\n"
            f"Best regards,\nShear Movement Team"
        )

        # Send to admin
        send_mail(
            subject=f"Contact Form: {subject}",
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        # Send confirmation to user
        send_mail(
            subject="We received your message - Shear Movement",
            message=user_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')

    return render(request, 'main/contact.html')
    
def appointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')  # corrected
        service_type = request.POST.get('service')  # corrected
        date = request.POST.get('date')
        time = request.POST.get('time')

        if not all([name, email, phone_number, service_type, date, time]):
            messages.error(request, "Please fill in all fields.")
            return render(request, 'main/appointment.html')

        Appointment.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            service_type=service_type,
            date=date,
            time=time
        )

        # Prepare the email content
        subject = f"New Appointment: {service_type.title()} by {name}"
        message = f"""
        You have a new appointment booked:

        Name: {name}
        Email: {email}
        Phone: {phone_number}
        Service: {service_type.title()}
        Date: {date}
        Time: {time}
        """

        # Send email to admin
        admin_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])

        messages.success(request, "Appointment booked successfully!")
        return redirect('appointment')

    return render(request, 'main/appointment.html')