from django.db import models

# Create your models here.

class Seizure(models.Model):
    """ """
    when = models.TimeField()
    duration = models.DurationField()
    trigger = models
    descriptions_trigger = models.TextField()
    type = models.OneToOneField(to, on_delete)
    comment = models.TextField()

    class Meta:
        verbose_name = "Seizure"
        verbose_name_plural = "Seizure"

    def __str__(self):
        return str(self.duration)


class TypeSeizure(models.Model):
    """ """
    name = models.CharField()
    descriptions = models.TextField()

    class Meta:
        verbose_name = "Type Seizure"
        verbose_name_plural = "Types Seizure"

    def __str__(self):
        return str(self.name)


class Aura(models.Model):
    """ """
    when = models.TimeField()
    duration = models.DurationField()
    trigger = models
    descriptions_trigger = models.TextField()
    type = models.OneToOneField(to, on_delete)
    comment = models.TextField()

    class Meta:
        verbose_name = "Seizure"
        verbose_name_plural = "Seizure"

    def __str__(self):
        return str(self.duration)


class TypeAura(models.Model):
    """ """
    name = models.CharField()
    descriptions = models.TextField()

    class Meta:
        verbose_name = "Type Seizure"
        verbose_name_plural = "Types Seizure"

    def __str__(self):
        return str(self.name)


class Content(models.Model):
    """ """
    header = models.CharField()
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField()


    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return str(self.header)


class Contact(models.Model):
    """ """
    first_name = models.CharField()
    last_name = models.CharField()
    disable_contact = models.BooleanField()
    email = models.EmailField()
    phone_number = models.CharField()


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return str(f"{self.first_name} {self.last_name}" )

