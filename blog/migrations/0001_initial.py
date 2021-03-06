# Generated by Django 4.0.3 on 2022-05-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_blog', models.CharField(max_length=20)),
                ('data_blog', models.DateTimeField()),
                ('text_blog', models.CharField(max_length=300)),
                ('image_blog', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
