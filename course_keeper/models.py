from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField('date added')

    def __str__(self):
        return self.name

class Hole(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=200, default='')
        course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
        hole_number  = models.IntegerField(validators=[MaxValueValidator(36),MinValueValidator(1)])
        length = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1500)])
        par = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)], default=3)
        target = models.CharField(max_length=200, default='')

        def __str__(self):
            number= str(self.hole_number)
            hole_str = ('Hole' + ': ' + number) 
            return hole_str
