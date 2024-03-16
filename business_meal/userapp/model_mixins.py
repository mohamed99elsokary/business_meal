from django.utils.crypto import get_random_string
from django_lifecycle import AFTER_CREATE, LifecycleModelMixin, hook

from ..addonsapp.daftra_integration import create_client
from ..addonsapp.models import SiteConfiguration
from .utils import send_sms


class UserMixin(LifecycleModelMixin):

    @hook(AFTER_CREATE)
    def create_daftra_client(self):
        self.daftra_id = create_client(self.username, self.email)
        self.save(skip_hooks=True)

    @classmethod
    def create_user_or_login(cls, validated_data):
        user = cls.objects.filter(phone=validated_data["phone"])
        if user.count() > 0:
            user = user.first()
        else:
            latest_user = cls.objects.last()
            user = cls.objects.create(
                phone=validated_data["phone"], email=f"{latest_user.id+1}@email.com"
            )
        is_send_msg = SiteConfiguration.objects.first().is_send_msg
        print(is_send_msg)

        user.send_otp(is_send_msg=is_send_msg)
        return user

    def send_otp(self, phone=None, is_send_msg=False):
        otp = self.set_otp(is_send_msg)
        if is_send_msg:
            phone = self.phone if phone is None else phone
            text = f"Your one time password (OTP) for Business Meal is {otp}"
            send_sms(self.phone, text)

    def set_otp(self, is_send_msg=False):
        otp = (
            get_random_string(length=4, allowed_chars="0123456789")
            if is_send_msg
            else 1234
        )
        self.verification_code = otp
        self.save()
        return otp
