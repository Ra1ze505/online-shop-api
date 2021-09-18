FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /zh_yarn

COPY ./requirements.txt /zh_yarn/requirements.txt
RUN pip install -r /zh_yarn/requirements.txt

COPY . /zh_yarn

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]