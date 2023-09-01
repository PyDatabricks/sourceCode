Clusters
========

A classe Cluster deve receber uma instância da classe Databricks, junto com o id do cluster.

.. code-block:: python

    >>> from databricks import Databricks
    >>> from databricks.compute.cluster import Cluster
    >>> 
    >>> db = Databricks("<token>", "<url>")
    >>> cluster = Cluster(db, "<cluster-id>")


Force Start
===========

O método 'forceStart' força o início do cluster, enquanto o cluster não estiver no estado de running, o código continuará no laço.

.. code-block:: python

    >>> cluster.forceStart()


Get Info
========

O método 'getInfo' retorna informações sobre o cluster.

.. code-block:: python

    >>> print(cluster.getInfo())
    {
        cluster_name: ''
        spark_version: ''
        spark_conf: { ... }
        azure_attributes: { ... }
        ...
    }


Restart
=======

O método 'restart' reinicia o cluster.

.. code-block:: python

    >>> cluster.restart()


Start
=====

O método 'start' inicia o cluster. Este método só funciona caso o cluster esteja no estado 'TERMINATED', caso contrário, utilize o método 'forceStart'.

.. code-block:: python

    >>> cluster.start()



Terminate
=========

O método 'terminate' envia uma chamada de desligamento para o cluster.

.. code-block:: python

    >>> cluster.terminate()
