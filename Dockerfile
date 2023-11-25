FROM python
COPY . /app
WORKDIR /app
COPY req.txt .
RUN ls -l
RUN cat req.txt
RUN pip install --upgrade pip
RUN pip install -r req.txt
CMD ["python", "app.py"]