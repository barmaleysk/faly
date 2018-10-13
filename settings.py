db_url='sqlite:///db.sqlite'

ref_pay_perc_1lvl=0.20 #столько получит от 1 уровная рефералов за оплату
ref_pay_perc_2lvl=0.10 #столько получит от 2 уровная рефералов за оплату
ref_view_pay_1lvl=0.20 #столько получит от 1 уровная рефералов за подписку
ref_view_pay_2lvl=0.10 #столько получит от 2 уровная рефералов за подписку
user_view_perc=0.5 #столько получит пользователь за вступление(проценты от стоимости установленной заказчиком)
min_out_pay=15 #минимальная сумма для вывода
min_post_cost=0.45 #минимальная стоимость 1 подписчика

number=+992928864416
qiwi_token ='17e785c92fbd7f9ac358e61b5a29437d'

ya_number=410013238616649
ya_token=''

telegram_token='658374451:AAGhl6rcfaC8tlTOISWwiHrvLlT4JpILkio'



uah_to_rub=2.16
usd_to_rub=57.85
eur_to_rub=67.73

admins = [575818266,471090279]


tutorial_url = 'http://telegra.ph/Kak-sdelat-bota-administratorom-04-07'



WEBHOOK_HOST = '54.77.103.27'
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'


WEBHOOK_SSL_CERT = './webhook_cert.pem'
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)

WEBHOOK_URL_PATH = "/{}/".format(telegram_token)




