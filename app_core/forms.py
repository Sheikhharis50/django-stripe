from django import forms


class ModelForm(forms.ModelForm):
    @property
    def is_update(self):
        return hasattr(self, "instance") and self.instance.pk is not None
