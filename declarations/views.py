# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from declarations.models import Office

class OfficeDetailView(DetailView):

    template_name='office.html'
    model = Office

    def get_context_data(self, **kwargs):
        context = super(OfficeDetailView, self).get_context_data(**kwargs)
        years = range(2009, 2017)
        years.reverse()
        offices = self.object.get_children()
        table = {}
        for office in offices:
            table[office.id] = []
            for year in years:
                status = office.get_document_status(year)
                table[office.id].append(status)
        context['offices'] = self.object.get_children()
        context['years'] = years
        context['table'] = table
        return context
