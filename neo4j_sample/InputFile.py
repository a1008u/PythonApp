def getFileData(fileName: str, searchList: list):
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
                    if 'cookie' == key and value in searchList:
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
                xlift, v3ex = target.split(',')
                if (xlift != 'dlog.dmp_id' and v3ex != 'dlog.v3ex'):
                    tempDict: dict = {xlift: v3ex}
                    mainList.append(tempDict)
    return mainList


def getFileDataForSearchXlift(fileName: str):
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
                xlift, v3ex = target.split(',')
                if (xlift != 'dlog.dmp_id' and v3ex != 'dlog.v3ex'):
                    mainList.append(xlift)
    return mainList
