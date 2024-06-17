ARG py_version=3.12
ARG tf_version=2.16.1

FROM python:${py_version}

ARG tf_version

RUN apt-get update -q && apt-get install -q -y libhdf5-dev
RUN pip install psutil tensorflow==$tf_version

COPY t.py t.py
CMD python t.py
