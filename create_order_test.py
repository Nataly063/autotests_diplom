import configuration
import data
import requests

    # URL для создания заказа
create_order_url = f"{configuration.BASE_URL}/api/v1/orders" 

   # URL для получения заказа
get_order_url = f"{configuration.BASE_URL}/api/v1/orders/track" 
   

# Функция для позитивной проверки получения заказа по треку заказа
def test_create_order_and_get_by_track():

    # запрос на создание заказа
    create_response = requests.post(
        create_order_url,
        json=data.order_body
    )
        
    # проверка успешного сохранения трека заказа
    track_number = create_response.json().get("track")
   
    # запрос на получение заказа по номеру трека
    get_response = requests.get(get_order_url, params={"t":track_number})

    # проверка кода ответа 200
    assert get_response.status_code == 200
