# Generated by Django 2.0.4 on 2018-09-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_notice_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='status',
            field=models.CharField(choices=[(1, '未审核'), (2, '审核中'), (3, '已发布')], default=1, max_length=4),
        ),
    ]
