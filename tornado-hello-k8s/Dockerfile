FROM python:2.7.14-alpine3.7
WORKDIR /app/
ADD hello.py requirements.txt version.txt /app/
RUN pip install -r requirements.txt
EXPOSE 9000
ENTRYPOINT ["/usr/local/bin/python", "/app/hello.py"]