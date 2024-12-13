# Define the image name
IMAGE_NAME = CheerUpApp
DOCKER_USERNAME = jahnavimaddhuri

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run Docker container
run:
	docker run -p 5000:5000 $(IMAGE_NAME)

# Remove Docker image
clean:
	docker rmi $(IMAGE_NAME)

image_show:
	docker images

container_show:
	docker ps

push:
	docker login
	docker tag $(IMAGE_NAME) $(DOCKER_USERNAME)/$(IMAGE_NAME)
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):latest

login:
	docker login -u ${DOCKER_USERNAME}

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app --cov=mylib test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint
