FROM python:3.9
RUN mkdir /code
WORKDIR /code
COPY . /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
# Chạy backend
WORKDIR /code
EXPOSE 8000
CMD ["gunicorn", "rel_api.wsgi"]