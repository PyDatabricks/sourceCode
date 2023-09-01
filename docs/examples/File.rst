File
====


A classe 'File' extende a classe 'Repository' e recebe 3 atributos:
    + databricks: Databricks
        Objeto da classe Databricks.

    + path: str
        Caminho para o arquivo.
    
    + encoding(optional): str
        Tipo de codificação do arquivo. 'utf-8' por default.

.. code-block:: python

    >>> from databricks.fileManagement.dbfs import File

    >>> file = File(databricks, "<path>", "latin-1")

Move
====

O método 'move' move o arquivo para outro caminho.
    Params:
        + destination: str
            Caminho de destino do arquivo

.. code-block:: python

    >>> file.move("<destination>")

Upload
======

O método 'upload' envia o conteúdo de um arquivo para o databricks.
    Params:
        + content: str
            Conteúdo do arquivo.
        
        + overwrite(optional): bool
            Indica se o arquivo será sobre escrito. False como default

.. code-block:: python

    >>> file.upload("<content>")


Get Partial Content
===================

O método 'getPartialContent' obtem 1Mb do conteúdo do arquivo codificado na base-64.
    Params:
        + offset: int
            Indica qual parte do arquivo será lida.

obs: Caso queira o conteúdo inteiro, usar o método 'getContent'.

.. code-block:: python

    >>> print(file.getPartialContent("<content>"))
    {
        bytes_read: int,
        data: str
    }

Get Content
===========

O método 'getContent' retorna todo o conteúdo do arquivo no formato de lista.
    Params:
        + workers(optional): int
            Indica quantas threads serão criadas para fazer o download do conteúdo do arquivo. Warning: Não aumentar muito o valor.

.. code-block:: python

    >>> print(file.getContent())
    ['...', ..., '...']

Download
========

O método 'download' baixa o arquivo do databricks para a máquina local.
    Params:
        + to: str
            Caminho que o arquivo será baixado.
        + workers(optional): int
            Indica quantas threads serão criadas para fazer o download do arquivo. Warning: Não aumentar muito o valor.

.. code-block:: python

    >>> file.download("<download-path>")

Delete
======

O metodo 'delete' remove o arquivo da memória interna do cluster.
    Params:
        - recursive(optional): bool
            Esse parâmetro indica se os arquivos internos serão excluídos.
.. code-block:: python

    >>> file.delete()

Get Properties
==============

O método 'getProperties' retorna as propriedades do arquivo.

.. code-block:: python

    >>> print(file.getProperties())
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

    >>> print(file.isDir())
    True

Is File
=======

O método 'isFile' retorna True, caso o caminho indicado seja um arquivo.

.. code-block:: python

    >>> print(file.isFile())
    False
