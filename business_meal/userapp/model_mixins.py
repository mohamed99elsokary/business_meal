from django.utils.crypto import get_random_string

from .utils import send_sms


class UserMixin:
    def soft_delete(self):
        self.is_deleted = True
        user_email = self.email
        random = get_random_string(10)
        self.email = user_email + random
        self.save()
        return self

    @classmethod
    def create_user_or_login(cls, validated_data):
        user, created = cls.objects.get_or_create(phone=validated_data["phone"])
        user.send_otp()
        return user

    def send_otp(self, phone=None):
        phone = self.phone if phone is None else phone
        otp = self.set_otp()
        text = f"Your one time password (OTP) for Business Meal is {otp}"
        # send_sms(self.phone, text)

    def set_otp(self):
        otp = get_random_string(length=4, allowed_chars="0123456789")
        otp = 1234
        self.verification_code = otp
        self.save()
        return otp
