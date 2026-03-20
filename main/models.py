from django.db import models

# Create your models here.
class About(models.Model):
    subtitle = models.CharField(max_length=200, default='Learn About Us')
    title = models.CharField(max_length=200, default='25 Years Experience')
    paragraphs = models.TextField(help_text="Write paragraphs separated by new lines")
    button_text = models.CharField(max_length=50, default='Learn More')
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='about/')

    def get_paragraph_list(self):
        # Split paragraphs on new lines for template
        return self.paragraphs.split('\n')

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    button_link = models.URLField(blank=True, null=True, default="#")

    def __str__(self):
        return self.title
    
class ServicePrice(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='price_images/')

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('haircut', 'Hair Cut'),
        ('hairwash', 'Hair Wash'),
        ('hairstraightening', 'Hair Straightening'),
        ('facial', 'Facial'),
        ('weddinghaircut', 'Wedding Haircut'),
        ('massage', 'Massage'),
        ('hairstyling', 'Hair Styling'),
        ('scalptreatment', 'Scalp Treatment'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    service_type = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.service_type} on {self.date} at {self.time}"
        
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery Image {self.id}"