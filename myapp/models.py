"""
"""
from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    """
    """
    name = models.CharField(max_length=30)
    cdt = models.DateTimeField(auto_now_add=True) # creation date
    mdt = models.DateTimeField(auto_now=True) #modification date

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return "%d - %s" % (self.id, self.name)


class Skill(models.Model):
    """
    """
    name = models.CharField(max_length=30)
    cdt = models.DateTimeField(auto_now_add=True) # creation date
    mdt = models.DateTimeField(auto_now=True) #modification date

    class Meta:
        db_table = 'skills'

    def __str__(self):
        return "%d - %s" % (self.id, self.name)


class Designation(models.Model):
    """
    """
    name = models.CharField(max_length=30)
    cdt = models.DateTimeField(auto_now_add=True) # creation date
    mdt = models.DateTimeField(auto_now=True) #modification date

    class Meta:
        db_table = 'designations'

    def __str__(self):
        return "%d - %s" % (self.id, self.name)


class Profiles(models.Model):
    """
    """
    RESUME_CHOICES = (
            (1, "Yes"),
            (2, "No"),
    )
    sno = models.IntegerField()
    mobile = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    resume = models.IntegerField(choices=RESUME_CHOICES, default=2)
    experience = models.DecimalField(max_digits=20, decimal_places=2)
    ctc = models.DecimalField(max_digits=20, decimal_places=2)
    current_city = models.ForeignKey(City)
    preferred_city = models.ForeignKey(City, related_name='profile')
    current_employer = models.CharField(max_length=30)
    current_designation = models.ForeignKey(Designation)
    skills = models.ManyToManyField(Skill)
    cdt = models.DateTimeField(auto_now_add=True) # creation date
    mdt = models.DateTimeField(auto_now=True) #modification date

    class Meta:
        db_table = 'profiles'
        permissions = (("can_view_profile", "Can view profiles"),
                        ("can_download_profiles", "Can download profiles"),)

    def __str__(self):
        return "%d - %s" % (self.id, self.name)

    def get_skills(self):
        skills = ""
        for skill in self.skills.all():
            skills += "," + skill.name
        return skills[1:]
