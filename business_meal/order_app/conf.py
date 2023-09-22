from django.db.models import Choices

PENDING_PAYMENT = "pending_payment"
PENDING_CONFIRMATION = "pending_confirmation"
CONFIRMED = "confirmed"
PREPARING = "preparing"
DELIVERING = "delivering"
DELIVERED = "delivered"
READY_FOR_PICKUP = "ready_for_pickup"
CANCELLED = "cancelled"
ORDER_CHOICES = Choices(
    "order",
    [
        PENDING_PAYMENT,
        PENDING_CONFIRMATION,
        CONFIRMED,
        PREPARING,
        DELIVERING,
        DELIVERED,
        READY_FOR_PICKUP,
        CANCELLED,
    ],
)
