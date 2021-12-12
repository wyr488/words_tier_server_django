
option1:	not use virtual enviranment
	SETUP:
		step1:install python
		step2:install django
			python -m pip install Django
	RUN:
		step1:within outer folder mysite in terminal
			python manage.py runserver
		step2:in browser
			http://127.0.0.1:8000/tier/5/			tier 5
			http://127.0.0.1:8000/admin/			admin(username) 0410(password)

option2:	use virtual enviranment
	SETUP:
		step1:	install python
		step2:	https://docs.python.org/3/tutorial/venv.html
		step3:	install django
			python -m pip install Django
	RUN:
		step1:enter virtual enviranment
		step2:within outer folder mysite in terminal
			python manage.py runserver
		step3:in browser
			http://127.0.0.1:8000/tier/5/			tier 5
			http://127.0.0.1:8000/admin/			admin(username) 0410(password)

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page

https://docs.djangoproject.com/en/3.2/intro/tutorial02/
python manage.py shell
from tiers.models import Word_gen
w=Word_gen.objects.get(word_text='importance')
w.levels