# contact: zekinv@gmail.com
FROM python:3.10-slim
RUN pip install --upgrade pip setuptools
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
CMD streamlit run main.py --server.port 8500 --server.address 0.0.0.0 --server.headless True --global.developmentMode False
