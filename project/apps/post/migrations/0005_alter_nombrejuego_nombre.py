# Generated by Django 4.2.2 on 2023-06-16 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_fecha_de_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nombrejuego',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Juegos'),
        ),
    ]