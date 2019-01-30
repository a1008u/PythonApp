MERGE(c:company{id:1,name:'インタースペース',category:'ad(asp)'})
MERGE(ca:systemdev{id:1,name:'システム開発',category:'アフィリエイト開発'})
MERGE(c)-[r:company_department]->(ca)


MERGE(di:division{id:1,name:'第１システム',category:'アフィリエイト開発全般'})
MERGE(di:division{id:2,name:'第２システム',category:'SFA開発全般'})
MERGE(di:division{id:3,name:'インフラ',category:'インフラ'})

MATCH(ca:systemdev{id:1}),(di:division{id:1})CREATE(ca)-[:department_division]->(di)
MATCH(ca:systemdev{id:1}),(di:division{id:2})CREATE(ca)-[:department_division]->(di)
MATCH(ca:systemdev{id:1}),(di:division{id:3})CREATE(ca)-[:department_division]->(di)


MERGE(per:person{id:1,name:'Y',position:'???'})
MERGE(per:person{id:2,name:'T',position:'マネージャー'})
MERGE(per:person{id:3,name:'TU',position:'マネージャー'})
MERGE(per:person{id:4,name:'O',position:'サブマネージャー'})
MERGE(per:person{id:5,name:'A',position:'サブマネージャー'})
MERGE(per:person{id:6,name:'KO',position:'スペシャリストlevel1'})
MERGE(per:person{id:7,name:'TA',position:'リーダー'})
MERGE(per:person{id:8,name:'KA',position:'スペシャリストlevel1'})
MERGE(per:person{id:9,name:'IT',position:'リードエンジニア'})
MERGE(per:person{id:10,name:'KA2',position:'リードエンジニア'})
MERGE(per:person{id:11,name:'AU',position:'リードエンジニア'})
MERGE(per:person{id:12,name:'YU',position:'エンジニア'})
MERGE(per:person{id:13,name:'SHI',position:'エンジニア'})
MERGE(per:person{id:14,name:'YAMA',position:'エンジニア'})
MERGE(per:person{id:15,name:'HAYA',position:'エンジニア'})


MATCH(di:division{id:1}),(per:person{id:3})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:4})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:6})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:7})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:8})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:9})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:10})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:11})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:12})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:13})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:14})CREATE(di)-[:belongs]->(per)
MATCH(di:division{id:1}),(per:person{id:15})CREATE(di)-[:belongs]->(per)

MATCH(di:division{id:1}),
     (per3:person{id:3}),
     (per4:person{id:4}),
     (per6:person{id:6}),
     (per7:person{id:7}),
     (per8:person{id:8}),
     (per9:person{id:9}),
     (per10:person{id:10}),
     (per11:person{id:11}),
     (per12:person{id:12}),
     (per13:person{id:13}),
     (per14:person{id:14}),
     (per15:person{id:15})
CREATE(di)-[:belongs]->(per),
      (di)-[:belongs]->(per3),
      (di)-[:belongs]->(per4),
      (di)-[:belongs]->(per5),
      (di)-[:belongs]->(per6),
      (di)-[:belongs]->(per7),
      (di)-[:belongs]->(per8),
      (di)-[:belongs]->(per9),
      (di)-[:belongs]->(per10),
      (di)-[:belongs]->(per11),
      (di)-[:belongs]->(per12),
      (di)-[:belongs]->(per13),
      (di)-[:belongs]->(per14),
      (di)-[:belongs]->(per15)


MATCH(per1:person{id:11}),(per2:person{id:12})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:10}),(per2:person{id:15})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:7}),(per2:person{id:13})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:7}),(per2:person{id:14})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:4}),(per2:person{id:11})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:4}),(per2:person{id:9})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:4}),(per2:person{id:7})CREATE(per1)-[:menter]->(per2)
MATCH(per1:person{id:8}),(per2:person{id:10})CREATE(per1)-[:menter]->(per2)



MATCH(di:division{id:1}),
     (per:person{id:11}),
     (per2:person{id:6})
CREATE(di)-[:belongs]->(per),
      (di)-[:belongs]->(per2)

