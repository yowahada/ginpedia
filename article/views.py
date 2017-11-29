from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormMixin
from django.http import Http404
from .models import Page
from .forms import MySearchForm

# Create your views here.
class FormListView(generic.ListView):
	model = Page

	def get(self, request, *args, **kwargs):

		self.form = MySearchForm(self.request.GET)
		self.form.is_valid()

		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if not allow_empty and len(self.object_list) == 0:
			raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

		context = self.get_context_data(object_list=self.object_list, form=self.form)
		return self.render_to_response(context)

	def get_queryset(self):

		if self.queryset is not None:
			queryset = self.queryset
			if isinstance(queryset, QuerySet):
				queryset = queryset.all()
		elif self.model is not None:
			queryset = self.model._default_manager.all()
		else:
			raise ImproperlyConfigured(
				"%(cls)s is missing a QuerySet. Define "
				"%(cls)s.model, %(cls)s.queryset, or override "
				"%(cls)s.get_queryset()." % {
					'cls': self.__class__.__name__
				}
			)

		# ここで、フォームからキーワードを取得しフィルター
		keyword = self.form.cleaned_data['keyword']
		if keyword:
			queryset = queryset.filter(title__icontains=keyword)

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, str):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)

		return queryset

class PageView(FormListView):
	model = Page

class PageDitailView(generic.DetailView):
	model = Page
	slug_field = "title"  # モデルのフィールドの名前
	slug_url_kwarg = "title"  # urls.pyでのキーワードの名前


def blog_list(request):
	posts = Page.objects.filter(
            is_publick=True).reverse()
	return render(request, 'article/blog_list.html',{
		'posts': posts
	})

def blog_article(request, pk):
	posts = get_object_or_404(Page, pk=pk)
	return render(request, 'article/blog_detail.html',{
		'posts':posts
	})