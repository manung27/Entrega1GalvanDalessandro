# Generated by Django 4.1 on 2022-08-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0003_alter_sobrina_examenes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('velocidad', models.ImageField(upload_to='')),
                ('caballos_fuerza', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Madre',
        ),
    ]
