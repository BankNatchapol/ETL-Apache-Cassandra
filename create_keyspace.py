from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.execute("""CREATE KEYSPACE IF NOT EXISTS udacity WITH REPLICATION = { 
                      'class' : 'SimpleStrategy', 
                      'replication_factor' : 3   }
                """)
