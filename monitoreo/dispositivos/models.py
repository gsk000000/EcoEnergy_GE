from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

class Organization(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name
    
class Category(BaseModel):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Zone(BaseModel):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Device(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Measurement(BaseModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    measured_at = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.device.name} - {self.value} at {self.measured_at}"
    
class Alert(BaseModel):
    SEVERITY_CHOICES = [
        ("Critical", "Critical"),
        ("High", "High"),
        ("Medium", "Medium"),
    ]

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    message = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    triggered_at = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.severity}] {self.device.name}: {self.message[:30]}..."
    