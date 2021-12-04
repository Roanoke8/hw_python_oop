class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    # 1 Шаг 0.65 метра.
    # 1 Гребок 1.13 метра
    LEN_STEP = 0.65
    M_IN_KM = 1000

    dst: float = 0
    spd: float = 0

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
            self.action = action
            # колличество действий
            self.duration = duration
            # длительность тренировки
            self.weight = weight 
            # Вес спортсмена

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        result = self.action * self.LEN_STEP / self.M_IN_KM
        return result
        
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        result = distance / self.duration
        return result

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        self.speed = 0
        
    def get_distance(self) -> float:
        print('RUN Дистанция в КМ.', super().get_distance())
        return super().get_distance()

    def get_mean_speed(self) -> float:
        self.speed = super().get_mean_speed()
        print('RUN Cредняя скорость движения', self.speed)

        return super().get_mean_speed()
        
    def get_spent_calories(self) -> float:
        # (18 * средняя_скорость – 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        speed = self.get_mean_speed()
        h_to_m = self.duration * 60 # Переводит в минуты
        
        callories = (coeff_calorie_1 * speed - coeff_calorie_2) * \
            self.weight / self.M_IN_KM * h_to_m
        print('Каллории', callories)
        return callories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()
        
    def get_spent_calories(self) -> float:
        return super().get_spent_calories()

    pass


class Swimming(Training):
    """Тренировка: плавание."""
    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()
        
    def get_spent_calories(self) -> float:
        return super().get_spent_calories()

    pass

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'RUN':
        run = Running(data[0], data[1], data[2])
        run.get_distance()
        run.get_mean_speed()
        run.get_spent_calories()

def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        # ('RUN', [15000, 1, 75]),
        ('RUN', [9000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
