from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200,unique=True,)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    user = models.CharField(max_length=50) #this should link to user profile eventually
    # temporary layout?
    # league layout
    # shorts vs longs
    # public v private
    # dog friendly
    # public park
    # cart ability 1-10

    def __str__(self):
        return self.name

class Hole(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=200, null=True, blank=True)
        course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
        hole_number  = models.IntegerField(validators=[MaxValueValidator(36),MinValueValidator(1)])
        length = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1500)])
        par = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)], default=3)
        target = models.CharField(max_length=200, null=True, blank=True)
        garbage = models.BooleanField(default=False)
        hazard = models.CharField(max_length=200, null=True, blank=True)
        out_boundary = models.BooleanField(default=False)
        mando = models.BooleanField(default=False)

        def __str__(self):
            number= str(self.hole_number)
            hole_str = ('Hole' + ': ' + number) 
            return hole_str
