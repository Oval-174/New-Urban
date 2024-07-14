# m5-hw5-r.py "Свой YouTube"
import time
import bcrypt


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.set_password(password)
        self.age = age

    @staticmethod
    def set_password(new_password):
        # converting password to array of bytes
        bytes_pass = new_password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        # Hashing the password
        hash_pass = bcrypt.hashpw(bytes_pass, salt)
        return hash_pass


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        if self.time_now < self.duration:
            print(f"Воспроизведение видео '{self.title}' с {self.time_now} секунды")
            self.time_now += 1
        else:
            print("Конец видео")

    def stop(self):
        self.time_now = 0
        print("Видео остановлено")


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == user.set_password(password):
                self.current_user = user
                print(f"Подключен {user.nickname}")
                return
        print("Ошибка подключения")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Зарегистрирован и подключен {nickname}")

    def log_out(self):
        self.current_user = None
        print("Сенс завершен")

    def add(self, *videos):
        for video in videos:
            exists = False
            for v in self.videos:
                if v.title == video.title:
                    exists = True
                    break
            if not exists:
                self.videos.append(video)
#                print(f"Добавлено видео: {video.title}")

    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(f"Просмотр видео: {video.title}")
                video.time_now = 0
                while video.time_now < video.duration:
                    time.sleep(1)  # пауза 1 секунда
                    video.time_now += 1
                    print(f"Время: {video.time_now} секунд")
                print("Видео завершено")
                return
        print(f"Видео '{title}' не найдено")


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
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
