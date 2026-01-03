from django.contrib import admin
from .models import Member, ChitPlan, Payment


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")


@admin.register(ChitPlan)
class ChitPlanAdmin(admin.ModelAdmin):
    list_display = ("plan_name", "monthly_amount", "duration_months")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("member", "month", "amount", "due_date", "status")
    list_filter = ("status",)

    actions = ["mark_as_paid", "mark_as_overdue"]

    def mark_as_paid(self, request, queryset):
        for obj in queryset:
            obj.mark_paid()
    mark_as_paid.short_description = "Mark as PAID (Send message demo)"

    def mark_as_overdue(self, request, queryset):
        for obj in queryset:
            obj.mark_overdue()
    mark_as_overdue.short_description = "Mark as OVERDUE"
