build_dev:
	docker stop $$(docker ps -q) || true
	docker-compose -f local.yml up --build
dev:
	docker stop $$(docker ps -q) || true
	docker-compose -f local.yml up
test:
	docker-compose -f local.yml run web pytest

redeploy-staging:
	bash redeploy-staging.sh
redeploy-prod:
	bash redeploy-prd.sh