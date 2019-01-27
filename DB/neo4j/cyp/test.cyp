// MERGE(a) DETACH DELETE a;

// cookie:5gmu8MkoWe5YnCe|android_idfa:14FC97A8-5B91-4B72-B431-EFABEE37DA8E
MERGE(c:cookie{id:1,name:'cookie',cookie:'5gmu8MkoWe5YnCe'})
MERGE(aidfa:android{id:3,name:'android',idfa:'14FC97A8-5B91-4B72-B431-EFABEE37DA8E'})
MERGE(c)-[r:cookie_android]-(aidfa)
RETURN c,aidfa


// cookie:p-kbg34KrmFqW6j|cookie:EY5bh1nM1SxBatk
MERGE(c1:cookie{id:1,name:'cookie',cookie:'p-kbg34KrmFqW6j'})
MERGE(c2:cookie{id:1,name:'cookie',cookie:'EY5bh1nM1SxBatk'})
MERGE(c1)-[r:cookie_cookie]-(c2)
RETURN c1,c2

/*
cookie:TOPvpD8lbTBhzW0|
cookie:nvPbqfPrB5yWY3k|
android_idfa:3656F603-EB2C-4CC4-837E-FCDFFDE00177|
android_idfa:2AC471E3-BA1F-4174-8B0E-CEB3A1CEA24D|
android_idfa:B8CFD773-80D1-4BB1-A4BD-F18187F77BBF|
android_idfa:E0E7E0E8-C0BE-4214-A2F3-AF570042E24C|
android_idfa:81AEFA38-89C8-495F-B986-34409E47DED5|
android_idfa:9E975C21-90B6-4DB9-8AE5-A10D0CE6DD9C|
android_idfa:CDC94C51-89FB-432C-A745-CAB4BCFE903E|
android_idfa:0A44983F-36C1-4AD0-831F-F29E103FF507|
android_idfa:5C354F18-3A2E-4414-A747-C1D322D3C020|
android_idfa:F78A0B10-3765-4980-873F-DF2DDDBD304D|
android_idfa:307F9E8C-98A7-46F3-ADF1-E306AE4349A6|
android_idfa:DF74C0C2-EAAB-4EBD-9BC6-709C54CE52CF|
android_idfa:B99030DC-C699-4C7B-9945-946A745A85A9|
android_idfa:3FF968FE-939B-4F09-8AC0-058EFEA5901D|
android_idfa:AEB55251-E83E-4F62-B4FC-438FBFA51288|
android_idfa:F15ADEEE-36DB-44B8-8EF8-89D9AF73322E|
android_idfa:25FDEE9A-5335-4BD3-A85E-98333500145D|
android_idfa:735277AB-53A6-4C78-A1EB-52A8B2C88F83|
android_idfa:3504FEB2-9535-4290-A5C9-7E724CF92F5E|
android_idfa:69C0AEB3-15A1-4414-ADE2-684B08883F60|
android_idfa:8E89E07F-E998-4D5C-8DB6-D4192AFBEB06|
android_idfa:9A90CD8F-C894-4194-93A2-2626C0AF8BA6|
android_idfa:06E09BF1-888D-4F04-9A14-49E59F0E84DA|
android_idfa:C876D4BD-E04B-4BBB-B0BB-771761D43C5D|
android_idfa:A0CF6D1F-C044-45DE-9300-7FADA1D8784A|
android_idfa:879DE8A2-717C-478D-AC80-3260C21497E9|
android_idfa:22CC6215-484E-43CA-A577-710DE9D0BF8B|
android_idfa:143CDE15-252B-4B9E-B9FF-5A29C892427E|
android_idfa:CFC90FC8-7C72-4C03-9D3F-84834EF2AB91|
android_idfa:A066BE78-C9B8-466D-9867-4022BEF782B6|
android_idfa:5BC3244C-01D9-4E75-B4F0-A8088997D31B|
android_idfa:6C1C28C5-CAE5-4BB9-A54A-F7D6B1AA46C2|
android_idfa:BCDC3DE4-8B51-4D31-81E9-45E943F40F94|
android_idfa:6BEE1F22-AADE-4891-9F0B-AA377360C024|
android_idfa:B2635F27-AC56-4A94-96B8-F5CAD9A8AB88|
android_idfa:9498653A-2901-443E-9E4F-A643242DC53E|
android_idfa:78B3353F-D96B-4A28-B7D2-608318D1B93E|
android_idfa:968A8348-0F7E-4CF1-84FF-8F25E801D7FD
*/
MERGE(c1:cookie{id:1,name:'cookie',cookie:'TOPvpD8lbTBhzW0'})
MERGE(c2:cookie{id:1,name:'cookie',cookie:'nvPbqfPrB5yWY3k'})
MERGE(aidfa1:android{id:3,name:'android',idfa:'3656F603-EB2C-4CC4-837E-FCDFFDE00177'})
MERGE(aidfa2:android{id:3,name:'android',idfa:'2AC471E3-BA1F-4174-8B0E-CEB3A1CEA24D'})
MERGE(aidfa3:android{id:3,name:'android',idfa:'B8CFD773-80D1-4BB1-A4BD-F18187F77BBF'})
MERGE(aidfa4:android{id:3,name:'android',idfa:'E0E7E0E8-C0BE-4214-A2F3-AF570042E24C'})
MERGE(aidfa5:android{id:3,name:'android',idfa:'81AEFA38-89C8-495F-B986-34409E47DED5'})
MERGE(aidfa6:android{id:3,name:'android',idfa:'9E975C21-90B6-4DB9-8AE5-A10D0CE6DD9C'})
MERGE(aidfa7:android{id:3,name:'android',idfa:'CDC94C51-89FB-432C-A745-CAB4BCFE903E'})
MERGE(aidfa8:android{id:3,name:'android',idfa:'0A44983F-36C1-4AD0-831F-F29E103FF507'})
MERGE(aidfa9:android{id:3,name:'android',idfa:'5C354F18-3A2E-4414-A747-C1D322D3C020'})
MERGE(aidfa10:android{id:3,name:'android',idfa:'F78A0B10-3765-4980-873F-DF2DDDBD304D'})
MERGE(aidfa11:android{id:3,name:'android',idfa:'B99030DC-C699-4C7B-9945-946A745A85A9'})
MERGE(aidfa12:android{id:3,name:'android',idfa:'3FF968FE-939B-4F09-8AC0-058EFEA5901D'})
MERGE(aidfa13:android{id:3,name:'android',idfa:'AEB55251-E83E-4F62-B4FC-438FBFA51288'})
MERGE(aidfa14:android{id:3,name:'android',idfa:'F15ADEEE-36DB-44B8-8EF8-89D9AF73322E'})
MERGE(aidfa15:android{id:3,name:'android',idfa:'25FDEE9A-5335-4BD3-A85E-98333500145D'})
MERGE(aidfa16:android{id:3,name:'android',idfa:'735277AB-53A6-4C78-A1EB-52A8B2C88F83'})
MERGE(aidfa17:android{id:3,name:'android',idfa:'3504FEB2-9535-4290-A5C9-7E724CF92F5E'})
MERGE(aidfa18:android{id:3,name:'android',idfa:'69C0AEB3-15A1-4414-ADE2-684B08883F60'})
MERGE(aidfa19:android{id:3,name:'android',idfa:'8E89E07F-E998-4D5C-8DB6-D4192AFBEB06'})
MERGE(aidfa20:android{id:3,name:'android',idfa:'9A90CD8F-C894-4194-93A2-2626C0AF8BA6'})
MERGE(aidfa21:android{id:3,name:'android',idfa:'06E09BF1-888D-4F04-9A14-49E59F0E84DA'})
MERGE(aidfa22:android{id:3,name:'android',idfa:'C876D4BD-E04B-4BBB-B0BB-771761D43C5D'})
MERGE(aidfa23:android{id:3,name:'android',idfa:'A0CF6D1F-C044-45DE-9300-7FADA1D8784A'})
MERGE(aidfa24:android{id:3,name:'android',idfa:'879DE8A2-717C-478D-AC80-3260C21497E9'})
MERGE(aidfa25:android{id:3,name:'android',idfa:'22CC6215-484E-43CA-A577-710DE9D0BF8B'})
MERGE(aidfa26:android{id:3,name:'android',idfa:'143CDE15-252B-4B9E-B9FF-5A29C892427E'})
MERGE(aidfa27:android{id:3,name:'android',idfa:'CFC90FC8-7C72-4C03-9D3F-84834EF2AB91'})
MERGE(aidfa28:android{id:3,name:'android',idfa:'A066BE78-C9B8-466D-9867-4022BEF782B6'})
MERGE(aidfa29:android{id:3,name:'android',idfa:'5BC3244C-01D9-4E75-B4F0-A8088997D31B'})
MERGE(aidfa30:android{id:3,name:'android',idfa:'6C1C28C5-CAE5-4BB9-A54A-F7D6B1AA46C2'})
MERGE(aidfa31:android{id:3,name:'android',idfa:'BCDC3DE4-8B51-4D31-81E9-45E943F40F94'})
MERGE(aidfa32:android{id:3,name:'android',idfa:'6BEE1F22-AADE-4891-9F0B-AA377360C024'})
MERGE(aidfa33:android{id:3,name:'android',idfa:'B2635F27-AC56-4A94-96B8-F5CAD9A8AB88'})
MERGE(aidfa34:android{id:3,name:'android',idfa:'9498653A-2901-443E-9E4F-A643242DC53E'})
MERGE(aidfa35:android{id:3,name:'android',idfa:'78B3353F-D96B-4A28-B7D2-608318D1B93E'})
MERGE(aidfa36:android{id:3,name:'android',idfa:'968A8348-0F7E-4CF1-84FF-8F25E801D7FD'})
MERGE(c1)-[r:cookie_cookie]-(c2)
MERGE(c1)-[r1:cookie_android]-(aidfa1)
MERGE(c1)-[r2:cookie_android]-(aidfa2)
MERGE(c1)-[r3:cookie_android]-(aidfa3)
MERGE(c1)-[r4:cookie_android]-(aidfa4)
MERGE(c1)-[r5:cookie_android]-(aidfa5)
MERGE(c1)-[r6:cookie_android]-(aidfa6)
MERGE(c1)-[r7:cookie_android]-(aidfa7)
MERGE(c1)-[r8:cookie_android]-(aidfa8)
MERGE(c1)-[r9:cookie_android]-(aidfa9)
MERGE(c1)-[r10:cookie_android]-(aidfa10)
MERGE(c1)-[r11:cookie_android]-(aidfa11)
MERGE(c1)-[r12:cookie_android]-(aidfa12)
MERGE(c1)-[r13:cookie_android]-(aidfa13)
MERGE(c1)-[r14:cookie_android]-(aidfa14)
MERGE(c1)-[r15:cookie_android]-(aidfa15)
MERGE(c1)-[r16:cookie_android]-(aidfa16)
MERGE(c1)-[r17:cookie_android]-(aidfa17)
MERGE(c1)-[r18:cookie_android]-(aidfa18)
MERGE(c1)-[r19:cookie_android]-(aidfa19)
MERGE(c1)-[r20:cookie_android]-(aidfa20)
MERGE(c1)-[r21:cookie_android]-(aidfa21)
MERGE(c1)-[r22:cookie_android]-(aidfa22)
MERGE(c1)-[r23:cookie_android]-(aidfa23)
MERGE(c1)-[r24:cookie_android]-(aidfa24)
MERGE(c1)-[r25:cookie_android]-(aidfa25)
MERGE(c1)-[r26:cookie_android]-(aidfa26)
MERGE(c1)-[r27:cookie_android]-(aidfa27)
MERGE(c1)-[r28:cookie_android]-(aidfa28)
MERGE(c1)-[r29:cookie_android]-(aidfa29)
MERGE(c1)-[r30:cookie_android]-(aidfa30)
MERGE(c1)-[r31:cookie_android]-(aidfa31)
MERGE(c1)-[r32:cookie_android]-(aidfa32)
MERGE(c1)-[r33:cookie_android]-(aidfa33)
MERGE(c1)-[r34:cookie_android]-(aidfa34)
MERGE(c1)-[r35:cookie_android]-(aidfa35)
MERGE(c1)-[r36:cookie_android]-(aidfa36)
RETURN c1


// cookie:mbsfP9N75eIbdaw|android_idfa:4D2D3EF6-6E16-4864-8082-8D45B9176DD0|ios_idfa:E819CCAA-1032-4FEE-8A3D-5C50F0E241F5
MERGE(c:cookie{id:1,name:'cookie',cookie:'mbsfP9N75eIbdaw'})
MERGE(iosidfa:ios{id:3,name:'ios',idfa:'E819CCAA-1032-4FEE-8A3D-5C50F0E241F5'})
MERGE(aidfa:android{id:3,name:'android',idfa:'4D2D3EF6-6E16-4864-8082-8D45B9176DD0'})
MERGE(c)-[r1:cookie_ios]-(iosidfa)
MERGE(c)-[r2:cookie_android]-(aidfa)
RETURN c,iosidfa,aidfa
