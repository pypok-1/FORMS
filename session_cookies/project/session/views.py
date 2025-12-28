from django.http import HttpRequest, HttpResponse

from django.http import HttpRequest, HttpResponse


def set_cookies(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookies set!')
    response.set_cookie('test_key', str(request))

    return response


def get_cookies(request: HttpRequest) -> HttpResponse:
    cookies = request.COOKIES.get('test_key')
    return HttpResponse(cookies)


def delete_cookies(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookies DELETE!')
    response.delete_cookie('test_key')
    return response


def set_session(request: HttpRequest) -> HttpResponse:
    request.session['color'] = 'red'
    return HttpResponse('Color saved')


def get_session(request: HttpRequest) -> HttpResponse:
    color = request.session.get('color', 'unknown')
    return HttpResponse(f'color is {color}')


# УДАЛАЕТ ВСЕ СЕССИИ
def clear_session(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return HttpResponse('Session Flushed!')


def update_session(request: HttpRequest) -> HttpResponse:
    request.session['points'] = 100
    request.session['color'] = 'blue'
    return HttpResponse('Updated!')


#======================DZ=========================================
def visit_counter(request: HttpRequest) -> HttpResponse:
    visits = request.session.get('visit_count', 0)
    count = visits + 1
    request.session['visit_count'] = count
    return HttpResponse(f'You have visited {count} times')


def reset_visit_counter(request: HttpRequest) -> HttpResponse:
    if 'visit_count' in request.session:
        request.session.pop('visit_count', None)
    return redirect('visit_counter')


