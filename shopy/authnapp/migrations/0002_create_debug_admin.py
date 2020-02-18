from django.conf import settings
from django.db import migrations


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authnapp.models import ShopUser

            ShopUser.objects.create_superuser(
                "admin", "admin@gmail.com", "50rtRFr4", age=25
            )
        except:
            print("Can't create super user for debug")


def reverse_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authnapp.models import ShopUser

            # ShopUser.objects.create_superuser(
            #     "admin", "admin@gmail.com", "admin", age=25
            # )
            ShopUser.objects.delete.all()
        except:
            print("Can't delete super user for debug")


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
