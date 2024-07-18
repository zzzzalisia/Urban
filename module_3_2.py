def send_mail(message_, recipient_, sender_="university.help@gmail.com"):
    if "@" not in sender_ or "@" not in recipient_:
        print("Невозможно отправить письмо с адреса", sender_, "на адрес", recipient_)
    elif '.com' not in sender_ and '.ru' not in sender_ and '.net' not in sender_:
        print("Невозможно отправить письмо с адреса", sender_, "на адрес", recipient_)
    elif '.com' not in recipient_ and '.ru' not in recipient_ and '.net' not in recipient_:
        print("Невозможно отправить письмо с адреса", sender_, "на адрес", recipient_)
    else:
        if recipient_ == sender_:
            print("Нельзя отправить письмо самому себе!")
        elif sender_ == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender_, "на адрес", recipient_)
        elif sender_ != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender_, "на адрес", recipient_)


send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender_='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender_='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender_='urban.teacher@mail.ru')


