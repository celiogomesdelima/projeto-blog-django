from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

PER_PAGE = 9

# Create your views here.
# def index(request):
#     posts = Post.objects.get_published()  # type: ignore
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(
#         request,
#         "blog/pages/index.html",
#         {"page_obj": page_obj, "page_title": "Home - "},
#     )
class PostListView(ListView):
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published() #type:ignore

    # def get_queryset(self) -> QuerySet[Any]:
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published = True)
    #     return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Home - ',
        })
        return context


# def post(request, slug):
#     post_obj = Post.objects.get_published().filter(slug=slug).first()  # type: ignore
#     if post_obj is None:
#         raise Http404()
#     page_title = f"{post_obj.title} - Post - "
#     return render(
#         request, "blog/pages/post.html", {"post": post_obj, "page_title": page_title}
#     )
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        post = self.get_object()
        page_title = f'{post.title} - Post - ' #type:ignore
        ctx.update({
            'page_title':page_title
        })
        return ctx
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published = True)

# def page(request, slug):
#     page_obj = Page.objects.filter(is_published=True).filter(slug=slug).first()  # type: ignore
#     if page_obj is None:
#         raise Http404
#     page_title = f"{page_obj.title} - Page - "
#     return render(
#         request, "blog/pages/page.html", {"page": page_obj, "page_title": page_title}
#     )

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        page = self.get_object()
        page_title = f'{page.title} - Página - ' #type:ignore
        ctx.update({
            'page_title':page_title
        })
        return ctx
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published = True)


# def created_by(request, author_pk):
#     user = User.objects.filter(pk=author_pk).first()

#     if user is None:
#         raise Http404()

#     user_full_name = user.username

#     if user.first_name:
#         user_full_name = f"{user.first_name} {user.last_name}"

#     page_title = "Posts de " + user_full_name + " - "
#     posts = Post.objects.get_published().filter(created_by__pk=author_pk)  # type: ignore
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(
#         request,
#         "blog/pages/index.html",
#         {"page_obj": page_obj, "page_title": page_title},
#     )

class CreatedByListView(PostListView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        author_pk = self.kwargs.get('author_pk')
        user = User.objects.filter(pk=author_pk).first()
        if user is None:
            raise Http404()
        
        user_full_name = user.username

        if user.first_name:
            user_full_name = f"{user.first_name} {user.last_name}"
        
        page_title = 'Post de ' + user_full_name + ' - '

        ctx.update({
            'page_title': page_title
        })

        return ctx
    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.filter(created_by__pk = self.kwargs.get('author_pk'))
        return qs

# def category(request, slug):
#     posts = Post.objects.get_published().filter(category__slug=slug)  # type: ignore
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     if len(page_obj) == 0:
#         raise Http404()
#     page_title = f"{page_obj[0].category.name} - "
#     return render(
#         request,
#         "blog/pages/index.html",
#         {"page_obj": page_obj, "page_title": page_title},
#     )

class CategoryListView(PostListView):
    allow_empty = False
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(
            category__slug = self.kwargs.get('slug')
        )
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        page_title = f"{self.object_list[0].category.name} - " #type: ignore
        ctx.update({
            'page_title': page_title,
        })
        return ctx

# def tag(request, slug):
#     posts = Post.objects.get_published().filter(tags__slug=slug)  # type: ignore
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     if len(page_obj) == 0:
#         raise Http404()
#     page_title = f"{page_obj[0].tags.first().name} - "
#     return render(
#         request,
#         "blog/pages/index.html",
#         {"page_obj": page_obj, "page_title": page_title},
#     )
class TagListView(PostListView):
    allow_empty = False
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(
            tags__slug = self.kwargs.get('slug')
        )
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        page_title = f"{self.object_list[0].tags.first().name} - " #type: ignore
        ctx.update({
            'page_title': page_title,
        })
        return ctx

# def search(request):
#     search_value = request.GET.get("search", "").strip()
#     posts = Post.objects.get_published().filter(  # type: ignore
#         Q(title__icontains=search_value)
#         | Q(content__icontains=search_value)
#         | Q(excerpt__icontains=search_value)
#     )
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     page_title = f"{search_value[:30]} - Search - "

#     return render(
#         request,
#         "blog/pages/index.html",
#         {"page_obj": page_obj, "search_value": search_value, "page_title": page_title},
#     )

class SearchListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._search_value = ''

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self._search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        search_value = self._search_value
        return super().get_queryset().filter(
            Q(title__icontains=search_value)
          | Q(content__icontains=search_value)
          | Q(excerpt__icontains=search_value)
        )
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title':f'{self._search_value[:30]} - Search - ',
            'search_value':self._search_value,
        })
        return ctx
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self._search_value == '':
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)