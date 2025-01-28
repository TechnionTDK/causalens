from py2neo import Graph
def connect_neo4j(uri, user, password):
    """
    Connects to a Neo4j database and returns a Graph object.
    """
    graph = Graph(uri, auth=(user, password))
    return graph

def sample_cypher_query(graph):
    query = """
    MATCH (n)
    RETURN n
    LIMIT 5
    """
    return graph.run(query).data()
    
if __name__ == "__main__":
    graph = connect_neo4j("bolt://localhost:7687", "neo4j", "12345678")
    data = sample_cypher_query(graph)
    print(data)