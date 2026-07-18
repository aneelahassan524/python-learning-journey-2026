class Email:

    def send(self):
        print("Email Notification: Message sent successfully.")

class SMS:

    def send(self):
        print("SMS Notification: Message sent successfully.")

class WhatsApp:

    def send(self):
        print("WhatsApp Notification: Message sent successfully.")

def send_notification(service):
          service.send()

email = Email()
sms = SMS()
whatsApp = WhatsApp()
send_notification(email)
send_notification(sms)
send_notification(whatsApp)