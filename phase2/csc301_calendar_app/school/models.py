from django.db import models

# Create your models here.
class SchoolProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.

    school_name = models.CharField(max_length=128, unique=True)
    email_domain = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.school_name
    
class Course(models.Model):
    # This line is required. Links UserProfile to a User model instance.

    course_name = models.CharField(max_length=128, unique=True)
    school_id = models.ForeignKey('SchoolProfile')
    def __unicode__(self):
        return self.SchoolProfile.school_name