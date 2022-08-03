from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


context_info = [
    {
        "id": "0001",
        "name": "Artur",
        "mail": "example@gmail.com",
        "discount_card": "13722",
        "age": "23",
        "city": "Kharkiv",
        "image": "https://sokol-larkin.com/wp-content/uploads/2021/06/placeholder-image.jpg"
    }
]

context = [
    {
        "name": "Macbook M1 2020",
        "image": "https://appleinsider.ru/wp-content/uploads/2020/11/macbookair_ssd_main.jpg",
        "description": "The lightest and thinnest laptop manufactured by Apple MacBook Air 13 M1 256Gb 2020. "
                       "It has been completely transformed, it has become even more powerful, "
                       "thanks to increased endurance and CPU performance. "
                       "Now its speed is 3.5 times faster, and machine learning has increased by as much as 9 times. "
                       "Without charging, the MacBook functions longer than its predecessors. "
                       "And even under heavy loads, it does not make unnecessary noise, "
                       "because there is no fan in its design. "
                       "Notebook Apple MacBook Air 13 M1 256Gb 2020 – power has never been so compact and thin!",
        "slug": "laptop"

    }, {
        "name": "Canon EOS20000",
        "image": "https://www.trustedreviews.com/wp-content/uploads/sites/54/2018/06/canon_eos_2000d_01.jpg",
        "description": "Create with ease the clarity of the signs from the clarity, like from a digital reflex camera,"
                       "that video cinematic clarity in Full HD format, inspire the minds of weak lighting,"
                       "with the help of the 24.1-megapixel EOS 2000D."
                       "Contribute Wi-Fi, "
                       "NFC and Canon Connect software for remote capture and wireless content transfer."
                       "Try photos with a 24.1-megapixel sensor, "
                       "which is 19 times larger than the sensor of a great smartphone,"
                       "and allows you to capture frames with an effective background, navigating for low light.",
        "slug": "camera"
    }, {
        "name": "MiTV 43'",
        "image": "https://mobile-review.com/all/wp-content/uploads/2021/08/5-28.jpg",
        "description": "The era of smart TVThe Mi TV P1 impresses with its harmoniously thought-out appearance with "
                       "thin bezels and stylish stands, innovative functionality, and a friendly Android TV interface."
                       "The model has a remote control connected via Bluetooth, "
                       "and a lot of ports for creating a network of devices."
                       "Access to online cinemas opens up almost limitless possibilities for the user."
                       "Now TV is not only about watching, but also about exciting leisure time for the whole family."
                       "Erase BezelsThe design of the display provides for a minimal frame",
        "slug": "tv"

    }
]


def homepage(request: HttpRequest) -> render:
    return render(request, 'homepage.html')


def client_page(request: HttpRequest, id: str) -> render:
    for name in context_info:
        if name["id"] == id:
            return render(request, 'client_page.html', name)


def basket(request: HttpRequest) -> render:
    return HttpResponse('Basket')


def product_all(request: HttpRequest, item_name: str) -> render:
    for name in context:
        if name["slug"] == item_name:
            return render(request, 'product_all.html', name)