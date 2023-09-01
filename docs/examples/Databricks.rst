Databricks
==========

A classe Databricks recebe 2 atributos:
    + token: str
        Chave de acesso obtido dentro da plataforma databricks.
        
    + link: str
        Link para a plataforma.

.. code-block:: python

    >>> from databricks import Databricks
    >>> token = "<token>"
    >>> url = "<url>"
    >>> db = Databricks(token, url)

Get Clusters
============

O método 'getClusters' retorna uma variável do tipo databricks.types.DatabricksListClustersResponseType todos os clusters

.. code-block:: python

    >>> from databricks.types import DatabricksListClustersResponseType
    >>> 
    >>> clusters: DatabricksListClustersResponseType = db.listClusters()
    >>> print(clusters)
    {
        'clusters': []
    }
