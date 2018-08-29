from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Person

class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'email', 'is_active']
    success_url = '/core/person/list'
    # template_name = 'base_form.html


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

class PersonList(LoginRequiredMixin, ListView):
    model = Person
    context_object_name = 'pessoas'
    login_url = '/core/login'

    def get_context_data(self, *args, **kw):
        result = super().get_context_data(*args, **kw)
        result['test_dict'] = {
            'foo': 'Bar'
        }
        result['counter'] = Counter()
        result['collumns'] = (
            ('Nome', 'name'),
            ('E-mail', 'email'),
            ('Ativo', 'is_active'),
        )
        return result


class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'email', 'is_active']
    success_url = '/core/person/list'


class PersonDelete(DeleteView):
    model = Person
    success_url = '/core/person/list'
    