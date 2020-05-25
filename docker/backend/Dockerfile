FROM python:3.7

ENV NLTK_DOWNLOAD=/app
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=True

RUN pip install pipenv
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg
COPY *.py /app/

EXPOSE 5000
CMD flask run --host=0.0.0.0
