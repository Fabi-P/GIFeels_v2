FROM python:3.10-slim-bookworm

WORKDIR /app

COPY confirmed_requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r confirmed_requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]