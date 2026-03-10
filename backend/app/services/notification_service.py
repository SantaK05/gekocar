from twilio.rest import Client # type: ignore
from twilio.base.exceptions import TwilioRestException # type: ignore
import logging

from app.core.config import settings

logger = logging.getLogger(__name__)


class NotificationService:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.admin_phone = settings.ADMIN_PHONE_NUMBER
        self.from_number = settings.TWILIO_FROM_NUMBER
        self.whatsapp_from = settings.TWILIO_WHATSAPP_FROM

    def _send_sms(self, message: str) -> bool:
        try:
            self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=self.admin_phone,
            )
            logger.info(f"SMS inviato a {self.admin_phone}")
            return True
        except TwilioRestException as e:
            logger.error(f"Errore invio SMS: {e}")
            return False

    def _send_whatsapp(self, message: str) -> bool:
        try:
            self.client.messages.create(
                body=message,
                from_=self.whatsapp_from,
                to=f"whatsapp:{self.admin_phone}",
            )
            logger.info(f"WhatsApp inviato a {self.admin_phone}")
            return True
        except TwilioRestException as e:
            logger.error(f"Errore invio WhatsApp: {e}")
            return False

    def notify_new_booking(self, customer_name: str, date: str, service: str) -> bool:
        message = (
            f"🔧 Nuova prenotazione!\n"
            f"Cliente: {customer_name}\n"
            f"Servizio: {service}\n"
            f"Data: {date}\n"
            f"Accedi al pannello per confermare."
        )
        return self._send_whatsapp(message)

    def notify_new_contact(self, customer_name: str, subject: str) -> bool:
        message = (
            f"✉️ Nuovo messaggio!\n"
            f"Da: {customer_name}\n"
            f"Oggetto: {subject}\n"
            f"Accedi al pannello per leggere."
        )
        return self._send_whatsapp(message)


notification_service = NotificationService()