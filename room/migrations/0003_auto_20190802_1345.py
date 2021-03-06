# Generated by Django 2.2.3 on 2019-08-02 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20190802_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='postcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomtype',
            field=models.CharField(choices=[('투룸', '투룸'), ('오피스텔', '오피스텔'), ('아파트', '아파트'), ('원룸', '원룸'), ('고시텔', '고시텔')], max_length=100),
        ),
    ]
