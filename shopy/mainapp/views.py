from django.shortcuts import render


def main(request):
    container_name = 'container'
    title = 'shopy - home'
    big_cards = [
        {'name': 'Reebok Track Jacket', 'price': '150$', 'img_src': 'product_1.png', 'img_alt': 'product1'},
        {'name': 'Reebok Track Jacket', 'price': '100$', 'img_src': 'product_2.png', 'img_alt': 'product2'},
        {'name': 'Reebok Track Jacket', 'price': '180$', 'img_src': 'product_3.png', 'img_alt': 'product3'},
        {'name': 'Reebok Track Jacket', 'price': '100$', 'img_src': 'product_2.png', 'img_alt': 'product2'},
    ]
    small_cards = [
        {'name': 'Reebok Track Jacket', 'price': '100$', 'img_src': 'product_4.png', 'img_alt': 'product4'},
        {'name': 'Reebok Track Jacket', 'price': '100$', 'img_src': 'product_4.png', 'img_alt': 'product4'},
        {'name': 'Reebok Track Jacket', 'price': '100$', 'img_src': 'product_4.png', 'img_alt': 'product4'},
    ]
    social_icons = [
        {'img_src': 'facebook.png', 'img_alt': 'facebook'},
        {'img_src': 'twitter.png', 'img_alt': 'twitter'},
        {'img_src': 'google.png', 'img_alt': 'google'},
        {'img_src': 'instagram.png', 'img_alt': 'instagram'},
    ]
    contact_icons = [
        {'text': 'info@shopy.com', 'img_src': 'mail.png', 'img_alt': 'mail'},
        {'text': '996 - 5553 - 453', 'img_src' '': 'phone.png', 'img_alt': 'phone'},
    ]
    content = {"container_name": container_name, 'title': title, 'big_cards': big_cards, 'small_cards': small_cards,
               'social_icons': social_icons, 'contact_icons': contact_icons}

    return render(request, 'mainapp/index.html', content)


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    container_name = 'contacts-container'
    title = 'shopy - contacts'
    content = {"container_name": container_name, 'title': title}
    return render(request, 'mainapp/contacts.html', content)
