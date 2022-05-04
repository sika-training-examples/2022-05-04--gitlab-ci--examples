generate-gitlab-ci:
	python3 generate-gitlab-ci.py
	git add .gitlab-ci.yml
	git commit -m "[auto] ci: Genetate .gitlab-ci.yml using generate-gitlab-ci.py"
