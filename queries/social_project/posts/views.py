from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, redirect

from forms.django_forms_example.posts.forms import Category, PostForm
from forms.django_forms_example.posts.models import Category, Post, Profile, Tag, Comment

from django.db.models import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post
from django.http.response import JsonResponse  # Django клас для повернення відповіді у форматі JSON.
from django.urls import reverse_lazy, reverse  # Функція Django для отримання URL за іменем маршруту.
from django.views.decorators.http import (require_POST,
                                          require_safe)
# Декоратор для view, який дозволяє обробляти лише POST-запити.
# декоратор, який дозволяє тільки "безпечні" методи: GET і HEAD.
from django.views.generic  import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView)
from django.contrib.auth.mixins import LoginRequiredMixin #класс додае додаткови можливости,
# перевиряе чи авторизрвани ми чи ни, якщо ні то не дае дуступ к постам
from django.http import HttpRequest, JsonResponse

# типи ответов
def debug_api(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        data={
            'method': request.method,
            # Преобразуем заголовки в стандартный словарь Python (dict),
            # чтобы була корректная JSON-сериализацию через JsonResponse.
            'headers': dict(request.headers.items()),
            'params': request.GET,
            'body': request.POST,
            'cookies': request.COOKIES,
            'user': str(request.user)
        }
    )


# =============================================================================
# ЗАМЕТКА: JSON-сериализация
# -----------------------------------------------------------------------------
# Процесс преобразования структурированных данных (объектов, словарей Python)
# в УНИВЕРСАЛЬНЫЙ ТЕКСТОВЫЙ ФОРМАТ JSON.
#
# Зачем:
# 1. Для передачи данных по сети (API-запросы).
# 2. Для сохранения данных в текстовые файлы.
#
# Суть: "Упаковка" сложных данных в простой текст для транспортировки/хранения.
# =============================================================================
@login_required(login_url=reverse_lazy('auth_user'))
# Декоратор, який перевіряє, чи користувач увійшов у систему.
# Якщо ні → перенаправляє на сторінку логіну (auth_user).
def post_create(
        request: HttpRequest,
) -> HttpResponseRedirect | HttpResponse:
    form = PostForm(request.POST)

    if form.is_valid():  # Перевіряє дані форми.
        post = form.save(commit=False)  # commit=False — створює об’єкт, але ще не зберігає його в базі.
        post.author = request.user  # Додає автора
        post.save()  # Зберігає пост у базі і зв’язки ManyToMany
        form.save_m2m()
        return redirect('post_list')

    return render(request, 'posts/post_form.html', context={"form": form})


# Якщо форма не валідна або GET-запит → показує форму для створення поста.
# если юзар не зареган то он будет анонимом



# 1. LoginRequiredMixin: Вимагає, щоб користувач був залогінений.
#    Неавторизованих перенаправляє на 'auth_user'.
# 2. ListView: Базовий клас Django для відображення списку об'єктів моделі.
class PostListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.select_related('author').prefetch_related('categories')
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('auth_user')




    """
    Представление для отображения деталей одного конкретного поста. 
    Использует встроенный класс DetailView от Django.
    """
class PostDetailView(DetailView):
    model = Post
    """
       [model] Указывает Django, с какой моделью базы данных мы работаем. 
       DetailView автоматически попытается найти объект этой модели, 
       используя часть URL (обычно PK или Slug).
       """
#temtlates можно подивитися POst
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'


"""
Представление для создания нового поста через форму.
Использует встроенный класс CreateView от Django.
"""
class PostCreateView(CreateView):
    template_name = 'posts/post_form.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  #



#def post_list(requset: HttpRequest) -> HttpResponse:
# #Використовуємо select_related та prefetch_related
 #   posts = Post.objects.select_related('author').prefetch_related('categories')

    # дістане всі пости, а також пов'язані з ними дані авторів та категорій

    # select_related('author') - це робота із зв'язками один-до-багатьох (ForeignKey, OneToOneField).
    # Завантажує дані автора (author) разом із постом в ОДНОМУ запиті до БД.Лёха сказал ORM

    # prefetch_related('categories') - Завантажує всі категорії (ManyToMany M2M),
    # що повʼязані з постом. Лёха сказал ORM
  #  return render(requset, 'posts/post_list.html', context={'posts': posts})



#  створює новий пост: бере дані з форми, прив’язує автора, зберігає в базу і повертає користувача на список постів.


# УДАЛяЕТ post
def post_remove(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)  # или находит (post) жто ошбвка 404
    post.delete()
    return redirect('post_list')


def category_list(requset: HttpRequest) -> HttpResponse:
    categories = Post.objects.all()
    return render(
        requset, 'posts/category.html', context={'categories': categories}
    )


# додавати

def post_add_category(_: HttpRequest, post_id: int,
                      category_id: int):  # _ - якщо мы не використовуемо зміну то просто _
    post = get_object_or_404(Post, pk=post_id)
    category = get_object_or_404(Category, pk=category_id)

    post.categories.add(category)
    return redirect('post_list')


def post_update(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_form.html', context={'form': form})


# прибрати катигории
def post_remove_category(_: HttpRequest, post_id: int,
                         category_id: int):  # _ - якщо мы не використовуемо зміну то просто _
    post = get_object_or_404(Post, pk=post_id)
    category = get_object_or_404(Category, pk=category_id)

    post.categories.remove(category)
    return redirect('post_list')


def category_update(request: HttpRequest, pk: int) -> HttpResponseRedirect | HttpResponse:
    """Оновити категорію."""
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = Category(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = Category(instance=category)

    return render(request, "posts/category_form.html", {"form": form})


@login_required(login_url=reverse_lazy('auth_user'))
 #@login_required: Вимагає аутентифікації користувача. Неавторизованих
#    перенаправляє на сторінку входу ('auth_user').
def category_create(request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
    """Створити категорію."""
    form = Category(request.POST)
    if form.is_valid():
        form.save()
        return redirect("category_list")

    return render(request, "posts/category_form.html", {"form": form})


@require_POST
def category_remove(_: HttpRequest, pk: int) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    """Видалити категорію."""
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("category_list")


def category_get_or_create(request: HttpRequest):
    category, created = Category.objects.get_or_create(
        title='Default category',
        defaults={'description': 'Auto created!'}
    )
    # либо достает (get), либо создает (create)

    return render(request, 'post/get_or_create_result.html', context={'category': category, 'created': created})


def category_update_or_create(request: HttpRequest) -> HttpResponse:
    """Оновити або створити категорію, якщо не існує."""
    category, created = Category.objects.update_or_create(
        title="Tutorial", defaults={"description": "Updated or created"}
    )
    return render(
        request,
        "posts/get_or_create_result.html",
        {"category": category, "created": created},
    )


# domashka


def profile_view(request: HttpRequest) -> HttpResponse:
    profile = get_object_or_404(Profile, User=request.user)
    context = {'profile': profile}
    return render(request, 'profile.html', context=context)


def comment_view(request: HttpRequest, post_id: int) -> HttpResponse:
    if request.method == "POST":
        text = request.POST.get('text')
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment.objects.create(post=post, author=request.user.profile, text=text)
        return redirect('post_detail', pk=post.id)

    return redirect('post_detail', pk=post_id)

def tags(request: HttpRequest) -> HttpResponse:
    PostsByTagView = ListView
    model = Post
    template_name = 'posts/posts_by_tag.html'