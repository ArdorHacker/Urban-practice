url_var = ["ru", "com", "net"]

def send_email(message, recipent, sender="university.help@gmail.com"):
    chek_at_recipent = str(recipent).split("@")
    chek_at_sender = str(sender).split("@")
    
    if (len(chek_at_recipent) == 1 or len(chek_at_sender) == 1):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipent}")
        return
    
    else:
        chek_url_recipent = chek_at_recipent[1].split(".")
        chek_url_sender = chek_at_sender[1].split(".")
        
        if (len(chek_url_recipent) == 1 or len(chek_url_sender) == 1):
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipent}")
            return
        
        else:
            if (chek_url_recipent[1] in url_var) and (chek_url_sender[1] in url_var):           
                if recipent == sender:
                    print("Нельзя отправить письмо самому себе!")
                    return
            
                elif sender != "university.help@gmail.com":
                    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipent}")
                    return
                
                else:
                    print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipent}")
                    return
                
            else: 
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipent}")
                return
                    
    
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')