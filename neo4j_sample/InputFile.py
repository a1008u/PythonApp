def getFileData(fileName: str):
    """
    neo4jに登録するファイルからデータを取得する(xlift)
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


def getFileDataXlifV3ex(fileName: str):
    """
    neo4jに登録するファイルからデータを取得する(xlift-v3ex用)
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

            for target in targetLine:
                key, value = target.split(',')
                if (key != 'dlog.dmp_id' and value != 'dlog.v3ex'):
                    tempDict: dict = {key: value}
                    mainList.append(tempDict)
    return mainList
