# Generated by Django 2.0.6 on 2019-02-19 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0024_cadastro_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pedido.Produto'),
        ),
    ]