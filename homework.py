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
        self.duration = duration
        self.weight = weight

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
        
    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        speed = self.get_mean_speed()
        h_in_m = self.duration * 60
        callories = (coeff_calorie_1 * speed - coeff_calorie_2) * \
            self.weight / self.M_IN_KM * h_in_m
        print('Каллории', callories)
        return callories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float,
                 weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()
        
    def get_spent_calories(self) -> float:
        speed = self.get_mean_speed()
        h_in_m = self.duration * 60
        weight = self.weight
        height = self.height
        callories: float = (0.035 * weight + (speed ** 2 // height) * 0.029 * weight) * h_in_m
        return callories

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
        return run
    elif workout_type == 'WLK':
        wlk = SportsWalking(data[0], data[1], data[2], data[3])
        wlk.get_distance()
        wlk.get_mean_speed()
        wlk.get_spent_calories()
        return wlk


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
