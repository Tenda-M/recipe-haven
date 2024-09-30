# Generated by Django 4.2.16 on 2024-09-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_sharedrecipe_delete_sharedbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedrecipe',
            name='ingredients',
            field=models.TextField(default='No ingredients provided'),
        ),
        migrations.AddField(
            model_name='sharedrecipe',
            name='methods',
            field=models.TextField(default='No methods provided'),
        ),
        migrations.AlterField(
            model_name='sharedrecipe',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sharedrecipe',
            name='image',
            field=models.ImageField(upload_to='recipes/'),
        ),
        migrations.AlterField(
            model_name='sharedrecipe',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
