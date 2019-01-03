from django.db import models
from django.conf import settings

# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_createdby',
        editable=False, null=True, blank=True,
        on_delete=models.SET_NULL
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_modifiedby',
        null=True, blank=True, editable=False,
        on_delete=models.SET_NULL
    )
    is_archive = models.BooleanField(default=False, editable=False)

    def archive(self, user=None):
        update_fields = ['is_archive']

        if user:
            self.modified_by = user
            update_fields.append('modified_by')

        self.is_archive = True
        self.save(update_fields=update_fields)
