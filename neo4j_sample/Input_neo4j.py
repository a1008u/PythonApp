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


def setDataXlift(tx, mainList):
    """
    neo4jに登録
    ----------
    :param tx:
    :param mainList:
    :return:
    """
    for index, targetList in enumerate(mainList):

        targetListlength: int = len(targetList)
        m2List: list = []
        m3List: list = []
        for i, targetDict in enumerate(targetList):

            # cypher作成
            for key, value in targetDict.items():
                id: str = '1' if key == 'cookie' else '3' if key == 'android_idfa' else '2'
                cookieOrIdfa: str = 'cookie' if key == 'cookie' else 'idfa'

                m2: str = 'MERGE(c' + str(i) + ':' + key + '{id:' + id + ',name:\'' + key + '\',' + cookieOrIdfa + ':\'' + value + '\'})\n'
                m2List.append(m2)

                m3: str = 'MERGE(l)-[:xliftlog' + '_' + key + ']-(c' + str(i) + ')\n'
                m3List.append(m3)

            # commit
            if i+1 == targetListlength:
                cypher: str = 'MERGE(l:log{id:' + str(index) + ',name:\'xlift_log\',service:\'xlift\'})\n'

                for m2 in m2List:
                    cypher += m2

                for m3 in m3List:
                    cypher += m3

                print(cypher)
                tx.run(cypher)




def setDataxliftv3exRelation(tx, mainList):
    """
    neo4jに登録(xlift-v3ex)
    ----------
    :param tx:
    :param mainList:
    :return:
    """
    for i, targetDict in enumerate(mainList):
            print(targetDict)
            for xliftValue, v3exValue in targetDict.items():
                m1: str = 'MERGE(c1:xlift_cookie{id:1,name:\'cookie\',cookie:$xliftValue})\n'
                m2: str = 'MERGE(c2:v3ex{id:1,name:\'v3ex\',cookie:$v3exValue})\n'
                m3: str = 'MERGE(c1)-[x:xlift_v3ex]-(c2)'
                newMerge:str = m1 + m2 + m3
                print(newMerge)
                tx.run(newMerge, xliftValue=xliftValue, v3exValue=v3exValue)

def setDataxRelation(tx, mainList):
    """
    neo4jに登録(事前に登録したxliftのcookieとv3exを紐付ける)
    ----------
    :param tx:
    :param mainList:
    :return:
    """
    for i, targetDict in enumerate(mainList):
        print(targetDict)
        for xliftValue, v3exValue in targetDict.items():
            m1: str = 'MATCH(c:cookie{cookie:$xliftValue})\n'
            m2: str = 'MERGE(c2:v3ex{id:1,name:\'v3ex\',cookie:$v3exValue})\n'
            m3: str = 'MERGE(c)-[x:xlift_v3ex]-(c2)'
            newMerge:str = m1 + m2 + m3
            print(newMerge)
            tx.run(newMerge, xliftValue=xliftValue, v3exValue=v3exValue)
