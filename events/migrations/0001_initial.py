# Generated by Django 4.0.3 on 2022-05-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_event', models.ImageField(upload_to='event_images/')),
                ('text_event', models.CharField(max_length=300)),
            ],
        ),
    ]
