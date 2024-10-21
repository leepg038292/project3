# Generated by Django 5.1.2 on 2024-10-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Gender', models.CharField(max_length=255)),
                ('P_name', models.TextField()),
                ('Name', models.TextField()),
                ('Rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Winter', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Spring', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Summer', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Fall', models.DecimalField(decimal_places=2, max_digits=10)),
                ('season', models.TextField()),
                ('Day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('Main_Components', models.TextField()),
                ('Top_Notes', models.TextField()),
                ('Middle_Notes', models.TextField()),
                ('Base_Notes', models.TextField()),
                ('Longetivity', models.TextField()),
                ('Image', models.TextField()),
                ('Skint_ype', models.TextField()),
                ('Style', models.TextField()),
                ('MBTI', models.TextField()),
            ],
        ),
    ]
