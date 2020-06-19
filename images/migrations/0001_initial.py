# Generated by Django 3.0.7 on 2020-06-19 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=128, null=True)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(blank=True, related_name='liked_images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
