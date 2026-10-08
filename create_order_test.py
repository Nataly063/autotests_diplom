# Хорина Наталья, 48-я когорта - Финальный проект. Инженер по тестированию плюс 
import sender_stand_request


# Функция для позитивной проверки получения заказа по треку заказа
def test_create_order_and_get_by_track():

    # запрос на создание заказа
    create_response = sender_stand_request.post_new_order()
        
    # проверка успешного сохранения трека заказа
    track_number = create_response.json()["track"]
   
    # запрос на получение заказа по номеру трека
    get_response = sender_stand_request.get_order_by_track(track_number)

    # проверка кода ответа 200
    assert get_response.status_code == 200
