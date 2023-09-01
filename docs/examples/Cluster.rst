Clusters
========

A classe Cluster deve receber uma instância da classe Databricks, junto com o id do cluster.

.. code-block:: python

    >>> from databricks import Databricks
    >>> from databricks.compute.cluster import Cluster
    >>> 
    >>> db = Databricks("<token>", "<url>")
    >>> cluster = Cluster(db, "<cluster-id>")


forceStart
==========

O método 'forceStart' força o  o cluster, enquanto o cluster não estiver no estado de running, o código continuará no laço.

.. code-block:: python

    >>> cluster.forceStart()


getInfo
=======

O método 'getInfo' retorna