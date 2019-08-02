# Generated by Django 2.2.3 on 2019-08-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20190802_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='postcode',
        ),
        migrations.AlterField(
            model_name='room',
            name='roomtype',
            field=models.CharField(choices=[('오피스텔', '오피스텔'), ('투룸', '투룸'), ('고시텔', '고시텔'), ('원룸', '원룸'), ('아파트', '아파트')], max_length=100),
        ),
    ]
