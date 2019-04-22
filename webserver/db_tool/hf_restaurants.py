from webserver.db_tool import hf_food
from webserver.entities import Restaurant
from webserver.storage.storage import Storage
from webserver.db_tool.hf_food import get_categories

restaurant_records = [
	{
		'title': 'Burger King',
		'provider': 'delivery',
		'asset': 'burger_king.jpg',
		'url': 'https://nn.delivery-club.ru/srv/Burger_King_nnov/'
	}, {
		'title': 'Woking',
		'provider': 'delivery',
		'asset': 'wok__go.jpg',
		'url': 'https://nn.delivery-club.ru/srv/Wok__Go/'
	}, {
		'title': 'Еда с совой',
		'provider': 'delivery',
		'asset': 'jeda_s_sovoj.jpg',
		'url': 'https://nn.delivery-club.ru/srv/Jeda_s_Sovoj'
	}, {
		'title': 'Кулинария Ирины Князевой',
		'provider': 'delivery',
		'asset': 'kilinaria_iriny_knayzevoj.jpg',
		'url': 'https://nn.delivery-club.ru/srv/Kilinaria_Iriny_Knayzevoj/'
	}, {
		'title': 'Осетинские пироги',
		'provider': 'delivery',
		'asset': 'osetinskie_pirogi_nn.jpg',
		'url': 'https://nn.delivery-club.ru/srv/Osetinskie_pirogi_nn'
	}, {
		'title': 'Тануки',
		'provider': 'delivery',
		'asset': 'tanuki_nn.jpg',
		'url': 'https://nn.delivery-club.ru/srv/Tanuki_nn'
	}, {
		'title': 'Папас Китчен',
		'provider': 'yandex',
		'asset': 'papa_kitchen.jpg',
		'url': ''
	}, {
		'title': 'Лепи тесто',
		'provider': 'yandex',
		'asset': 'pelmennaya_lepi_testo.jpg',
		'url': ''
	}, {
		'title': 'Вай Гоги',
		'provider': 'yandex',
		'asset': 'vai_gogi.jpg',
		'url': ''
	}, {
		'title': 'Plov&Go',
		'provider': 'yandex',
		'asset': 'plovgo-logo.svg',
		'url': ''
	}, {
		'title': 'Жарбалкон',
		'provider': 'yandex',
		'asset': 'zharbalkon.jpg',
		'url': ''
	}, {
		'title': 'Та самая шаурма',
		'provider': 'other',
		'asset': 'shaurma.png',
		'url': 'https://shaurmanasrednom.ru/'
	}, {
		'title': 'Barabeq',
		'provider': 'other',
		'asset': 'barabeq.svg',
		'url': 'https://barabeq.ru/'
	}
]


def update(db):
	storage = Storage(db)
	for r in restaurant_records:
		rest = Restaurant(r['title'], r['provider'])
		rest.categories = get_categories(r['title'])
		rest.initialize(r)
		rest.asset = r['asset']
		rest.url = r['url']
		print("Written {}: {}".format(r['title'], storage.save(rest)))
