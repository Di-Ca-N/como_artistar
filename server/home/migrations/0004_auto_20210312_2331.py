# Generated by Django 3.1.7 on 2021-03-12 23:31

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_coursepage_resourcepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]