# Generated by Django 4.2.10 on 2024-03-10 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_featured_image'),
        ('messaging', '0003_remove_conversation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='topic',
        ),
        migrations.AlterField(
            model_name='conversation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='products.product', unique=True),
        ),
    ]
