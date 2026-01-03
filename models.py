from django.db import models
from django.utils import timezone


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ChitPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()

    def __str__(self):
        return self.plan_name


class Payment(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("OVERDUE", "Overdue"),
    )

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    chit_plan = models.ForeignKey(ChitPlan, on_delete=models.CASCADE)

    month = models.CharField(max_length=20)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    payment_date = models.DateField(null=True, blank=True)
    message_log = models.TextField(blank=True)

    def mark_paid(self):
        self.status = "PAID"
        self.payment_date = timezone.now().date()
        self.message_log = f"Message sent: Payment received for {self.month}"
        self.save()

    def mark_overdue(self):
        self.status = "OVERDUE"
        self.save()

    def __str__(self):
        return f"{self.member} - {self.month}"
