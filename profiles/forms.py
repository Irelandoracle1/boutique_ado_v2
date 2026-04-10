from django import forms
from .models import UserProfile
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

        # 🔥 FIX: force proper country widget (prevents BlankChoiceIterator crash)
        widgets = {
            'default_country': CountrySelectWidget(),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes, remove labels,
        set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # autofocus first field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # skip country field (handled by widget above)
            if field != 'default_country':

                if self.fields[field].required:
                    placeholder = f"{placeholders.get(field, field)} *"
                else:
                    placeholder = placeholders.get(field, field)

                self.fields[field].widget.attrs['placeholder'] = placeholder

            # common styling for all fields
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input'
            )

            # remove labels
            self.fields[field].label = False