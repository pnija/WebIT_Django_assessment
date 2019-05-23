from django import forms
from .models import Client


class ClientAddForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('client_name', 'street_name', 'suburb', 'postcode', 'state', 'client_contact_name', 'email',
                  'phone_number',)

    def clean(self):
        super(ClientAddForm, self).clean()

        client_name = self.cleaned_data.get('client_name')
        street_name = self.cleaned_data.get('street_name')
        suburb = self.cleaned_data.get('suburb')
        postcode = self.cleaned_data.get('postcode')
        state = self.cleaned_data.get('state')
        client_contact_name = self.cleaned_data.get('client_contact_name')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')

        if len(client_name) is None:
            self._errors['client_name'] = self.error_class([
                'client name cannot be empty'])

        if len(email) is None:
            self._errors['email'] = self.error_class([
                'email cannot be empty'])

        if len(phone_number) is None:
            self._errors['phone_number'] = self.error_class([
                'phone number cannot be empty'])

        return self.cleaned_data
