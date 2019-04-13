from requests_html import HTMLSession


delivery_categories_selector = 'h2[id^="anchor_"]'
delivery_dish_selector = '#{}+.dish_list .product_title'

result = []

session = HTMLSession()
r = session.get('https://nn.delivery-club.ru/srv/Wok__Go/#Kazanskoje_sh/')

for category_el in r.html.find(delivery_categories_selector):
    food = r.html.find(delivery_dish_selector.format(category_el.attrs['id']))
    for food_el in food:
        result.append({
                'category': category_el.text,
                'title': food_el.text
            }
        )

print('Result {}'.format(result))
