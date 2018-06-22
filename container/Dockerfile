FROM python

RUN pip install --upgrade pip

ARG GROUPID
ARG USERID

RUN groupadd -g ${GROUPID} -r developer && useradd -u ${USERID} -r -g developer developer

RUN mkdir -p /home/developer/.local/bin
RUN chown -R developer:developer /home/developer

RUN mkdir /app
RUN chown developer:developer /app

ENV PATH="${PATH}:/home/developer/.local/bin"

USER developer

WORKDIR /app
