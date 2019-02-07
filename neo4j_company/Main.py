from neo4j.v1 import GraphDatabase, Driver
from neo4j_company import DeleteNeo4j as clear
from neo4j_company import Input_neo4j as input_neo4j
from neo4j_company import InputFile as inputFile

# MATCH p=(x:log)-[*1..2]->(c:v3ex) RETURN p 結果の確認用
if __name__ == '__main__':
    driver: Driver = GraphDatabase.driver('bolt://localhost:7687')
    with driver.session() as session:
        session.write_transaction(clear.clearDb)

        nodeList: list = inputFile.getNodeFile('node.txt')
        print(nodeList)
        session.write_transaction(input_neo4j.setNode, nodeList)


        relationList: list = inputFile.getRelationData('relation.txt')
        print(relationList)
        session.write_transaction(input_neo4j.setRelation, relationList)

        # xliftList: list = inputFile.getFileData('./test.rtf', searchList)
        # session.write_transaction(input_neo4j.setDataXlift, xliftList)

        # xliftV3exList: list = inputFile.getFileDataXlifV3ex('./xlift-v3ex.csv')
        # session.write_transaction(input_neo4j.setDataxRelation, xliftV3exList)

        # print(xliftList)
        # print(len(xliftList))



