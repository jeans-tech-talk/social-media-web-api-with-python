# Generated by Django 4.2.3 on 2023-08-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_profile_cover_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_cover',
            field=models.ImageField(blank=True, upload_to='users/profile_covers/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='users/profile_pictures/%Y/%m/%d/'),
        ),
    ]