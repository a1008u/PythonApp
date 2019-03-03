def getRelationData(relationFile: str):
    """
    neo4jに登録するファイルからデータを取得する(xlift)
    ----------
    :param fileName:
    :return:
    """
    mainList: list = []
    filePath: str = './text/' + relationFile
    with open(filePath, 'r') as f:
        while True:
            targetLine: list = f.readline().splitlines()

            if not targetLine:
                break

            for target in targetLine:
                label, relation, target = target.split(':')
                targets: list = target.split('|')
                mainList.append({label + '_' + relation: targets})
    return mainList


def getNodeFile(nodeFile: str):
    """
    neo4jに登録するファイルからデータを取得する(xlift-v3ex用)
    ----------
    :param fileName:
    :return:
    """
    mainList: list = []

    filePath: str = './text/node/' + nodeFile
    with open(filePath, 'r') as f:
        while True:
            targetLine: list = f.readline().splitlines()

            if not targetLine:
                break

            for target in targetLine:
                print(target)
                label, name = target.split(':')
                mainList.append({label: name})

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
