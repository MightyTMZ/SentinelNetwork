from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from users.models import CustomUser

'''def validate_image_file_extension(value):
    if not value.name.lower().endswith(('.mp4', '.mov', '.avi')):
        raise ValidationError('Unsupported file extension.')'''


class Video(models.Model):
    title = models.CharField(max_length=2083)
    file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi'])])


class Image(models.Model):
    title = models.CharField(max_length=2083)
    file = models.FileField(upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', '.webp'])])


class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    images = models.ManyToManyField(Image)
    videos = models.ManyToManyField(Video)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

