from django.forms import ModelForm, Form, CharField, PasswordInput

from apps.ish.models import Client, Saw, Edge, AddEdge


class ClientCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if str(field) != "is_active":
                self.fields[field].widget.attrs.update(
                    {"class": "form-control", "placeholder": f"Enter the {str(field)}"}
                )

    class Meta:
        model = Client
        fields = ("name", "metr", "color_id", "edge_id")


class ClientSawCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if str(field) != "is_active":
                self.fields[field].widget.attrs.update(
                    {"class": "form-control", "placeholder": f"Enter the {str(field)}"}
                )

    class Meta:
        model = Saw
        fields = ("name", "list_list", "color_id", "laminate", 'price')


