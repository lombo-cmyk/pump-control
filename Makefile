.PHONY: build, build-, start, stop, restart, logs-, dev, tests

build:
	BUILDKIT_COLORS="run=light-cyan" docker compose build

build-%:
	BUILDKIT_COLORS="run=light-cyan" docker compose build $*

start:
	docker compose up -d --remove-orphans

stop:
	docker compose down

restart: stop start

logs-%:
	docker logs $* -f

dev:
	./build_helpers/make-dev.sh

tests:
	./build_helpers/make-tests.sh