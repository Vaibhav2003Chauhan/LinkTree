# Generated by Django 4.2.1 on 2023-09-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_userinformation_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=''),
        ),
    ]