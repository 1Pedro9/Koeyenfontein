from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    farm = models.IntegerField(default=1)
    owner = models.CharField(max_length=10, default='GCGB')
    type_id = models.IntegerField(default=1)
    tag = models.CharField(max_length=20)
    tag_color = models.CharField(max_length=20, null=True, blank=True)
    sex = models.IntegerField(default=1)
    sire = models.CharField(max_length=100, null=True, blank=True)
    dam = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.farm) + " - " + self.owner + " - " + self.tag

    class Meta:
        db_table = 'game'

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    is_admin = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'members'

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    sex = models.IntegerField(default=1)
    unit_cost = models.IntegerField()
    year = models.IntegerField()
    year_market_unit_value = models.IntegerField(null=True, blank=True)
    year_market_value = models.IntegerField(null=True, blank=True)
    year_value = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'units'

class Viewer(models.Model):
    id = models.AutoField(primary_key=True)
    type_id = models.IntegerField()
    img = models.CharField(max_length=300, default='')

    def __str__(self):
        object = Type.objects.filter(type_id = self.type_id)
        return str(object[0].type_name)
    
    class Meta:
        db_table = 'viewer'
        
        
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=200)
    value = models.CharField(max_length=10, default='High')

    def __str__(self):
        return str(self.type_name)

    class Meta:
        db_table = 'types'