$(eval USERID = $(shell id --user))
$(eval GROUPID = $(shell id --group))


build: env-up
	docker exec -it python-node python setup.py bdist_wheel


console: env-up
	docker exec -it python-node bash


env-up: env-build
	USERID=${USERID} GROUPID=${GROUPID} docker-compose -f compose.yml up -d


env-build:
	USERID=${USERID} GROUPID=${GROUPID} docker-compose -f compose.yml build


env-rebuild:
	USERID=${USERID} GROUPID=${GROUPID} docker-compose -f compose.yml build --no-cache
