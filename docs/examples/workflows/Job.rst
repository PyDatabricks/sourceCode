Job
===

A classe 'Job' possui 2 atributos:
    + databricks: Databricks
        Objeto da classe Databricks.

    + id: str
        Id da job.


.. code-block:: python

    >>> from databricks.workflows.job import Job

    >>> dbJob = Job(databricks, "<job-id>")

Get Info
========

O método 'getInfo' retorna informações sobre a job.

.. code-block:: python

    >>> print(dbJob.getInfo())
    {
        job_id: int
        creator_user_name: str
        settings: { ... }
        created_time: int
        run_as_user_name: str
        trigger_history: { ... }
    }

Delete
======

O método 'delete' exclui a job da lista de workflows.

.. code-block:: python

    >>> dbJob.delete()


Run
===

O método 'run' inicia a job. O método retorna um jobRunId.

    Params:
        + params: DatabricksRunJobRequestType
            Parâmetros para o início da job.

.. code-block:: python

    >>> print(dbJob.run())
    {
        "run_id": int
    }

Cancel All Runs
===============

O método 'calcelAllJobRuns' cancela todas as 'runs' da job atual.

.. code-block:: python

    >>> dbJob.calcelAllJobRuns()