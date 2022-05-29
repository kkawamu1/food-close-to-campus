FROM python:3.8

EXPOSE 8501

WORKDIR /usr/app/src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app ./

CMD ["sh", "-c", "streamlit run /usr/app/src/app.py --server.port=$PORT"]