def setNode(tx, nodeList: list):
    """
    neo4jに登録(nodeを追加)
    ----------
    :param tx:
    :param xliftList:
    :return:
    """
    for index, nodeDict in enumerate(nodeList):
        for label, nameValue in nodeDict.items():
            mergeCypher: str = 'MERGE(:' + label + '{name:\'' + nameValue + '\'})\n'
            print(mergeCypher)
            tx.run(mergeCypher)


def setRelation(tx, relationList: list):
    """
    neo4jに登録(事前に登録したxliftのcookieとv3exを紐付ける)
    ----------
    :param tx:
    :param mainList:
    :return:
    """
    print(' =========== ')
    for i, targetDict in enumerate(relationList):
        for labelRelation, nameList in targetDict.items():
            label, relation = labelRelation.split('_')
            for name in nameList:
                print(label, relation, name)
                m1: str = 'MATCH(l{name:$label})\n'
                m2: str = 'MATCH(n{name:$name})\n'
                m3: str = 'MERGE(l)-[:' + relation + ']-(n)'
                newMerge:str = m1 + m2 + m3
                print(newMerge)
                tx.run(newMerge, label=label, name=name, relation=relation)
