def clearDb(tx):
    """
    neo4jを空にする
    ----------
    :param tx:
    :return:
    """
    tx.run('MATCH (n) DETACH DELETE n')
