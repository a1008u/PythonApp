from neo4j.v1 import GraphDatabase, Driver
from neo4j_sample import DeleteNeo4j as clear
from neo4j_sample import Input_neo4j as input_neo4j
from neo4j_sample import InputFile as inputFile

# MATCH p=(x:log)-[*1..2]->(c:v3ex) RETURN p 結果の確認用
if __name__ == '__main__':
    driver: Driver = GraphDatabase.driver('bolt://localhost:7687')
    with driver.session() as session:
        session.write_transaction(clear.clearDb)
        mainList: list = inputFile.getFileData('./test.rtf')
        # session.write_transaction(setData, mainList)
        session.write_transaction(input_neo4j.setDataXlift, mainList)

        mainList: list = inputFile.getFileDataXlifV3ex('./xlift-v3ex.csv')
        session.write_transaction(input_neo4j.setDataxRelation, mainList)

