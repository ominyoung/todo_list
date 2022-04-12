from django.views.generic import TemplateView


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'