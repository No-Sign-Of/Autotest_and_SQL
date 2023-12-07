import configuration
import requests
import data


# Функция на отправление запроса на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)


# Функция на отправление запроса на получение заказа по номеру
def get_order_by_track(track):
    current_params = data.params.copy()
    current_params["t"] = track
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params=current_params)
