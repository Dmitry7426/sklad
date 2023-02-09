from django.db import models


# Таблица ТипыОборудования
class TypesEquipments(models.Model):
    TypesEq = models.CharField(max_length=100, unique=True)


# Таблица Бренды
class Brands(models.Model):
    BrandName = models.CharField(max_length=100, blank=True, unique=True)


# Таблица Модель
class Models(models.Model):
    ModelName = models.CharField(max_length=100, blank=True, unique=True)


# Таблица Подразделения
class Unit(models.Model):
    UnitName = models.CharField(max_length=150, blank=True, unique=True)


# Таблица Должность
class Position(models.Model):
    PositionName = models.CharField(max_length=250, blank=True, unique=True)


# Таблица Пользователи
class Users(models.Model):
    UserName = models.CharField(max_length=100)
    MidlName = models.CharField(max_length=100)
    SurName = models.CharField(max_length=100)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True)
    Unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True)


# таблица инвентарные номере с привязками
class InvNum(models.Model):
    InvNumber = models.CharField(max_length=9, unique=True)
    typ = models.ForeignKey(TypesEquipments, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(Models, on_delete=models.CASCADE, null=True)
    netname = models.CharField(max_length=25, null=True)


# Таблица Состав оборудования
class Hardware(models.Model):
    InvNumber = models.ForeignKey(InvNum, on_delete=models.DO_NOTHING)
    OperateSystem = models.CharField(max_length=150, blank=True, null=True)
    Activate = models.CharField(max_length=10, blank=True, null=True)
    CurrentUser = models.CharField(max_length=100, blank=True, null=True)
    IPAddress = models.CharField(max_length=255, null=True)
    MAC = models.CharField(max_length=100, blank=True, null=True)
    SystemName = models.CharField(max_length=50, blank=True, null=True)
    LANSpeed = models.CharField(max_length=10, blank=True, null=True)
    HDD = models.CharField(max_length=150, blank=True, null=True)
    Mboard = models.CharField(max_length=150, blank=True, null=True)
    ProcessorName = models.CharField(max_length=150, blank=True, null=True)
    Soccet = models.CharField(max_length=50, blank=True, null=True)
    OZU = models.CharField(max_length=25, blank=True, null=True)
    PrinterTypeConnect = models.CharField(max_length=15, blank=True, null=True)
    InstalledSoft = models.TextField(blank=True, null=True)


# Таблица Оборудование с инвентарными номерами и связи по пользователям, подразделениям
class Equipments(models.Model):
    Number = models.ForeignKey(InvNum, on_delete=models.DO_NOTHING)
    User = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True)
    Hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE, blank=True, null=True)

