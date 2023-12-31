# Generated by Django 4.2.6 on 2023-10-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, verbose_name='Aucune nom')),
                ('prix', models.IntegerField(default=0.0)),
                ('description', models.TextField(verbose_name='Aucune description')),
                ('quantite', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mes image', verbose_name='Image')),
            ],
        ),
    ]
