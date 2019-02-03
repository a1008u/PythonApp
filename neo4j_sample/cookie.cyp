
// xlift
MERGE(s:service{id:1,name:'xlift'})
MERGE(l:log{id:1,name:'log',service:'xlift'})
MERGE(c1:cookie{id:1,name:'cookie',cookie:'NUlyI1G7d5Zxb2-'})
MERGE(c2:cookie{id:2,name:'cookie',cookie:'32F2q_H6eMcCsZn'})
MERGE(c3:cookie{id:3,name:'cookie',cookie:'7CvYpyNV8rehfzL'})
MERGE(a1:android{id:1,name:'android',idfa:'78661A2D-D8AB-4280-B10E-77389F0475CA'})
MERGE(a2:android{id:2,name:'android',idfa:'6D4DB644-E55E-4D87-AC10-545779A6E723'})
MERGE(a3:android{id:3,name:'android',idfa:'D0E1437C-75DE-44C7-A8B4-E43FC438DCD6'})
MERGE(s)-[xp:xlift_log]-(l)
MERGE(l)-[r1:cookie]-(c1)
MERGE(l)-[r2:cookie]-(c2)
MERGE(l)-[r3:cookie]-(c3)
MERGE(l)-[r4:android]-(a1)
MERGE(l)-[r5:android]-(a2)
MERGE(l)-[r6:android]-(a3)

// at
MERGE(s:service{id:2,name:'accesstrade'})
MERGE(l:log{id:1,name:'log',service:'accesstrade'})
MERGE(v3ex:v3ex{id:2,name:'v3ex',v3ex:'bac6f38fb9b32933a80211cfeba6ee0f'})
MERGE(s)-[r1:accesstrade_log]-(l)
MERGE(l)-[r2:v3ex]-(v3ex)

// xlift_atのrelation
MATCH(c:cookie{cookie:'32F2q_H6eMcCsZn'}),
     (v3ex:v3ex{v3ex:'bac6f38fb9b32933a80211cfeba6ee0f'})
CREATE(c)-[:xlift_v3ex]->(v3ex)




MATCH p=(c:cookie{cookie:'32F2q_H6eMcCsZn'})-[*1..3]-(v3ex:v3ex{v3ex:'bac6f38fb9b32933a80211cfeba6ee0f'}) RETURN p


MATCH p=(s:service{name:'xlift'})
  -[*1..3]-
(v3ex:v3ex{v3ex:'bac6f38fb9b32933a80211cfeba6ee0f'})
  -[*1..3]-
(s:service{id:2,name:'accesstrade'})
RETURN p


MATCH(s1:service{name:'xlift'})-[]-(s2:service{id:2,name:'accesstrade'}) RETURN s1,s2
