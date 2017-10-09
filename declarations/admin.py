# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from declarations.models import Office, Document, DocumentFile

admin.site.register(Office, MPTTModelAdmin)
admin.site.register(Document)
admin.site.register(DocumentFile)