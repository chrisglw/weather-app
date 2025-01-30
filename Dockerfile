FROM python:3.9-slim
EXPOSE 8501
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir -r requirements.txt
ENV MPLBACKEND=Agg
# RUN pip3 install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
