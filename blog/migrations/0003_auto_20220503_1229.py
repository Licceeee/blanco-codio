# Generated by Django 3.2.5 on 2022-05-03 12:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStamps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamps_ptr',
            field=models.OneToOneField(auto_created=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.timestamps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='timestamps_ptr',
            field=models.OneToOneField(auto_created=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.timestamps'),
            preserve_default=False,
        ),
    ]