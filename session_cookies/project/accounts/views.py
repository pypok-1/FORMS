from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def password_reset_request(request: HttpRequest) -> HttpResponse:
    # Перевірка: чи користувач надіслав форму (POST), чи просто відкрив сторінку (GET)
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            #Це отримання чистого Email(чистил от пробелов ). Код бере введену пошту, яку Django вже перевірив на правильність формату, щоб далі знайти юзера в базі.
            # Пошук користувача в БД за поштою
            user = User.objects.filter(email=email).first() #один (первый) объект

            if user is not None:
                # Дані для створення унікального посилання на скидання пароля
                context = {
                    'email': email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Website',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),   # ID юзера в Base64
                    # Це закодований ID користувача. Перетворює цифру ID на безпечний для посилань текст,
                    # щоб сервер знав, кому саме ми скидаємо пароль.
                    'token': default_token_generator.make_token(user),  # Тимчасовий токен
                    'protocol': 'http'
                }
                # Надсилання листа з використанням вказаних шаблонів
                form.send_mail(
                    subject_template_name="accounts/registration/password_reset_subject.txt",
                    email_template_name="accounts/registration/password_reset_email.txt",
                    context=context,
                    from_email="admin@mysite.com",
                    to_email=user.email,
                    html_email_template_name="accounts/registration/password_reset_email.html",
                )
                # Перенаправлення на сторінку "Лист відправлено"
                return redirect(reverse('password_reset_done'))
    else:
        # Якщо GET-запит — створюємо порожню форму
        form = PasswordResetForm()

    return render(
        request,
        template_name='accounts/registration/password_reset.html',
        # Передача об'єкта форми в шаблон (виправлено синтаксис словника)
        context={'password_reset_form': form}
    )


