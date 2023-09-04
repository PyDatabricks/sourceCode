Databricks
==========

A classe Databricks recebe 2 atributos:
    + token: str
        Chave de acesso obtido dentro da plataforma databricks.

    + link: str
        Link para a plataforma.

.. code-block:: python

    >>> from databricks.databricks import Databricks
    >>> token = "<token>"
    >>> url = "<url>"
    >>> db = Databricks(token, url)

Get Clusters
============

O método 'getClusters' retorna uma variável do tipo databricks.types.DatabricksTypes.DatabricksListClustersResponseType todos os clusters

.. code-block:: python
    
    >>> clusters = db.listClusters()
    >>> print(clusters)
    {
        'clusters': []
    }
