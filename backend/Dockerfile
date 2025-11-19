FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install "unstructured[pdf]"
COPY . .
CMD ["python", "main.py"]