from celery.schedules import crontab
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = 'test_secret_key'
	CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
	TASK_SERIALIZER = 'json'
	CELERYBEAT_SCHEDULE = {
		'update_stored_data': {
			'task': 'app.tasks.update_stored_data',
			'schedule': crontab(minute='*')#crontab(minute='0', hour='0', day_of_week='0'),
			'args': ()
		}
	}
	SQLALCHEMY_DATABASE_URI = ('sqlite:///' + 
		os.path.join(basedir, 'app.db'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SERVER_NAME = '34.218.1.48'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'shorensteintesting@gmail.com'
	MAIL_PASSWORD = 'hkshkshks'