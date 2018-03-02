FROM python:2.7.14-alpine3.7
WORKDIR /app/
ADD hello.py /app/
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python", /app/hello.py]