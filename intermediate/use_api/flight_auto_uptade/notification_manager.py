from twilio.rest import Client
from environs import Env
import smtplib

env = Env()
env.read_env()# Carrega as variáveis do arquivo .env


class NotificationManager:

    def __init__(self):
        self.smtp_address = env.str("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.email = env.str("MY_EMAIL")
        self.email_password = env.str("MY_EMAIL_PASSWORD")
        self.twilio_virtual_number = env.str("TWILIO_VIRTUAL_NUMBER")
        self.twilio_verified_number = env.str("TWILIO_VERIFIED_NUMBER")
        self.whatsapp_number = env.str("TWILIO_VIRTUAL_NUMBER")
        # Set up Twilio Client and SMTP connection
        self.client = Client(env.str("TWILIO_ACCOUNT_SID"),env.str("TWILIO_AUTH_TOKEN"))
        self.connection = smtplib.SMTP(env.str("EMAIL_PROVIDER_SMTP_ADDRESS"))
    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=env.str("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=env.str("TWILIO_VERIFIED_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{env.str("TWILIO_VIRTUAL_NUMBER")}',
            body=message_body,
            to=f'whatsapp:{env.str("TWILIO_VERIFIED_NUMBER")}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )