from django.db import models


class Balance(models.Model):
    date = models.DateField()
    sum_balance = models.IntegerField()

    class Meta:
        verbose_name = 'Доступный остаток'

    def __unicode__(self):
        self.sum_balance


class User(models.Model):
    username = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Пользователи'

    def __str__(self):
        return self.username


class SourceType(models.Model):
    S_TYPE = [
        ('1', 'Наличные'),
        ('2', 'Карта'),
    ]
    type = models.CharField(max_length=200, choices=S_TYPE)
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    source_sum = models.IntegerField()

    class Meta:
        verbose_name = 'Типы источников'

    def __str__(self):
        return self.type


class TransactionsType(models.Model):
    pass

    class Meta:
        pass

    def __str__(self):
        pass


class Transactions(models.Model):
    pass

    class Meta:
        pass

    def __str__(self):
        pass

