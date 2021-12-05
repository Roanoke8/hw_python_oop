from typing import Dict


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (
            f'Тип тренировки: {self.training_type}; '
            f'Длительность: {self.duration:.3f} ч.; '
            f'Дистанция: {self.distance:.3f} км; '
            f'Ср. скорость: {self.speed:.3f} км/ч; '
            f'Потрачено ккал: {self.calories:.3f}.')
        return message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    dst: float = 0
    spd: float = 0
    inf: Dict[str, float] = {}

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
        training_type = self.__class__.__name__
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        get_message = InfoMessage(training_type,
                                  duration,
                                  distance,
                                  speed,
                                  calories)
        return get_message


class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
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
        callories = ((coeff_calorie_1 * speed - coeff_calorie_2)
                     * self.weight / self.M_IN_KM * h_in_m)
        return callories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
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
        callories: float = (0.035 * weight + (speed ** 2
                            // height) * 0.029 * weight) * h_in_m
        return callories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()

    pass


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        result = (self.length_pool * self.count_pool
                  / self.M_IN_KM / self.duration)
        return result

    def get_spent_calories(self) -> float:
        # (средняя_скорость + 1.1) * 2 * вес
        mean_speed = self.get_mean_speed()
        result = (mean_speed + 1.1) * 2 * self.weight
        return result

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()

    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training = Training(data[0], data[1], data[2])

    if workout_type == 'RUN':
        run = Running(data[0], data[1], data[2])
        run.show_training_info()
        return run
    elif workout_type == 'WLK':
        wlk = SportsWalking(data[0], data[1], data[2], data[3])
        wlk.show_training_info()
        return wlk
    elif workout_type == 'SWM':
        swm = Swimming(data[0], data[1], data[2], data[3], data[4])
        swm.show_training_info()
        return swm
    return training


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())
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
