Directory
=========

A classe 'Directory' extende a classe 'Repository' e recebe 2 atributos:
    + databricks: Databricks
        Objeto da classe Databricks.

    + path: str
        Caminho para o diretório.

.. code-block:: python

    >>> from databricks.fileManagement.dbfs.directory import Directory

    >>> dbDir = Directory(databricks, "<path>")


Create
======

O método 'create' cria um novo diretório.

.. code-block:: python

    >>> dbDir.create()


List Dir
========

O método 'listDir' lista os sub diretórios do diretório atual.

.. code-block:: python

    >>> print(dbDir.listDir())
    {
        "files": [
            {
                "path": str
                "is_dir": bool
                "file_size": int
                "modification_time": int
            },
            ...
            {
                "path": str
                "is_dir": bool
                "file_size": int
                "modification_time": int
            }
        ]
    }


Download
========

O método 'download' baixa o diretório, juntamente com seus sub arquivos, para o caminho indicado.
    Params:
        + to: str
            Caminho que o arquivo será baixado.

        + encoding(optional): str
            Tipo de codificação do arquivo. 'utf-8' como default.

        + workers(optional): int
            Indica quantas threads serão criadas para fazer o download do arquivo. Warning: Não aumentar muito o valor.
            
.. code-block:: python

    >>> dbDir.download("<download-path>", "<encoding>", "<workers-number>")

Delete
======

O metodo 'delete' remove o diretório da memória interna do cluster.
    Params:
        - recursive(optional): bool
            Esse parâmetro indica se os sub diretórios serão excluídos.

.. code-block:: python

    >>> dbDir.delete()

Get Properties
==============

O método 'getProperties' retorna as propriedades do diretório.

.. code-block:: python

    >>> print(dbDir.getProperties())
    {
        path: str,
        is_dir: bool,
        file_size: int,
        modification_time: int
    }

Is Dir
======

O método 'isDir' retorna True, caso o caminho indicado seja um diretório.

.. code-block:: python

    >>> print(dbDir.isDir())
    True

Is File
=======

O método 'isFile' retorna True, caso o caminho indicado seja um arquivo.

.. code-block:: python

    >>> print(dbDir.isFile())
    False

