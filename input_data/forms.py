from django import forms


class EquipmentsForm(forms.Form):
    Typ = forms.CharField(label="Тип оборудования")


class FormList(forms.Form):
    lst = forms.ChoiceField()


