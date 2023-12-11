from datetime import datetime, timedelta

ORDERS_DATA = [
    {
        'order_button': 'order_top_btn',
        'logo_button': 'main_img',
        'name': 'Вася',
        'surname': 'Пупкин',
        'address': 'Красная площадь 1',
        'station': 'Охотный ряд',
        'phone': '+79208888888',
        'date': (datetime.now().date() + timedelta(days=1)).strftime('%d.%m.%Y'),
        'term': 'сутки',
        'color': 'чёрный жемчуг',
        'comment': 'позвонить в домофон'
    },
    {
        'order_button': 'order_bottom_btn',
        'logo_button': 'ya_img',
        'name': 'Маша',
        'surname': 'Пупкина',
        'address': 'Красная площадь 2',
        'station': 'Театральная',
        'phone': '+79208888889',
        'date': (datetime.now().date() + timedelta(days=2)).strftime('%d.%m.%Y'),
        'term': 'трое суток',
        'color': 'серая безысходность',
        'comment': 'позвонить на телефон'
    }
]
