from neo4j.v1 import GraphDatabase, Driver


def clearDb(tx):
    """
    neo4jを空にする
    ----------
    :param tx:
    :return:
    """
    tx.run('MATCH (n) DETACH DELETE n')


def getFileData(fileName: str):
    """
    neo4jに登録するファイルからデータを取得する
    ----------
    :param fileName:
    :return:
    """
    mainList: list = []
    with open(fileName, 'r') as f:
        while True:
            targetLine: list = f.readline().splitlines()

            if not targetLine:
                break

            tempList: list = []
            for target in targetLine:
                targets: list = target.split('|')
                for t in targets:
                    key, value = t.split(':')
                    tempList.append({key: value})

            mainList.append(tempList)
    return mainList


def setData(tx, mainList):
    """
    neo4jに登録
    ----------
    :param tx:
    :param mainList:
    :return:
    """
    for targetList in mainList:
        mainKey: str
        mainValue: str
        for i, targetDict in enumerate(targetList):
            if i == 0:
                for key, value in targetDict.items():
                    mainKey = key
                    mainValue = value
            else:
                if mainKey == 'cookie':
                    for key, value in targetDict.items():
                        id: str = '1' if key == 'cookie' else '3' if key == 'android_idfa' else '2'
                        cookieOrIdfa: str = 'cookie' if key == 'cookie' else 'idfa'
                        m1: str = 'MERGE(c1:' + mainKey + '{id:1,name:\'' + mainKey + '\',cookie:$mainValue})\n'
                        m2: str = 'MERGE(c2:' + key + '{id:' + id + ',name:\'' + key + '\',' + cookieOrIdfa + ':$value})\n'
                        m3: str = 'MERGE(c1)-[r:' + mainKey + '_' + key + ']-(c2)'
                        newMerge:str = m1 + m2 + m3
                        print(newMerge)
                        tx.run(newMerge, mainValue=mainValue, value=value)
                else:
                    break


if __name__ == '__main__':
    driver: Driver = GraphDatabase.driver('bolt://localhost:7687')
    with driver.session() as session:
        session.write_transaction(clearDb)
        mainList: list = getFileData('./test.rtf')
        session.write_transaction(setData, mainList)



