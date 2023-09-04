Context
=======

A classe 'Context' recebe 2 atributos:
    + cluster: Cluster
        Objeto da classe 'Cluster'.

    + language(optional): Literal["sql", "python", "scala"]
        Linguagem que será utilizada. "python" é utilizado como default.

.. code-block:: python

    >>> from databricks.compute.commandExecution import Context

    >>> context = Context(cluster) # PYTHON


Create
======

O método 'create' cria um contexto dentro do cluster, para que algum comando seja executado.

.. code-block:: python

    >>> context.create()

Get Status
==========

O método 'getStatus' retorna de um contexto dentro do cluster.

.. code-block:: python

    >>> context.getStatus()
    {
        id: str,
        status: str
    }

Delete
======
O método 'delete' exclui um contexto de dentro do cluster.

.. code-block:: python

    >>> context.delete()
    {
        clusterId: str,
        contextId: str
    }