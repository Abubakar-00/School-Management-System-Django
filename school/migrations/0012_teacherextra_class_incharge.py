# Generated by Django 3.0.5 on 2023-06-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherextra',
            name='class_incharge',
            field=models.CharField(blank=True, choices=[(None, 'null'), ('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four'), ('five', 'Five'), ('six', 'Six'), ('seven', 'Seven'), ('eight', 'Eight'), ('nine', 'Nine'), ('ten', 'Ten')], default=None, max_length=10, null=True),
        ),
    ]
