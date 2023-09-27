# from .models import *
from my_app.models import Snippet
from django.forms import ModelForm

# under Scrutiny
class MyForm(ModelForm):
# class MyForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields='__all__'

    def clean(self):
        super(MyForm, self).clean()
        firstname=self.cleaned_data.get('firstname')
        lastname=self.cleaned_data.get('lastname')
        # gender=self.cleaned_data.get('gender')

        if len(firstname)<5:
            self._errors['firstname']=self.error_class(
                ['minimum of 5 characters required'])
        if len(lastname)<5:
            self._errors['lastname']=self.error_class(
                ['minimum of 5 characters required'])
        # if len(gender)<5:
        #     self._errors['gender']=self.error_class(
        #         ['minimum of 5 characters required'])
        return self.cleaned_data