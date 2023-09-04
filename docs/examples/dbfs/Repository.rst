Repository
==========

A classe 'Repository' recebe 2 atributos:
    + databricks: Databricks
        Objeto da classe Databricks.

    + path: str
        Caminho para o repositório.

.. code-block:: python

    >>> from databricks.fileManagement.dbfs import Repository

    >>> repo = Repository(databricks, "<path>")


Delete
======

O metodo 'delete' remove o repositório da memória interna do cluster.
    Params:
        - recursive(optional): bool
            Esse parâmetro indica se os arquivos internos serão excluídos.

.. code-block:: python

    >>> repo.delete()

Get Properties
==============

O método 'getProperties' retorna as propriedades do repositório.

.. code-block:: python

    >>> print(repo.getProperties())
    {
        path: str,
        is_dir: bool,
        file_size: int,
        modification_time: int
    }

Is Dir
======

O método 'isDir' retorna True, caso o repositório seja um diretório.

.. code-block:: python

    >>> print(repo.isDir())
    True

Is File
=======

O método 'isFile' retorna True, caso o repositório seja um arquivo.

.. code-block:: python

    >>> print(repo.isFile())
    False
