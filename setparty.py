import mysql.connector
import test
"""
오픈 API에서 데이터를 받아와서 정당 테이블을 업데이트
"""



"""
getlist = 'getMemberCurrStateList'#국회의원 현황조회 method_num = 0
getdetail = 'getMemberDetailInfoList'#국회의원 상세조회 method_num = 1
getjungdang = 'getJungDangMemberCurrStateList'#소속정당별 국회의원 목록조회 method_num = 2
getcomm = 'getCommMemberCurrStateList'#소속위원회별 국회의원 목록조회 method_num = 3
getmethod = 'getLoOrProporMemberCurrStateList'#당선방법별 국회의원 목록 정보조회 method_num = 4
getlocalmen = 'getLocalMemberCurrStateList'#지역별 국회의원 목록 정보조회 method_num = 5
getparty = 'getPolySearch' #정당검색 method_num = 6
getlocal = 'getLocalSearch' #지역검색 method_num = 7
getCd = 'getMemberNameInfoList' #이름검색
"""



#"""
def partyset():
    cnx = mysql.connector.connect(user='root', password='flalxlem116',
                                  host='127.0.0.1',
                                  database='dbtest')
    cursor = cnx.cursor()

    #정당 코드와 이름 입력 부분
    table = "party"
    table_column = "(partyCd, partyNm) "
    insert_tuple = "INSERT into " + table + table_column + "values "
    insert_query = insert_tuple + "(%s, %s) " +"ON DUPLICATE KEY UPDATE partyCd = partyCd;"

    items = test.getitem(6)

    for item in items :
        data_partyCd = item['polyCd']
        data_partyNm = item['polyNm']
        cursor.execute(insert_query, (data_partyCd, data_partyNm))
        cnx.commit()
    #"""
    #정당 내 국회의원 수
    #더민당 : 123, 자한당 ; 122, 국민의당 : 38, 정의당 : 6, 무소속 : 11
    #정당별 당대표
    #더민당 : 이해찬, 자한당 : 황교안, 바른미래당 : 손학규, 정의당 : 이정미, 무소속 : NULL
    # 정당별 창당일
    # 더민당 : 2014.03.26, 자한당 : 2017.02.13, 대한애국당 : 2017.07.08, 민주평화당 : 2018.02.07, 민중당 : 2017.10.15 , 바른미래당 : 2018.02.13 , 정의당 : 2012.10.21
    # 정당별 당대표 입력부분
    update_num = "UPDATE party set partyNum = 123, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101182; "#더민당
    cursor.execute(update_num, ("이해찬", "2014.03.26"))
    update_num = "UPDATE party set partyNum = 122, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101186; "#자한당
    cursor.execute(update_num, ("황교안", "2017.02.13"))
    update_num = "UPDATE party set partyNum = 38, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101192; "#바른미래당
    cursor.execute(update_num, ("손학규", "2018.02.13"))
    update_num = "UPDATE party set partyNum = 6, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101180; "#정의당
    cursor.execute(update_num, ("이정미", "2012.10.21"))
    update_num = "UPDATE party set partyNum = 11, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101030;"#무소속
    cursor.execute(update_num, ("없음", "없음"))
    update_num = "UPDATE party set partyNum = 0, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101191;"#민주평화당
    cursor.execute(update_num, ("정동영", "2018.02.07"))
    update_num = "UPDATE party set partyNum = 0, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101190;"#민중당
    cursor.execute(update_num, ("이상규", "2017.10.15"))
    update_num = "UPDATE party set partyNum = 0, partyLeaderCd = %s, dateOfEstablish = %s where partyCd = 101188;"#대한애국당
    cursor.execute(update_num, ("조원진", "2017.07.08"))

    cnx.commit()






