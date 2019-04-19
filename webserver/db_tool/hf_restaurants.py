from webserver.entities import Restaurant
from webserver.storage.storage import Storage

restaurant_records = [
	{
		'title': 'Burger King',
		'provider': 'delivery',
		'asset': 'burger_king.jpg',
		'url': ''
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
	},{
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
		rest.initialize(r)
		print("Written {}: {}".format(r['title'], storage.save(rest)))
