run:
	python manage.py runserver 0.0.0.0:8000

shell:
	python manage.py shell_plus --print-sql

notebook_shell:
	python manage.py shell_plus --notebook

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

makedatamigration:
	python manage.py makemigrations --empty $(app)

clean_pyc:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
