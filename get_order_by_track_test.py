# Анастасия Затоковенко, 11-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


# Тест: Код ответа равен 200
def test_get_order_by_track_success():
    track = sender_stand_request.post_new_order(data.order_body).json()["track"]
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200
