# Generated by Django 3.1.7 on 2021-05-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210502_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Mobiles', 'Mobiles'), ('Cars', 'Cars'), ('Bikes', 'Bikes'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('PB', 'Punjab'), ('ML', 'Meghalaya'), ('NL', 'Nagaland'), ('KL', 'Kerala'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('MN', 'Manipur'), ('KA', 'Karnataka'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('BR', 'Bihar'), ('WB', 'West Bengal'), ('TS', 'Telangana'), ('TN', 'Tamil Nadu'), ('CG', 'Chhattisgarh'), ('MI', 'Sikkim'), ('MP', 'Madhya Pradesh'), ('UK', 'Uttarakhand'), ('OD', 'Odisha'), ('MH', 'Maharashtra'), ('HP', 'Haryana'), ('JH', 'Jharkhand'), ('AS', 'Assam'), ('GA', 'Goa'), ('MZ', 'Mizoram')], max_length=100),
        ),
    ]
