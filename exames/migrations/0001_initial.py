# Generated by Django 5.0.3 on 2024-03-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiposExames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('I', 'Exame de imagem'), ('S', 'Exame de sangue')], max_length=1)),
                ('preco', models.FloatField()),
                ('disponivel', models.BooleanField(default=True)),
                ('horario_inicial', models.IntegerField()),
                ('horario_final', models.ImageField(upload_to='')),
            ],
        ),
    ]
