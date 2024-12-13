FROM python:3.9-slim

# set wd to dir in container
WORKDIR /app

# cp curr dir to /app 
COPY . /app

# install reqs
RUN pip install --no-cache-dir -r requirements.txt

# port 5001
EXPOSE 5001

# set env var
ENV FLASK_APP=app.py

# run flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
# CMD ["python", "app.py"]
