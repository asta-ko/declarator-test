# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Office(MPTTModel):

    parent = TreeForeignKey('self', blank=True, null=True)
    name = models.TextField(verbose_name='полное название')
    sort_order = models.IntegerField(
        default=0, verbose_name='Порядок сортировки')

    def __unicode__(self):
        return self.name

    def get_document_status(self, year=None):
        documents = self.documents
        if year:
            documents = documents.filter(income_year=year)
        if not documents:
            return 'none'
        files = DocumentFile.objects.filter(document__in=documents)
        if not files.exists():
            return 'blank'
        elif files.filter(file='').exists():
            return 'some'
        else:
            docs_with_files_ids = set([x.document.id for x in files])
            all_docs_ids = set(documents.values_list('id', flat=True))
            if docs_with_files_ids != all_docs_ids:
                return 'some'
            else:
                return 'all'


class Document(models.Model):
    office = TreeForeignKey(
        'declarations.Office', verbose_name="орган власти", related_name='documents')
    income_year = models.IntegerField(
        verbose_name="год за который указан доход")

    def __unicode__(self):
        return self.office.name + ' ' + str(self.income_year)


class DocumentFile(models.Model):
    document = models.ForeignKey(
        Document, verbose_name="декларация", related_name='files')
    file = models.FileField(blank=True, max_length=255, null=True,
                            upload_to='media/files/', verbose_name="файл")
