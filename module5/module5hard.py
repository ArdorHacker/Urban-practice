import hashlib
import time
from math import trunc


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = {}        # общий список пользователей
        self.videos = []       # список всех видео
        self.current_user = "" # текущий пользователь

    def log_in(self, nickname, password):
        user = self.users.get(nickname)

        if not user:
           print("Пользователь не найден.")

        if user.password != hashlib.sha256(password.encode()).hexdigest():
            print("Неверный пароль.")

        self.current_user = vars(user)["nickname"]

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует.")
            return

        self.users[nickname] = User(nickname, password, age)
        self.log_in(nickname, password)

    def log_out(self, nickname):
        if nickname not in self.users:
            raise ValueError("Пользователь не найден.")

        self.current_user = None


    def add(self, *args):
        videos_lst = []
        for i in range(len([*args])):
            videos_lst.append(vars([*args][i]))

        self.videos = videos_lst

    def get_videos(self, title):
        videos_lst = []
        for i in range(len(self.videos)):
            if title.lower() in self.videos[i]["title"].lower():
                videos_lst.append(self.videos[i]["title"])

        return videos_lst

    def watch_video(self, title):
        if self.current_user:
            if vars(self.users[self.current_user])["age"] >= 18:
                for i in range(len(self.videos)):
                    if title == self.videos[i]["title"]:
                        for j in range(self.videos[i]["duration"]):
                            if j > j - 1:
                                print(j + 1, end=" ")
                                time.sleep(1)

                            if j == self.videos[i]["duration"] - 1:
                                print("Конец видео")

            else:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            

        else:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')   
