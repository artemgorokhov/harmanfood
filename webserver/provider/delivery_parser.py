from requests_html import HTML
import asyncio
from pyppeteer import launch


delivery_categories_selector = 'h2[id^="anchor_"]'
delivery_dish_selector = '#{}+.dish_list>li'
delivery_title_selector = '.product_title'
delivery_pic_selector = '.main_img>img'
delivery_detail_selector = '.dish_detail'
delivery_price_selector = 'form>p>strong>span:first-child'
address_selector = '#user-addr__input'
address_button_selector = 'a.user-addr__submit'
close_time = '#close_time_window'
vendor_selector = '.vendor-headline__tab-link'
footer_selector = '.footer-copyright'


def get_food(html):
    result = []
    for category_el in html.find(delivery_categories_selector):
        food = html.find(delivery_dish_selector.format(category_el.attrs['id']))
        if category_el.text == 'Пицца':
            print('!!!!')
        print(category_el.text)

        for food_el in food:
            title = food_el.find(delivery_title_selector)[0]
            pic = food_el.find(delivery_pic_selector)[0]
            detail = food_el.find(delivery_detail_selector)[0]
            price = food_el.find(delivery_price_selector)[0]
            result.append({
                'category': category_el.text,
                'title': title.text,
                'price': price.text,
                'pic': pic.attrs['src'],
                'description': detail.text
            }
            )
    return result


async def main(rest_url):
    # session = AsyncHTMLSession()
    # r = await session.get('https://nn.delivery-club.ru/srv/Wok__Go/#Kazanskoje_sh/')
    # await r.html.arender(keep_page=True)
    # print('Vendor: {}'.format(r.html.find(vendor_selector)[0].attrs['href']))
    # page = r.html.page
    browser = await launch(
        {
            "headless": False,
            "args": [
                '--window-size=1000,1000',
                # '--disable-dev-shm-usage',
                # '--shm-size=1gb',
                '--no-sandbox',
                '--no-user-gesture-required'
            ]
        }
    )
    page = await browser.newPage()
    await page.goto(rest_url)
    print('PAGE URL: {}'.format(page.url))
    print('Page rendered')
    # await asyncio.sleep(2)
    # page = r.html.page
    # await page.screenshot({'path': '01.png', 'fullPage': True})

    # cookies = await page.cookies()
    # print('Cookies: {}'.format(cookies))
    # await page.setCookie({'name': 'mapup_addr',
    #      'value': '%5B%22%5Cu0420%5Cu043e%5Cu0441%5Cu0441%5Cu0438%5Cu044f%2C+%5Cu041d%5Cu0438%5Cu0436%5Cu043d%5Cu0438%5Cu0439+%5Cu041d%5Cu043e%5Cu0432%5Cu0433%5Cu043e%5Cu0440%5Cu043e%5Cu0434%2C+%5Cu0421%5Cu0430%5Cu043b%5Cu0433%5Cu0430%5Cu043d%5Cu0441%5Cu043a%5Cu0430%5Cu044f+%5Cu0443%5Cu043b%5Cu0438%5Cu0446%5Cu0430%2C+24%22%5D',
    #      'domain':'.delivery-club.ru'})
    # await page.setCookie({'name':'new_gtm_address_coords', 'value': 'long%3A44.020359%2Flat%3A56.304445',
    #                       'domain':'.delivery-club.ru'})
    # print('Trying to reload')
    # await page.reload()
    cookies = await page.cookies()
    print('Cookies: {}'.format(cookies))
    try:
        await page.click(close_time)
    except Exception:
        print('No close time')
    # await page.screenshot({'path': '02.png', 'fullPage': True})
    await page.focus(address_selector)
    print('in focus')
    await asyncio.sleep(3)
    for i in range(20):
        await page.keyboard.press('ArrowRight')
        await page.keyboard.press('Backspace')
    await page.type(address_selector, 'Нижний Новгород, Салганская улица, 24')
    print('Input address')
    # await page.screenshot({'path': '03.png', 'fullPage': True})
    navigationPromise = asyncio.ensure_future(page.waitForNavigation())
    await page.click(address_button_selector)
    print('Clicked on button')
    await navigationPromise
    await asyncio.sleep(5)
    print('Waited navigation')

    # Maybe to let images load
    # await page.click(footer_selector)
    # await asyncio.sleep(5)

    # Or this one
    # await page.screenshot({'path': '04.png', 'fullPage': True})
    # await asyncio.sleep(5)

    wok_content = await page.content()

    # print('Vendor: {}'.format(r.html.find(vendor_selector)[0].attrs['href']))
    # await r.html.arender(keep_page=True)

    await asyncio.sleep(5)
    # await page.close()
    # await browser.close()
    return wok_content


rests = {
    'Woking': 'https://nn.delivery-club.ru/srv/Wok__Go/',
    'Tanuki': 'https://nn.delivery-club.ru/srv/Tanuki_nn',
    'OsePirogi': 'https://nn.delivery-club.ru/srv/Osetinskie_pirogi_nn',
    'Sova': 'https://nn.delivery-club.ru/srv/Jeda_s_Sovoj',
    'Irina': 'https://nn.delivery-club.ru/srv/Kilinaria_Iriny_Knayzevoj/'
}

loop = asyncio.new_event_loop()
the_content = loop.run_until_complete(main(rests['Irina']))

print('done')

html = HTML(html=the_content)
food = get_food(html)

print('Result {}'.format(food))
# loop.close()
