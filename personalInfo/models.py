from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from frontend.templatetags.tags import ContentTypeRestrictedFileField
# from multiselectfield import MultiSelectField

class Profile(models.Model):
    #_id = models.AutoField(primary_key=True)
    username = models.CharField(User, primary_key=True, max_length=100)
    name = models.CharField(max_length=100,blank=True, help_text="Don't write salutation, Just write name")
    email = models.CharField(max_length=40,null=True,blank=True)
    institute = models.CharField(max_length=100)
    #profile_image = ContentTypeRestrictedFileField(upload_to = "profile_images", max_length=20000, blank=True, null=True, content_types=['image/jpeg', 'image/gif', 'image/png', 'image/jpg'], help_text="Only jpg, gif, png formats Size < 5MB | preferable resolution 512x512", max_upload_size=5242880)
    post = models.CharField(choices = (
                                    ("Professor", ("Professor")),
                                    ("Assistant Professor", ("Assistant Professor")),
                                    ("Associate Professor", ("Associate Professor")),
                                    ("Emeritus Professor", ("Emeritus Professor")),
                                    ("Visiting Professor", ("Visiting Professor")),
                                    ("Adjunct Professor", ("Adjunct Professor")),
				    ("Retired Professor", ("Retired Professor")),

                                )
                                 ,default="Professor",max_length=30)

    areas_of_interest = models.CharField(max_length=1500,blank=False)#required field
    #upload_cv = ContentTypeRestrictedFileField(upload_to = "cv", max_length=20000, blank=True, null=True, content_types=['image/jpeg', 'image/gif', 'image/png', 'image/jpg', 'application/pdf', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/msword'], max_upload_size=10485760, help_text="In pdf, ppt, pptx, doc, docx, png, gif, jpeg  format Size < 10MB")
    upload_cv = models.FileField(upload_to='/media/', blank=True)
    skypeId = models.CharField(max_length=40,null=True,blank=True)
    personal_home_page_link = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    #_id = models.AutoField(primary_key=True)
    username = models.CharField(User, primary_key=True, max_length=100)
    name = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=40,null=True,blank=True)
    institute = models.CharField(max_length=100)
    #profile_image = ContentTypeRestrictedFileField(upload_to = "profile_images", max_length=20000, blank=True, null=True, content_types=['image/jpeg', 'image/gif', 'image/png', 'image/jpg'], help_text="Only jpg, gif, png formats Size < 5MB | preferable resolution 512x512", max_upload_size=5242880)
    areas_of_interest = models.CharField(max_length=1500,blank=True)
    upload_cv = models.FileField(upload_to='/media/', blank=True)
    work_highlight = models.TextField(max_length=2000,null=True, blank=True)
    def __str__(self):
        return self.name
