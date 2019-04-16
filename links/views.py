from django.shortcuts import render
# core features
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# http
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
# views
from django.shortcuts import render, get_object_or_404
from django.views import generic
#models
from .models import Link, Category, Review
from .forms import LinkForm, ReviewForm

def home(request):
    return render(request, 'links/home.html')


#### MAIN VIEWS ####

class AllLinks(generic.ListView):
    context_object_name = 'links'
    model = Link

class LinkDetailView(generic.DetailView):
    model = Link


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "links/categories/category_detail.html"

class UserLinkList(generic.ListView):
    model = Link
    template_name = "links/user_linklist.html"
    context_object_name='links'

    def get_queryset(self):
            self.link_author = get_object_or_404(User, username=self.kwargs['username'])
            return Link.objects.filter(user=self.link_author)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['link_author']=self.link_author
        return context


### LINK CRUD ###
class LinkCreate(LoginRequiredMixin, generic.CreateView):
    form_class = LinkForm
    model = Link

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class LinkUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Link
    form_class = LinkForm

class LinkDelete(LoginRequiredMixin, generic.DeleteView):
    model = Link
    success_url = reverse_lazy("links:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Link successfullly deleted")
        return super().delete(*args, **kwargs)



### Review CRUD ###
class ReviewCreate(LoginRequiredMixin, generic.CreateView):
    form_class = ReviewForm
    model = Review

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.link = Link.objects.get(slug=self.kwargs.get('slug'))
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Review
    form_class = ReviewForm

class ReviewDelete(LoginRequiredMixin, generic.DeleteView):
    model = Review
    success_url = reverse_lazy("links:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Review successfullly deleted")
        return super().delete(*args, **kwargs)
