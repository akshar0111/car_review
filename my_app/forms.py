from .models import complain
from django.forms import ModelForm

class complainform(ModelForm):
    class Meta:
        model = complain
        fields = '__all__'