# Generated by Django 2.0.10 on 2019-01-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0021_auto_20190127_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='preco_unitario',
            field=models.FloatField(default=0),
        ),
    ]
