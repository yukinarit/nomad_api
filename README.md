# `nomad_api`

[![image](https://img.shields.io/pypi/v/nomad_api.svg)](https://pypi.org/project/nomad_api/) [![image](https://img.shields.io/pypi/pyversions/nomad_api.svg)](https://pypi.org/project/nomad_api/)

A Hashicorp Nomad API client written in modern Python.

## Motivation

There is already [python-nomad](https://github.com/jrxFive/python-nomad) library in PyPI, but I wanted to have async based Nomad API client written in modern Python with type annotation.

## Installation

`nomad_api` requires Python 3.9.

* pip
    ```
    pip install nomad_api
    ```
* pipenv
    ```
    pipenv install nomad_api
    ```
* poetry
    ```
    poetry add nomad_api
    ```

## Usage

```python
async with nomad.Client("http://localhost:4646") as cli:
    for job in await cli.jobs():
        print(job)
```

## Supported APIs

Nomad 1.0.4

 * [event_stream](https://www.nomadproject.io/api-docs/events)
 * Jobs
     * [List jobs](https://www.nomadproject.io/api-docs/jobs#list-jobs)
     * [Read job](https://www.nomadproject.io/api-docs/jobs#read-job)
