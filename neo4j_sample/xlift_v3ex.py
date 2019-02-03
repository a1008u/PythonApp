from neo4j.v1 import GraphDatabase, Driver
from neo4j_sample import DeleteNeo4j as clear
from neo4j_sample import InputFile as inputFile
from neo4j_sample.Input_neo4j import setDataxliftv3exRelation

if __name__ == '__main__':
    driver: Driver = GraphDatabase.driver('bolt://localhost:7687')
    with driver.session() as session:
        session.write_transaction(clear.clearDb)
        mainList: list = inputFile.getFileDataXlifV3ex('./xlift-v3ex.csv')
        session.write_transaction(setDataxliftv3exRelation, mainList)
