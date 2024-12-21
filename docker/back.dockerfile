FROM python:3.9.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /app/api
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]