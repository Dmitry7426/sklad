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

# инвентарные номера
class InvNumForm(forms.Form):
    inv = forms.CharField(label='Инвентарный номер')


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


# форма для регистрации нового облорудования
class EquipmentAddForm(forms.Form):
    inv = forms.CharField(label='Инвентарный номер')
    netname = forms.CharField(label='Сетевое имя', required=False)
    # typ = forms.CharField(label='Тип')
    # brand = forms.CharField(label='Бренд')
    # model = forms.CharField(label='Модель')

# форма привязки оборудования к пользователю
class EquipmentsLinkUsers(forms.Form):
    InvNum = forms.CharField(label='Инвентарный номер', required=False)
    # Types_id = forms.CharField(label='Тип')
    # Brand_id = forms.CharField(label='Производитель')
    # Model_id = forms.CharField(label='Модель')
    User = forms.CharField(label='Пользователь', required=False)
    # Hardware_id = forms.CharField(label='Установленный софт')











class FormList(forms.Form):
    lst = forms.ChoiceField()


