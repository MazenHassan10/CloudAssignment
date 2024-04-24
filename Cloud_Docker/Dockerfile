FROM python

WORKDIR /app

RUN pip install nltk

RUN python -m nltk.downloader stopwords

COPY . /app

CMD python CloudAssignment.py
