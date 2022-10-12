from django.db import models
from datetime import date


class TypeSeizure(models.Model):
    """ """
    name = models.CharField(max_length=150)
    descriptions = models.TextField()

    class Meta:
        verbose_name = "Type Seizure"
        verbose_name_plural = "Types Seizure"

    def __str__(self):
        return str(self.name)


class Seizure(models.Model):
    """ """
    when = models.TimeField(default = date.today)
    duration = models.DurationField()
    trigger = models.CharField(max_length=150)
    descriptions_trigger = models.TextField()
    type = models.OneToOneField(
        TypeSeizure, 
        on_delete = models.CASCADE,
        primary_key=True
    )
    comment = models.TextField()

    class Meta:
        verbose_name = "Seizure"
        verbose_name_plural = "Seizure"

    def __str__(self):
        return str(self.duration)


class TypeAura(models.Model):
    """ """
    name = models.CharField(max_length=150)
    descriptions = models.TextField()

    class Meta:
        verbose_name = "Type Aura"
        verbose_name_plural = "Types Aura"

    def __str__(self):
        return str(self.name)


class Aura(models.Model):
    """ """
    when = models.TimeField(default = date.today)
    duration = models.DurationField()
    trigger = models.CharField(max_length=150)
    descriptions_trigger = models.TextField()
    type = models.OneToOneField(
        TypeAura,
        on_delete = models.CASCADE,
        primary_key=True
    )
    comment = models.TextField()

    class Meta:
        verbose_name = "Aura"
        verbose_name_plural = "Aura"

    def __str__(self):
        return str(self.duration)


class Content(models.Model):
    """ """
    header = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="content_image/")

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return str(self.header)


class Contact(models.Model):
    """ """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    disable_contact = models.BooleanField(default=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return str(f"{self.first_name} {self.last_name}" )

