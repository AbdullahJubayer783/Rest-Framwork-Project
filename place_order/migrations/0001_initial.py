# Generated by Django 4.2.7 on 2024-01-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_usermodel_image'),
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=15)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.flowermodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='users.usermodel')),
            ],
        ),
    ]
