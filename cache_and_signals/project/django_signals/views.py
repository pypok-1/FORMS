from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .models import Project


# Декоратор, який дозволяє доступ до функції лише авторизованим користувачам.
# Якщо користувач не увійшов, його перенаправить на сторінку "login".
@login_required(login_url=reverse_lazy("login"))
def get_users_projects(request: HttpRequest) -> HttpResponse:
    """Показує проєкти користувача. Дані дістаються з кешу."""

    # Отримуємо об'єкт поточного користувача з об'єкта запиту
    user = request.user

    # Формуємо унікальний ключ для кешу (наприклад: "user:1:project")
    # Це дозволяє зберігати окремий список проєктів для кожного користувача
    cache_key = f"user:{user.pk}:project"

    # Намагаємося отримати дані з кешу за створеним ключем
    projects = cache.get(cache_key)

    # Якщо в кеші даних немає (повернувся None)
    if projects is None:
        # Робимо запит до бази даних: шукаємо всі проєкти, де вказаний користувач є учасником
        # Перетворюємо QuerySet у список (list), щоб зберегти готові дані в кеш
        projects = list(Project.objects.filter(users=user))

        # Зберігаємо отриманий список у кеш за нашим ключем для наступних запитів
        cache.set(cache_key, projects)

    # Повертаємо відрендерену HTML-сторінку з переданим списком проєктів
    return render(
        request,
        "django_signals/user_projects.html",
        {"projects": projects},
    )


@login_required(login_url=reverse_lazy("login"))
def add_user_to_project(request: HttpRequest, project_id: int) -> HttpResponse:
    """
    Додає поточного користувача до проєкту.
    Інвалідація кешу проходить не тут, а в сигналі.
    """
    project = get_object_or_404(Project, id=project_id)
    project.users.add(request.user)
    return redirect("user-projects")


@login_required(login_url=reverse_lazy("login"))
def remove_user_from_project(request: HttpRequest, project_id: int) -> HttpResponse:
    """Видаляє користувача з проєкту."""
    project = get_object_or_404(Project, id=project_id)
    project.users.remove(request.user)
    return redirect("user-projects")


@login_required(login_url=reverse_lazy("login"))
def clear_user_projects(request: HttpRequest) -> HttpResponse:
    """Очищає всі m2m-зв'язки користувача."""
    request.user.project.clear()

    return redirect("user-projects")
