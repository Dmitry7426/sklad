from django.db import models


# Таблица ТипыОборудования
class TypesEquipments(models.Model):
    TypesEq = models.CharField(max_length=100)


# Таблица Бренды
class Brands(models.Model):
    BrandName = models.CharField(max_length=100)


# Таблица Модель
class Models(models.Model):
    ModelName = models.CharField(max_length=100)


# Таблица Подразделения
class Units(models.Model):
    UnitName = models.CharField(max_length=150)


# Таблица Должность
class Positions(models.Model):
    PositionName = models.CharField(max_length=250)


# Таблица Пользователи
class Users(models.Model):
    UserName = models.CharField(max_length=100)
    MidlName = models.CharField(max_length=100)
    SurName = models.CharField(max_length=100)
    Position_id = models.ForeignKey(Positions, on_delete=models.DO_NOTHING)


# Таблица Состав оборудования
class Hardware(models.Model):
    OperateSystem = models.CharField(max_length=150)
    Activate = models.CharField(max_length=10)
    CurrentUser = models.CharField(max_length=100)
    IPAddress = models.IPAddressField
    MAC = models.CharField(max_length=100)
    SystemName = models.CharField(max_length=50)
    LANSpeed = models.CharField(max_length=10)
    HDD = models.CharField(max_length=150)
    Mboard = models.CharField(max_length=150)
    ProcessorName = models.CharField(max_length=150)
    Soccet = models.CharField(max_length=50)
    OZU = models.CharField(max_length=25)
    PrinterIP = models.IPAddressField
    InstalledSoft = models.TextField


# Таблица Оборудование по подразделениям
class Equipments(models.Model):
    InvNum = models.CharField(max_length=9)
    Types_id = models.ForeignKey(TypesEquipments, on_delete=models.DO_NOTHING)
    Brand_id = models.ForeignKey(Brands, on_delete=models.DO_NOTHING)
    Model_id = models.ForeignKey(Models, on_delete=models.DO_NOTHING)
    Unit_id = models.ForeignKey(Units, on_delete=models.DO_NOTHING)
    User_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    Hardware_id = models.ForeignKey(Hardware, on_delete=models.DO_NOTHING)


