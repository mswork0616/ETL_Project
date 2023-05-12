# 비동기 요청 가능한 html 파일 실행이 주 목적

import pandas as pd
import json, datetime
from flask import Flask, request, render_template, redirect
from etlDTO import EtlDTO
from etlDAO import EtlDAO

app = Flask(__name__)

# http://127.0.0.1:5000
@app.route("/")
def intro():
    print("etlcrud.py의 intro() 함수 실행 -----------------------------------------------")
    return render_template("etlcrud.html")

# 1. 영화 등록 ----------------------------------------------------------------------------------------------------------
@app.route('/insert', methods=['post'])
def insert():
    id = request.form.get("id")
    title = request.form.get("title")
    release_date = request.form.get("release_date")
    runtime = request.form.get("runtime")

    etl = EtlDTO(id, title, release_date, runtime)
    etlDao = EtlDAO()
    etlDao.etlinsert(etl)
    print("-----------------------------")
    
    print('{"id" : %s, "title" : "%s", "release_date" : %s, "runtime" : %s}' % (id, title, release_date, runtime))
    return '{"id" : %s, "title" : "%s", "release_date" : %s, "runtime": %s}' % (id, title, release_date, runtime) 

# 2. 영화 모두 보기 ----------------------------------------------------------------------------------------------------------
@app.route('/selectall')
def selectall():
    etlDao = EtlDAO()
    rs = etlDao.etlselectall() # rs는 튜플
    
    print("\n" + "-----1" +"*"*200 )
    print(rs)
    print("\n" + "-----2" +"*"*200)
    print(rs[0])
    print("\n" + "-----3" +"*"*200)
    print(rs[0][0])
    print("\n" + "*"*100 + "\n")
    # for i in range(len(rs)) :
    #     return 
    #     return '{"id" : %s, "title" : "%s", "release_date" : "%s", "runtime" : %s}' % (rs[i][0],rs[i][1],rs[i][2],rs[i][3])

    # for i in range(len(rs)):
    #     a = print('{"id" : %s, "title" : "%s", "release_date" : "%s", "runtime": %s}' % (rs[i][0], rs[i][1], rs[i][2], rs[i][3]))
    # return a

    df = pd.DataFrame(rs, columns=['id','title','release_date', 'runtime'])
    a = json.dumps(df.to_dict('records'))
    print(a +"\n")
    print(type(a))
    return a

# 3. 단일 영화 조회 ----------------------------------------------------------------------------------------------------------
@app.route('/select', methods=['get'])
def select():
    id = request.args.to_dict()['id']
    
    etlDao = EtlDAO()
    rs = etlDao.etlselect(id) # rs는 튜플
    print("----- etlcrud.py의 select()------------------------------------------------------------------------------------------------------------------")
    print( '{"id" : %s, "title" : "%s", "release_date" : "%s", "runtime" : %s}' % (rs[0],rs[1],rs[2],rs[3]))
    return '{"id" : %s, "title" : "%s", "release_date" : "%s", "runtime" : %s}' % (rs[0],rs[1],rs[2],rs[3])

# 4. 영화 업데이트 ----------------------------------------------------------------------------------------------------------
@app.route('/update', methods=['get'])
def update():
    id = request.args.to_dict()['id']
    title = request.args.to_dict()['title']

    etlDao = EtlDAO()
    etlDao.etlupdate(id, title)
    rs = etlDao.etlselect(id)
    print("----- etlcrud.py의 update()------------------------------------------------------------------------------------------------------------------")
    
    print( '{"id" : %s, "title" : "%s", "release_date" : "%s", "runtime" : %s}' % (rs[0],rs[1],rs[2],rs[3]))
    return '{"id" : %s, "title" : "%s", "release_date" : "%s", "runtime" : %s}' % (rs[0],rs[1],rs[2],rs[3])

# 5. 영화 삭제 ----------------------------------------------------------------------------------------------------------
@app.route('/delete', methods=['post'])
def deletl():
    id = request.form.get("id")
    
    etlDao = EtlDAO()
    r = etlDao.etldelete(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
