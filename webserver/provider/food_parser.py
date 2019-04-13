from requests_html import HTMLSession


delivery_categories_selector = 'h2[id^="anchor_"]'
delivery_dish_selector = '#{}+.dish_list>li'
delivery_title_selector = '.product_title'
delivery_pic_selector = '.main_img>img'
delivery_detail_selector = '.dish_detail'

result = []

session = HTMLSession()
r = session.get('https://nn.delivery-club.ru/srv/Wok__Go/#Kazanskoje_sh/')

for category_el in r.html.find(delivery_categories_selector):
    food = r.html.find(delivery_dish_selector.format(category_el.attrs['id']))
    for food_el in food:
        title = food_el.find(delivery_title_selector)[0]
        pic = food_el.find(delivery_pic_selector)[0]
        detail = food_el.find(delivery_detail_selector)[0]
        result.append({
                'category': category_el.text,
                'title': title.text,
                'pic': pic.attrs['src'],
                'description': detail.text
            }
        )

print('Result {}'.format(result))
