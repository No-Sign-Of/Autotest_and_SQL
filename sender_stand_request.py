import configuration
import requests
import data


# Функция для отправления запроса на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)


track = post_new_order(data.order_body).json()["track"]


# Функция на отправление запроса на получение заказа по номеру
def get_order_by_track():
    params_get_order = data.params.copy()
    params_get_order["t"] = track
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params=params_get_order)


response_get_order = get_order_by_track()
