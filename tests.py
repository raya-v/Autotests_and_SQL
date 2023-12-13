# Воробьёва Раиса, 11-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


def test():
    # выполняем запрос на создание заказа
    response_create_order = sender_stand_request.create_order(data.create_order_body)

    # сохраняем трек номер заказа
    track = response_create_order.json()["track"]
    print("\nТрек созданного заказа: " + str(track))

    # выполняем запрос на получение заказа по треку
    response_get_order = sender_stand_request.get_order(track)
    print("Код ответа на запрос на получение заказа по треку: " + str(response_get_order.status_code))

    # проверяем что код ответа равен 200
    assert response_get_order.status_code == 200