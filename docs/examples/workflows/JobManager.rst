Job Manager
===========

A classe 'JobManager' recebe 1 atributo.
    + databricks: Databricks
        Objeto da classe 'Databricks'.

.. code-block:: python

    >>> from databricks.workflows import JobManager

    >>> jobManager = JobManager(databricks)


Create Job
==========

O método 'createNewJob' cria uma nova job na lista de workflows.
    Params:
        + options: DatabricksCreateJobRequestType
            Opções para a criação da job.

.. code-block:: python

    >>> print(jobManager.create())
    {
        "job_id": int
    }

List Jobs
=========

O método 'listJobs' lista as jobs do cluster.
    Params:
        + limit(optional): int
            Número de jobs que serão retornadas.
        + page_token(optional): str
            Use 'next_page_token' ou 'prev_page_token' para retornar a próxima página ou a anterior, respectivamente.
        + name(optional): str
            As jobs serão filtradas com base neste parâmetro.
        + expand_tasks(optional): bool
            Incluir detalhes do cluster no retorno.

.. code-block:: python

    >>> jobManager.listJobs()
    {
        jobs: [ ... ]
        has_more: bool
        next_page_token: str
        prev_page_token: str
    }