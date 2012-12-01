install:
	python setup.py develop
	pip install -r requirements.txt

test:
	./runtests.py

release:
	git checkout master
	python setup.py sdist upload
	git push origin master
	git push --tags
