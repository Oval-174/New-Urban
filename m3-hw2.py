# m3-hw2.py "Рассылка писем"
def send_email(message, recipient, sender="university.help@gmail.com"):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

