Command Execution
=================

A classe 'CommandExecution' recebe 3 atributos:
    + command: str
        Comando a ser executado.

    + cluster: Cluster
        Objeto da classe 'Cluster'.

    + language(optional): Literal["sql", "python", "scala"]
        Linguagem que será utilizada. "python" é utilizado como default.

.. code-block:: python

    >>> from databricks.compute.commandExecution import CommandExecution

    >>> cmd = CommandExecution("<command>", cluster) # PYTHON

Run
===

O método 'run' cria um contexto dentro do cluster e executa o comando.

.. code-block:: python

    >>> print(cmd.run())
    {
        resultType: str,
        ...
        data: { ... },
        schema: [ ... ],
        truncated: bool,
        pos: int
    }

Cancel
======

O método 'cancel' cancela a execução do comando e exclui seu contexto.

.. code-block:: python

    >>> cmd.cancel()
