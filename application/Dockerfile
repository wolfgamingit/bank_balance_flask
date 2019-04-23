FROM python:2.7

RUN adduser bank_balance

WORKDIR /home/bank_balance

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY bank_balance bank_balance
COPY db db
COPY bank_app.py config.py boot.sh gunicorn_config.py ./
RUN chmod +x boot.sh

ENV FLASK_APP bank_app.py

RUN chown -R bank_balance: ./
USER bank_balance

#EXPOSE 5000
#ENTRYPOINT ["./boot.sh"]
CMD ["gunicorn", "--config", "gunicorn_config.py", "bank_app:app"]
