from django.http import HttpRequest, HttpResponse

from django.http import HttpRequest, HttpResponse


def set_cookies(request: HttpRequest) -> HttpResponse:
    # 1. Создаем ответ сервера с простым текстом внутри.
    response = HttpResponse('Cookies set!')

    # 2. ДОБАВЛЯЕМ К ОТВЕТУ ИНСТРУКЦИЮ ДЛЯ БРАУЗЕРА:
    #    "Сохрани куку с именем 'test_key' и значением 'str(request)'".
    #    Кука будет сессионной (удаляется при закрытии браузера), так как нет срока годности.
    response.set_cookie('test_key', str(request))

    return response


# get_cookise - достать кукис
# request.COOKIES — это словарь Python, который содержит все куки, отправленные браузером.
# Метод .get() безопасно извлекает значение по ключу 'test_key'.
# Если куки 'test_key' не существует, переменная 'cookies' получит значение None (или то, что вы укажете как default).
def get_cookies(request: HttpRequest) -> HttpResponse:
    cookies = request.COOKIES.get('test_key')
    return HttpResponse(cookies)


def delete_cookies(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookies DELETE!')
    response.delete_cookie('test_key')
    return response


# request.session ведет себя как обычный словарь Python.
# Мы присваиваем значение 'red' ключу 'color' в данных сессии текущего пользователя.
# Django автоматически сохранит эти данные на сервере (например, в базе данных)
# и отправит пользователю специальную куку с ID сессии, чтобы потом его узнать.
def set_session(request: HttpRequest) -> HttpResponse:
    request.session['color'] = 'red'
    return HttpResponse('Color saved')


def get_session(request: HttpRequest) -> HttpResponse:
    color = request.session.get('color', 'unknown')
    return HttpResponse(f'color is {color}')


# УДАЛАЕТ ВСЕ СЕССИИ
def clear_session(request: HttpRequest) -> HttpResponse:
    # Повне видалення даних сесії та кукі (аналог Logout)
    request.session.flush()
    return HttpResponse('Session Flushed!')


def update_session(request: HttpRequest) -> HttpResponse:
    # Запис значень у сесію (зберігаються на сервері)
    request.session['points'] = 100
    request.session['color'] = 'blue'
    return HttpResponse('Updated!')
#Зберігає значення 100 та 'blue' у сховище сесій на сервері, прив’язуючи їх до конкретного користувача.


#======================DZ=========================================
def visit_counter(request: HttpRequest) -> HttpResponse:
    country = request.session.get('visit_count', 0)
    count = country + 1
    request.session['visit_count'] = count

    return HttpResponse(f'You have visited {count}')
