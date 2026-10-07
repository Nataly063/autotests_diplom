import requests
import configuration
import data


# Создать заказ
def post_new_order():
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_PATH, 
                         json=data.order_body 
    )

# Получить заказ по треку заказа
def get_order_by_track(track):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_PATH, 
                         params={"t": track}
    )    