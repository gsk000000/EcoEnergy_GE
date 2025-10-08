from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Zone(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    maximum_consumption = models.IntegerField()
    state = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    date = models.DateTimeField()
    registered_consumption = models.IntegerField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.registered_consumption} kWh"
    
class Alert(models.Model):
    message = models.CharField(max_length=250)
    alert_level = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Alert {self.device} - {self.message}"