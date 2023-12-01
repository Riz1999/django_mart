# Generated by Django 4.2.7 on 2023-11-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Books&Sports', 'Books&Sports'), ('Mobiles', 'Mobiles'),('Electronics', 'Electronics'), ('Bikes', 'Bikes'), ('Cars', 'Cars'), ('Furniture', 'Furniture'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('KA', 'Karnataka'), ('TN', 'Tamil Nadu'), ('MP', 'Madhya Pradesh'), ('WB', 'West Bengal'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('AS', 'Assam'), ('BR', 'Bihar'), ('MI', 'Sikkim'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('OD', 'Odisha'), ('KL', 'Kerala'), ('RJ', 'Rajasthan'), ('AP', 'Andhra Pradesh'), ('JH', 'Jharkhand'), ('UK', 'Uttarakhand'), ('MH', 'Maharashtra'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('GA', 'Goa'), ('CG', 'Chhattisgarh'), ('TS', 'Telangana'), ('HP', 'Haryana'), ('GJ', 'Gujarat'), ('PB', 'Punjab'), ('AR', 'Arunachal Pradesh')], max_length=100),
        ),
    ]
