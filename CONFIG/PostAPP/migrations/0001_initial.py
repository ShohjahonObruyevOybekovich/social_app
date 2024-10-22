# Generated by Django 4.0.2 on 2022-02-08 14:08

import PostAPP.models
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
            name='ModelPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('modifiedDate', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('images', models.FileField(blank=True, null=True, upload_to='Posts')),
                ('unique_id', models.UUIDField(default=PostAPP.models.create_new_ref_number, editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gönderi',
                'verbose_name_plural': 'Gönderiler',
                'db_table': 'Posts',
            },
        ),
    ]