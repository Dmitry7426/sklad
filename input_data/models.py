from django.core.validators import validate_slug, RegexValidator
from django.db import models


# Таблица ТипыОборудования
class TypesEquipments(models.Model):
    TypesEq = models.CharField(max_length=100)


# Таблица Бренды
class Brands(models.Model):
    BrandName = models.CharField(max_length=100)


# Таблица Модель
class Models(models.Model):
    ModelName = models.CharField(max_length=100, blank=True)


# Таблица Подразделения
class Unit(models.Model):
    UnitName = models.CharField(max_length=150, blank=True)


# Таблица Должность
class Position(models.Model):
    PositionName = models.CharField(max_length=250, blank=True)


# Таблица Пользователи
class Users(models.Model):
    UserName = models.CharField(max_length=100, validators=[RegexValidator('[0-9]', message='Wrong')])
    MidlName = models.CharField(max_length=100)
    SurName = models.CharField(max_length=100)
    Position = models.ForeignKey(Position, on_delete=models.DO_NOTHING, blank=True)
    Unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, blank=True)


# Таблица Состав оборудования
class Hardware(models.Model):
    OperateSystem = models.CharField(max_length=150, blank=True)
    Activate = models.CharField(max_length=10, blank=True)
    CurrentUser = models.CharField(max_length=100, blank=True)
    IPAddress = models.IPAddressField
    MAC = models.CharField(max_length=100, blank=True)
    SystemName = models.CharField(max_length=50, blank=True)
    LANSpeed = models.CharField(max_length=10, blank=True)
    HDD = models.CharField(max_length=150, blank=True)
    Mboard = models.CharField(max_length=150, blank=True)
    ProcessorName = models.CharField(max_length=150, blank=True)
    Soccet = models.CharField(max_length=50, blank=True)
    OZU = models.CharField(max_length=25, blank=True)
    PrinterTypeConnect = models.CharField(max_length=15, blank=True)
    InstalledSoft = models.TextField(blank=True)


# Таблица Оборудование с инвентарными номерами и связи по пользователям, подразделениям
class Equipments(models.Model):
    InvNum = models.CharField(max_length=9)
    Types_id = models.ForeignKey(TypesEquipments, on_delete=models.DO_NOTHING)
    Brand_id = models.ForeignKey(Brands, on_delete=models.DO_NOTHING)
    Model_id = models.ForeignKey(Models, on_delete=models.DO_NOTHING)
    # Unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    User_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    Hardware_id = models.ForeignKey(Hardware, on_delete=models.DO_NOTHING, blank=True)


