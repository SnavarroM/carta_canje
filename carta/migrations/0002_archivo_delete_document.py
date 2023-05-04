# Generated by Django 4.2 on 2023-04-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
