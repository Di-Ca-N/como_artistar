# Generated by Django 3.1.7 on 2021-03-18 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0013_auto_20210318_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
