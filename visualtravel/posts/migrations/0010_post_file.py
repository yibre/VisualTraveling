# Generated by Django 3.0.14 on 2021-06-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210526_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ImageField(default='https://media1.giphy.com/media/3oz8xBgi2syJQiMJAQ/giphy.gif', upload_to='post_photos'),
        ),
    ]