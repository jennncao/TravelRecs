from import_export import resources
from .models import Activity

class ActivityResource(resources.ModelResource):
    class Meta:
        model = Activity