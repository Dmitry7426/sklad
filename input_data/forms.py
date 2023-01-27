import regex as regex
from django import forms
from django.core.validators import validate_slug, validate_unicode_slug, RegexValidator
import re

# Форма типов оборудования
class EquipmentsForm(forms.Form):
    name = forms.CharField(label="Тип оборудования:")

# форма бренды
class BrandsForm(forms.Form):
    name = forms.CharField(label="Бренд:")

# форма модели
class ModelsForm(forms.Form):
    name = forms.CharField(label="Модель")

# форма для шаблона с вкладками
class TabForm(forms.Form):
    name = forms.CharField(label='Введите данные')

# форма заполнения Фамилии, имени, отчества сотрудников
class UserForm(forms.Form):
    UserName = forms.CharField(label='Имя', validators=[RegexValidator(r'[0-9]', message='Wrong')])
    MidlName = forms.CharField(label='Отчество')
    SurName = forms.CharField(label='Фамилия')
    Position = forms.CharField(label='Должность')
    Units = forms.CharField(label='Подразделение')

# форма для удаления пользователя из справочника
class UserDeleteForm(forms.Form):
    UserName = forms.CharField(label='Имя')
    MidlName = forms.CharField(label='Отчество')
    SurName = forms.CharField(label='Фамилия')














class FormList(forms.Form):
    lst = forms.ChoiceField()


