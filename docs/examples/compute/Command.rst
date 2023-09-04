Command
=======

A classe 'Command' recebe 2 atributos:
    + command: str
        Comando a ser executado

    + context: Context
        Contexto em que o comando será executado

- obs: Caso o objetivo seja apenas executar um comando e obter seu resultado, tente usar a classe 'commandExecution'.

.. code-block:: python

    >>> from databricks.compute.commandExecution import Command
    
    >>> command = Command("<command>", context)


Run
===

O método 'run' executa o comando.

.. code-block:: python

    >>> print(command.run())
    {
        id: str
    }


Get Status
==========

O método 'getStatus' retorna o estado do comando em questão.

.. code-block:: python

    >>> print(command.getStatus())
    {
        id: str,
        status: str,
        results: { ... }
    }


Cancel
======

O método 'cancel' cancela a execução de um comando.

.. code-block:: python

    >>> command.cancel()
