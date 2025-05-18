FROM python:3.10-slim

WORKDIR /app

COPY main.py .

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false"]
