.PHONY: init clean assets db

init:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -delete

db:
	flask recreate_db
	flask populate_db --num_users 5
