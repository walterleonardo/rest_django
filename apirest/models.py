from django.db import models
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError(u'Is not a valid file, need to be CSV', code='invalid')

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs', max_length=100, validators=[validate_file_extension])
    uploaded = models.DateField(auto_now=False, auto_now_add=True)
    activated = models.BooleanField( default=False)

    def __str__(self):
        return f"File id: {self.id}     - File name: {self.file_name}    - File uploaded: {self.uploaded}     - File activated: {self.activated} "