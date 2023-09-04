Job Run
=======

A classe 'JobRun' possui 2 atributos.
    + databricks: Databricks
        Objeto da classe 'Databricks'.
    + id: str
        Job Run id.

.. code-block:: python

    >>> from databricks.workflows import JobRun

    >>> jobRun = JobRun(databricks, "<job-run-id>")


Cancel
======

O método 'cancel' interrompe uma 'Job Run'.

.. code-block:: python

    >>> jobRun.cancel()

Delete
======

O método 'delete' exclui uma 'run' da job.

.. code-block:: python

    >>> jobRun.delete()

GetOutPut
=========

O método 'getOutput' retorna a saída da job.

.. code-block:: python

    >>> print(jobRun.getOutput())
    {
        notebook_output: { ... }
        sql_output: { ... }
        ...
        error_trace: str
        metadata: { ... }
    }

Repair
======

O método 'repair' repara a job run.
    Params:
        + params: DatabricksJobRunRequestType
            Parâmetros para a reparação da jobrun.

.. code-block:: python

    >>> print(jobRun.repair())
    {
        repair_id: int
    }
    

Get Info
========

O método 'getInfo' retorna as informações da jobrun.

    Params:
        + include_history(optional): bool
            Incluir o histórico de reparação na resposta.

.. code-block:: python

    >>> print(jobRun.getInfo())
    {
        job_id: int
        run_id: int
        ...
        run_type: Literal["JOB_RUN", "WORKFLOW_RUN", "SUBMIT_RUN"]
        attempt_number: int
        repair_history: [ ... ]
    }