from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from django.views import generic
from .forms import CommentCreateForm
from .models import Post, Category


class ListAndList(generic.ListView):
    model = Post
    template_name = 'app/post_list_and_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class ListAndCreate(generic.ListView, ModelFormMixin):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:list_and_create')  # このビュー自身!
    template_name = 'app/post_list_and_post_create.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DetailAndCreate(ModelFormMixin, generic.DetailView):
    model = Post
    form_class = CommentCreateForm
    template_name = 'app/post_detail_and_comment_create.html'

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('app:detail_and_create', pk=post_pk)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)
