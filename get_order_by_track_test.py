# Анастасия Затоковенко, 11-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Тест: Код ответа равен 200
def test_correct_status():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200
