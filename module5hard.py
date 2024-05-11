import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def set_password(self, new_password):
        self.password = new_password


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        if self.time_now < self.duration:
            print(f"Воспроизводится видео '{self.title}' с {self.time_now} секунды")
            self.time_now += 1
        else:
            print("Воспроизведение видео завершено")

    def stop(self):
        self.time_now = 0
        print("Воспроизведение видео остановлено")


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                print(f"Вошел в систему как {user.nickname}")
                return
        print("Ошибка входа")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Зарегистрировался и вошел в систему как {nickname}")

    def log_out(self):
        self.current_user = None
        print("Вышел из системы")

    def add(self, *videos):
        for video in videos:
            exists = False
            for v in self.videos:
                if v.title == video.title:
                    exists = True
                    break
            if not exists:
                self.videos.append(video)
                print(f"Добавлено видео: {video.title}")

    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Просмотр видео: {video.title}")
                video.time_now = 0
                while video.time_now < video.duration:
                    print(f"Время просмотра, секунд: {video.time_now + 1}")
                    time.sleep(1)  # пауза 1 секунда
                    video.time_now += 1
                print("Конец видео")
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
print(getattr(ur.current_user, 'nickname'))

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
