// systemを調査する人を探索
MATCH (s:system)<-[:調査]-(m:member) return s,m

// こっちだとダメです
MATCH (s:system)-[:調査]->(m:member) return s,m

// d -> name -> m
MATCH (s{name:'上本 英'})-[*..1]->(m) with s,m
MATCH (d)-[]->(s)
return s,m,d

// departmentを中心に最短ルート2つで表示
MATCH (d{name:'システム企画開発部'})-[*..2]->(s)
return s,d

// ------------------------------------------------------------------
// 同じ結果　
MATCH p=shortestPath(
(s:company {name:'interspace'})-[*]-(m:member{name:'上本 英'})
)
RETURN p

MATCH (s:company {name:'interspace'})-[*]->(x)-[*]->(m:member{name:'上本 英'})
RETURN s,x,m
// ------------------------------------------------------------------

// ------------------------------------------------------------------
// 同じ結果　
MATCH (c:company {name:'interspace'})-[*]->(x)-[*]->(m:member{name:'上本 英'})-[:改修対応]->(sys)
RETURN c,x,m,sys

MATCH (c:company {name:'interspace'})-[*]->(x)-[*]->(m:member{name:'上本 英'}) with c,x,m
MATCH (m)-[:改修対応]->(sys)
RETURN c,x,m,sys

// ------------------------------------------------------------------

// ------------------------------------------------------------------
// 同じ結果　
MATCH (c:company {name:'interspace'})-[*]->(x)-[*]->(m:member) -[:調査]->(s:system)with c,x,m,s
MATCH (m)-[:改修対応]->(s)
RETURN c,x,m,sys


MATCH (c:company {name:'interspace'})-[*]->(x)-[*]->(m:member) with c,x,m
MATCH (m)-[:調査]->(s:system)<-[:改修対応]-(m)
RETURN c,x,m,s
// ------------------------------------------------------------------

// ------------------------------------------------------------------
// isToolsを調査する人
MATCH (s:system{name:'isTools'})<-[:調査]-(x) return s,x

// isToolsを調査して、改修する人の経路を取得
MATCH (s:system{name:'isTools'})<-[:調査{system:'isTools'}]-(x)-[:開発依頼]->(m:member) return s,x,m

MATCH (s:system{name:'isTools'})-[r:調査]-(m:member) with s,r,m
RETURN s.name,m.name

MATCH (s:system{name:'isTools'})-[r:調査]-(m:member) with s,r,m
SET r.system='isTools'
RETURN s,r,m

//
MATCH (s:system{name:'マーチャント管理画面'})<-[:調査]-(m1:member)
MATCH (m1)-[:開発依頼]->(m2:member)
MATCH (m2)-[:改修対応]->(s)
return s,m1,m2
// ------------------------------------------------------------------


// ------------------------------------------------------------------
// indexの使い方。

// memberラベルのnameプロパティでインデックスを設定
CREATE INDEX ON :member(name)

// indexの確認
CREATE INDEX ON :member(name)

// 2つは同じ結果(NodeIndexSeekを先に探しに行くよ)
EXPLAIN MATCH (m:member {name:"上本　英" }) RETURN m
EXPLAIN MATCH (m:member)
  where m.name STARTS WITH  "上本"
RETURN m

// labelをスキャンしている
EXPLAIN MATCH (d:department)
  where d.name STARTS WITH  "ストアフロント事業部"
RETURN d

// ------------------------------------------------------------------



// ------------------------------------------------------------------
// isToolsを軸に深さノード2分のノードを取得する。
MATCH (s:system{name:'isTools'})<-[*1..2]-(k)
return s,k



// isToolsに改修対応する人たち
CREATE INDEX ON :system(name)
EXPLAIN MATCH p= (m:member)-[:改修対応]->(s:system)
where s.name = 'isTools'
return p
// ------------------------------------------------------------------



// ------------------------------------------------------------------
// 企業から所属部署を表示して、memmberを紹介
explain MATCH (m:member{name:'上本 英'}),(c:company{name:'interspace'}),
              p=(m)-[*..3]-(c)
return p
// ------------------------------------------------------------------

// ------------------------------------------------------------------
// ------------------------------------------------------------------

// ------------------------------------------------------------------
// ------------------------------------------------------------------
