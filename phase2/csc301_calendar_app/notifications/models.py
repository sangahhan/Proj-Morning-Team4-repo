from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    # 'event' or 'course_admin'
    notification_type = models.CharField(max_length=256)

    # The object_id will include the event id if it is an event notification
    # If the notification is a student admin notification, then will include the
    # admin id.
    content_type = models.ForeignKey(ContentType, related_name="subject")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    OWNER_TYPES = (('user', 'User'),
                ('course', 'Course'),
                ('school', 'School'))

    # All notifications are about a course, school or a user
    owner_type = models.CharField(max_length=8, choices=OWNER_TYPES, default='school')
    owner_id = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=128)

    # The owner of the notification
    user = models.ForeignKey(User)

    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_created"]
