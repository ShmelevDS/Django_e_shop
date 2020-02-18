from django.db import migrations


def forwards_func(apps, schema_editor):
    pro_cat_model = apps.get_model("mainapp", "ProductCategory")  # Load model for make changes
    pro_model = apps.get_model("mainapp", "Product")  # Load model for make changes
    icon_cat_model = apps.get_model("mainapp", "IconCategory")  # Load model for make changes
    icon_model = apps.get_model("mainapp", "Icon")  # Load model for make changes

    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=1,
        name="Jackets", description="Everybody needs one")
    # Create new products in this category
    pro_model.objects.create(
        pk=1,
        category=pro_cat_obj,  # Foreign key
        name="Reebok Trace Jacket",
        image="source/products/product_3.png",
        short_desc="Nice jacket",
        full_desc="Really nice jacket",
        price="134.56",
        quantity=65,
        size="M",
        brand="Reebok"
    )
    pro_model.objects.create(
        pk=2,
        category=pro_cat_obj,  # Foreign key
        name="Nike Trace Jacket",
        image="source/products/product_2.png",
        short_desc="Nice jacket",
        full_desc="Really nice jacket",
        price="184.56",
        quantity=125,
        size="L, XL, S",
        brand="Nike"
    )
    pro_model.objects.create(
        pk=3,
        category=pro_cat_obj,  # Foreign key
        name="Adiddas Trace Jacket",
        image="source/products/product_1.png",
        short_desc="Such a cool jacket",
        full_desc="Warm and waterproof, wow",
        price="250.00",
        quantity=25,
        size="M, XL",
        brand="Adiddas"
    )
    pro_model.objects.create(
        pk=4,
        category=pro_cat_obj,  # Foreign key
        name="Another Trace Jacket",
        image="source/products/product_1.png",
        short_desc="For nice guys",
        full_desc="Such a nice-looking jacket",
        price="312.27",
        quantity=37,
        size="L, XL",
        brand="Adiddas"
    )
    del pro_cat_obj  # Delete link for category

    # Create new category
    pro_cat_obj = pro_cat_model.objects.create(
        pk=2,
        name="Leather Jackets", description="Nice for cold ad rainy weather"
    )
    # Create new products in this category
    pro_model.objects.create(
        pk=5,
        category=pro_cat_obj,  # Foreign key
        name="Leather Jacket",
        image="source/products/product_4.png",
        short_desc="Tough guy edition",
        full_desc="Kick some ass",
        price="450.22",
        quantity=87,
        size="S, M, XL, XXL",
        brand="LeatherJ"
    )
    pro_model.objects.create(
        pk=6,
        category=pro_cat_obj,  # Foreign key
        name="Raincoat",
        image="source/products/product_4.png",
        short_desc="Perfect for rainy weather",
        full_desc="Extraordinary quality and low price",
        price="278.05",
        quantity=32,
        size="S, XL, XXL",
        brand="LeatherJ"
    )
    pro_model.objects.create(
        pk=7,
        category=pro_cat_obj,  # Foreign key
        name="Another Leather Jacket",
        image="source/products/product_4.png",
        short_desc="Such a cool jacket",
        full_desc="Nice quality much comfort",
        price="87.54",
        quantity=29,
        size="S, M, L",
        brand="LeatherJ"
    )
    del pro_cat_obj  # Delete link for category

    # Create new category
    icon_cat_obj = icon_cat_model.objects.create(
        pk=1,
        name="Social media", description="Social media icons, e. g. facebook, twitter and so on")
    # Create new products in this category
    icon_model.objects.create(
        pk=1,
        category=icon_cat_obj,  # Foreign key
        name="Facebook",
        image="source/icons/facebook.png",
        text="Facebook"
    )
    icon_model.objects.create(
        pk=2,
        category=icon_cat_obj,  # Foreign key
        name="Twitter",
        image="source/icons/twitter.png",
        text="Twitter"
    )
    icon_model.objects.create(
        pk=3,
        category=icon_cat_obj,  # Foreign key
        name="Google+",
        image="source/icons/google.png",
        text="Google+"
    )
    icon_model.objects.create(
        pk=4,
        category=icon_cat_obj,  # Foreign key
        name="Instagram",
        image="source/icons/instagram.png",
        text="Instagram"
    )
    del icon_cat_obj  # Delete link for category

    # Create new category
    icon_cat_obj = icon_cat_model.objects.create(
        pk=2,
        name="Contact icons", description="Contact icons, e. g. phone, mail and so on")
    # Create new products in this category
    icon_model.objects.create(
        pk=5,
        category=icon_cat_obj,  # Foreign key
        name="Phone",
        image="source/icons/phone.png",
        text="+ 7 (985) 259-02-58"
    )
    icon_model.objects.create(
        pk=6,
        category=icon_cat_obj,  # Foreign key
        name="E-mail",
        image="source/icons/mail.png",
        text="shopy@gmail.com"
    )
    del icon_cat_obj  # Delete link for category


def reverse_func(apps, schema_editor):
    pro_cat_model = apps.get_model("mainapp", "ProductCategory")  # Load model for make changes
    icon_cat_model = apps.get_model("mainapp", "IconCategory")  # Load model for make changes

    # Delete all objects
    pro_cat_model.objects.all().delete()
    icon_cat_model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("mainapp", "0007_auto_20200216_1905")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
