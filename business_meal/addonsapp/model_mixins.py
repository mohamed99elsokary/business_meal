
from django.core.mail import send_mail
from django.template.loader import render_to_string


class ContactUsMixin(object):
    def send_notification_email(self):
        recipient_list = []
        body = render_to_string(
            "contact_us.html",
            {
                "name": self.name,
                "phone": self.phone_number,
                "email": self.email,
                "message": self.message,
                "subject": self.subject,
            },
        )
        send_mail(
            subject="business_meal Contact Us Form",
            message=body,
            html_message=body,
            from_email="donotreply@bit68.com",
            recipient_list=recipient_list,
        )
