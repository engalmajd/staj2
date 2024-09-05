FROM rasa/rasa:2.8.0

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["rasa"]
CMD ["run", "--enable-api"]
