# Generated by Django 4.1.7 on 2023-06-20 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("post", "0004_post_praceid"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="UserID",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="users",
                to="accounts.user",
                to_field="UserID",
            ),
            preserve_default=False,
        ),
    ]
