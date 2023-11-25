FROM python
COPY . /app
WORKDIR /app
COPY req.txt .
RUN dir
RUN python -m pip install --upgrade pip
RUN pip install -r req.txt
CMD ["python", "app.py"]