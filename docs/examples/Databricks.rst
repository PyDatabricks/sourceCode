Databricks
==========

Para instanciar a classe Databricks, é preciso passar o token e o link.

.. code-block:: python

    >>> from databricks import Databricks
    >>> token = "sample-token"
    >>> url = "sample-link"
    >>> db = Databricks(token, url)

Get Clusters
============

O método retorna uma variável do tipo databricks.types.DatabricksListClustersResponseType todos os clusters

.. code-block:: python

    >>> from databricks.types import DatabricksListClustersResponseType
    >>> 
    >>> clusters: DatabricksListClustersResponseType = db.listClusters()
    >>> print(clusters)
    {
        'clusters': []
    }
