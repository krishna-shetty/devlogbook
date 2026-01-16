from collections import defaultdict
from django.views.generic import ListView, DetailView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapters = defaultdict(list)

        for entry in self.get_queryset().order_by('order'):
            chapters[entry.get_chapter_display()].append(entry)

        context['grouped_entries'] = dict(chapters)
        return context

class EntryView(DetailView):
    model = Entry
    template_name = 'entry_details.html'