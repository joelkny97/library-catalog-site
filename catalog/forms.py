import datetime
from django import forms
from django.forms import ModelForm
from catalog.models import BookInstance

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
#
#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
#
#         #Check if date entered in from is not in past nor more than 3 weeks from current date
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#
#         if data > datetime.date.today()+datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#         #return cleaned data
#         return data

class RenewReturnBookModelForm(ModelForm):

    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Check if date entered in from is not in past nor more than 3 weeks from current date
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # return cleaned data
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back', 'status']
        labels = {
            'due_back': _('New due date'),
            'status': _('Mark as returned'),
        }
        help_texts = {
            'due_back': _('Enter a date between now and 4 weeks (default 3).'),
            'status': _('Change status of book to Available to mark returned'),
        }
