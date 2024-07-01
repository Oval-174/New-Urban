# m3-hw2.py "Рассылка писем"
def send_email(message, recipient, sender = "university.help@gmail.com"):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if message.find('@') == -1 or recipient.find('@') == -1:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email("1","2",1)

