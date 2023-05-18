from django.conf import settings
from django.core.mail import send_mail
from typing import List

class SendEmail(object):
    """Função responsável pelo envio de emails

    Args:
        subject: string
        message: string
        email_from: string
        recipients: list of email addresses
    """
    def __init__(
        self, 
        subject: str = None, 
        message: str = None, 
        email_from: str = settings.EMAIL_HOST_USER, 
        recipients: List[str] = None
    ) -> None:
        self.subject = subject
        self.message = message
        self.emailfrom = email_from
        self.recipients = recipients

    def send(self):
        return send_mail(self.subject, self.message, self.emailfrom, self.recipients)