"""
    Here is the code of models from the database
    --------------------------------------------
    Link https://github.com/build-brain/epi-help/blob/main/api/models.py
"""



from django.db import models
from datetime import date, time



# -------------- Type Trigger -------------------

class TypeTrigger(models.Model):
    """ """
    name     = models.CharField(max_length=150)
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name        = "Type Trigger"
        verbose_name_plural = "Types Trigger"

    def __str__(self):
        return str(self.name)



# -------------- Type Seizure -------------------

class TypeSeizure(models.Model):
    """ """
    name         = models.CharField(max_length=150)
    descriptions = models.TextField()

    class Meta:
        verbose_name        = "Type Seizure"
        verbose_name_plural = "Types Seizure"

    def __str__(self):
        return str(self.name)



# -------------- Type Aura ----------------------

class TypeAura(models.Model):
    """ """
    name         = models.CharField(max_length=150)
    descriptions = models.TextField()

    class Meta:
        verbose_name        = "Type Aura"
        verbose_name_plural = "Types Aura"

    def __str__(self):
        return str(self.name)



# --------------- Seizure -----------------------

class Seizure(models.Model):
    """ """
    when     = models.DateTimeField()
    duration = models.DurationField()
    trigger  = models.CharField(max_length=150)
    descriptions_trigger = models.TextField()
    type = models.OneToOneField(
        TypeSeizure, 
        on_delete = models.CASCADE,
        primary_key=True
    )
    comment = models.TextField()

    class Meta:
        verbose_name        = "Seizure"
        verbose_name_plural = "Seizure"

    def __str__(self):
        return str(self.duration)



# --------------- Aura --------------------------

class Aura(models.Model):
    """ """
    when     = models.DateTimeField()
    duration = models.DurationField()
    trigger  = models.CharField(max_length=150)
    descriptions_trigger = models.TextField()
    type = models.ForeignKey(
        TypeAura,
        on_delete = models.CASCADE,
        primary_key=True
    )
    comment = models.TextField()

    class Meta:
        verbose_name        = "Aura"
        verbose_name_plural = "Aura"

    def __str__(self):
        return str(self.duration)



# --------------- Report Event ------------------

class ReportEvent(models.Model):
    """ """
    when     = models.DateTimeField(auto_now_add = True)
    duration = models.DurationField()
    trigger  = models.ForeignKey(
        TypeTrigger,
        on_delete = models.CASCADE,
        primary_key=True
    )
    descriptions_trigger = models.TextField()
    type = models.OneToOneField(
        TypeSeizure, 
        on_delete = models.CASCADE
    )
    comment = models.TextField()

    class Meta:
        verbose_name        = "Report Event"
        verbose_name_plural = "Report Events"

    def __str__(self):
        return str(self.duration)



# --------------- Content -----------------------

class Content(models.Model):
    """ """
    header = models.CharField(max_length = 150)
    text   = models.TextField()
    date   = models.DateField(default = date.today)
    image  = models.ImageField(upload_to = "content_image/")

    class Meta:
        verbose_name        = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return str(self.header)



# --------------- Contact -----------------------

class Contact(models.Model):
    """ """
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    disable_contact = models.BooleanField(default=False)
    email           = models.EmailField()
    phone_number    = models.CharField(max_length=20)
    # alert_methods   = models.ForeignKey(to, on_delete)


    class Meta:
        verbose_name        = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return str(f"{self.first_name} {self.last_name}" )



# ------------- General Settings ---------------

class GeneralSettings(models.Model):
    """ """
    help_delay        = models.IntegerField()
    phone_sensitivity = models.IntegerField()
    watch_sensitivity = models.IntegerField()
    above_beats       = models.IntegerField()
    bellow_beats      = models.IntegerField()
    audible_alarm     = models.BooleanField(default=True)
    repeat_alarm      = models.IntegerField()
    audible_message   = models.BooleanField(default=True)
    repeat_message    = models.IntegerField()

    class Meta:
        verbose_name        = "General Settings"
        verbose_name_plural = "General Settings"

    def __str__(self):
        return str(f"{self.above_beats} -> {self.bellow_beats}" )



# --------------- My Profile -------------------

class MyProfile(models.Model):
    """ """
    first_name          = models.CharField(max_length=100)
    last_name           = models.CharField(max_length=100)
    email               = models.EmailField()
    phone_number        = models.CharField(max_length=20)
    birthday            = models.DateField()
    weight              = models.IntegerField()
    blood_type          = models.IntegerField()
    allergy             = models.CharField(max_length=200)
    congenital_diseases = models.CharField(max_length=200)
    acquired_diseases   = models.CharField(max_length=200)
    triggers = models.ForeignKey(
        TypeTrigger,
        verbose_name = "Triggers that precede seizures",
        on_delete    = models.CASCADE,
        primary_key  = True
    )
    
    class Meta:
        verbose_name        = "My Profile"
        verbose_name_plural = "My Profiles"

    def __str__(self):
        return str(f"{self.first_name} {self.last_name}" )