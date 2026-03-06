from typing import Any

from django.core.cache import cache
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Project


# Декоратор @receiver связывает эту функцию с сигналом m2m_changed.
# Сигнал срабатывает, когда меняется поле ManyToMany (в данном случае Project.users).
@receiver(m2m_changed, sender=Project.users.through)
def invalidate_user_projects_cache(
        sender, instance, action: str, pk_set: set[int], **kwargs: Any
) -> None:
    # Выводим сообщение в консоль для отладки, что сигнал сработал
    print("Сигнал 'invalidate_user_projects_cache' викликаний")

    # Проверяем тип действия. Сигнал m2m_changed срабатывает 6 раз (до и после каждого действия).
    # Мы реагируем только на завершенные действия: добавление (post_add),
    # удаление (post_remove) или полную очистку связей (post_clear).
    if action not in {"post_add", "post_remove", "post_clear"}:
        return

    # pk_set — это набор (set) ID пользователей, которые были добавлены или удалены.
    # Мы перебираем эти ID, чтобы удалить устаревший кеш именно для этих пользователей.
    # "or []" добавлено для безопасности, если pk_set окажется None.
    for user_id in pk_set or []:
        # Формируем тот же самый ключ кеша, который использовался во view-функции
        cache_key = f"user:{user_id}:project"

        # Удаляем запись из кеша.
        # При следующем запросе функция get_users_projects не найдет данные в кеше
        # и загрузит свежие данные из базы.
        cache.delete(cache_key)
