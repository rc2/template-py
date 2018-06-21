FROM python

RUN pip install --upgrade pip

ARG GROUPID
ARG USERID

RUN groupadd -g ${GROUPID} -r developer && useradd -u ${USERID} -r -g developer developer

RUN mkdir /app

RUN chown developer:developer /app

USER developer

WORKDIR /app

ENV PYTHONPATH="/app"
