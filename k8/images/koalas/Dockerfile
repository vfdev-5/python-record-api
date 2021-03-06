# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://koalas.readthedocs.io/en/latest/development/contributing.html#environment-setup
RUN git clone \
    --branch v1.2.0 \
    --depth 1 \
    git://github.com/databricks/koalas.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    install-jdk \
    pyspark \
    'pandas>=0.23.2,<1.1.0' \
    'pyarrow>=0.10' \
    'matplotlib>=3.0.0,<3.3.0' \
    'numpy>=1.14,<1.19.0' \
    'mlflow>=1.0' \
    pytest \
    pytest-cov \
    scikit-learn \
    openpyxl \
    xlrd \
    'plotly>=4.8' && \
    echo $(python -c "import jdk; print(jdk.install('8'))") > /tmp/java_home

RUN python -c "import databricks.koalas"

ENV PYTHON_RECORD_API_FROM_MODULES=koalas
CMD bash -c "JAVA_HOME=$(cat /tmp/java_home) ./dev/pytest --doctest-modules databricks -k 'not to_clipboard and not test_day_name and not test_month_name'"
