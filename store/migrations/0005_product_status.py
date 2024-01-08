# Generated by Django 5.0 on 2024-01-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waiting Approval'), ('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]
