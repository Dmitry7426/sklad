from django import forms


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


# форма подразделение
class UnitForm(forms.Form):
    name = forms.CharField(label='Наименование подразделения')


# форма должности
class PositionForm(forms.Form):
    name = forms.CharField(label='Наименование должности')


# форма для шаблона с вкладками
class TabForm(forms.Form):
    name = forms.CharField(label='Введите данные')


# форма заполнения Фамилии, имени, отчества сотрудников
class UserForm(forms.Form):
    UserName = forms.CharField(label='Имя')
    MidlName = forms.CharField(label='Отчество')
    SurName = forms.CharField(label='Фамилия')


# форма для удаления пользователя из справочника
class UserDeleteForm(forms.Form):
    UserName = forms.CharField(label='Имя')
    MidlName = forms.CharField(label='Отчество')
    SurName = forms.CharField(label='Фамилия')


# форма для регистрации нового облорудования
class EquipmentAddForm(forms.Form):
    inv = forms.CharField(label='Инвентарный номер')
    netname = forms.CharField(label='Сетевое имя', required=False)


# форма привязки оборудования к пользователю
class EquipmentsLinkUsers(forms.Form):
    InvNum = forms.CharField(label='Инвентарный номер', required=False)
    User = forms.CharField(label='Пользователь', required=False)


# форма заполнения конфигурации ПК
class ConfigComputer(forms.Form):
    OperateSystem = forms.CharField(label='Операционная система', required=False)
    Activate = forms.CharField(label='Статус активации системы', required=False)
    CurrentUser = forms.CharField(label='Текущий пользователь', required=False)
    IPAddress = forms.CharField(label='IP адрес', required=True)
    MAC = forms.CharField(label='МАС адрес', required=False)
    SystemName = forms.CharField(label='Имя ПК', required=False)
    LANSpeed = forms.CharField(label='Скорость сети', required=False)
    HDD = forms.CharField(label='HDD', required=False)
    Mboard = forms.CharField(label='Системная плата', required=False)
    ProcessorName = forms.CharField(label='Процессор', required=False)
    Soccet = forms.CharField(label='Соккет', required=False)
    OZU = forms.CharField(label='ОЗУ', required=False)
    PrinterTypeConnect = forms.CharField(label='Тип подключения принтера', required=False)
    InstalledSoft = forms.CharField(label='Софт', required=False)


class FormList(forms.Form):
    lst = forms.ChoiceField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, label='Описание файла')
    file = forms.FileField(label='Выберите файл')
