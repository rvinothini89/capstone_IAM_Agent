FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Streamlit environment settings
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

ENV PYTHONPATH=/app

# Run Streamlit app
CMD ["streamlit", "run", "ui/app.py"]
