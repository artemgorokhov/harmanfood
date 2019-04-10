from webserver.entities import Restaurant
from webserver.storage.storage import Storage

restaurant_records = [
	{
		'title': 'Burger King',
		'provider': 'delivery',
		'asset': 'burger_king.jpg'
	}, {
		'title': 'Woking',
		'provider': 'delivery',
		'asset': 'wok__go.jpg'
	}, {
		'title': 'Еда с совой',
		'provider': 'delivery',
		'asset': 'jeda_s_sovoj.jpg'
	}, {
		'title': 'Кулинария Ирины Князевой',
		'provider': 'delivery',
		'asset': 'kilinaria_iriny_knayzevoj.jpg'
	}, {
		'title': 'Папас Китчен',
		'provider': 'yandex',
		'asset': 'papa_kitchen.jpg'
	}, {
		'title': 'Лепи тесто',
		'provider': 'yandex',
		'asset': 'pelmennaya_lepi_testo.jpg'
	}, {
		'title': 'Вай Гоги',
		'provider': 'yandex',
		'asset': 'vai_gogi.jpg'
	}, {
		'title': 'Plov&Go',
		'provider': 'yandex',
		'asset': 'plovgo-logo.svg'
	}, {
		'title': 'Жарбалкон',
		'provider': 'yandex',
		'asset': 'zharbalkon.jpg'
	}, {
		'title': 'Та самая шаурма',
		'provider': 'other',
		'asset': 'shaurma.png'
	}, {
		'title': 'Barabeq',
		'provider': 'other',
		'asset': 'barabeq.svg'
	}
]


def update(db):
	storage = Storage(db)
	for r in restaurant_records:
		rest = Restaurant(r['title'], r['provider'])
		rest.initialize(r)
		print("Written {}: {}".format(r['title'], storage.save(rest)))

