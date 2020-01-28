FROM python:3
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./scrap.py