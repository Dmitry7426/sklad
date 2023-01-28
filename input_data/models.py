from django.core.validators import validate_slug, RegexValidator
from django.db import models


# Таблица ТипыОборудования
class TypesEquipments(models.Model):
    TypesEq = models.CharField(max_length=100)


# Таблица Бренды
class Brands(models.Model):
    BrandName = models.CharField(max_length=100, blank=True)


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
    UserName = models.CharField(max_length=100)
    MidlName = models.CharField(max_length=100)
    SurName = models.CharField(max_length=100)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True)
    Unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True)

class InvNum(models.Model):
    InvNumber = models.CharField(max_length=9)
    typ = models.ForeignKey(TypesEquipments, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(Models, on_delete=models.CASCADE, null=True)
    netname = models.CharField(max_length=25, null=True)

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
    Number = models.ForeignKey(InvNum, on_delete=models.DO_NOTHING)
    # Types_id = models.ForeignKey(TypesEquipments, on_delete=models.CASCADE)
    # Brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    # Model_id = models.ForeignKey(Models, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True)
    Hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE, blank=True)



