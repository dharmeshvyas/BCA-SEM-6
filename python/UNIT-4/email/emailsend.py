import smtplib,ssl

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "parmarchandu7058@gmail.com"
        self.password = ""
    def send(self,emails,subject,content):
        ssl_contex =ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name,self.port,context=ssl_contex)
        service.login(self.sender_mail,self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail,email,f"Subject :{subject}\n{content}")
            service.quit()

mails = input("enter emails :").split()
subject = input("Enter Subject :")
Content = input("Enter Content :")
mail = Mail()
mail.send(mails,subject,Content)