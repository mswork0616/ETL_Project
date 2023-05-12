from etlDTO import EtlDTO
from dbutil import getConnect
import pyautogui as pg

class EtlDAO:
    # 1. 영화 등록 ----------------------------------------------------------------------------------------------------------
    def etlinsert(self, etlDTO):
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('insert into etl (id, title, release_date, runtime) values (%s, %s, %s, %s)', (etlDTO.getId(), etlDTO.getTitle(), etlDTO.getRelease_date(), etlDTO.getRuntime()))

            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()

    # 2. 영화 모두 보기 ----------------------------------------------------------------------------------------------------------
    def etlselectall(self):
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('select * from etl')

            result = cur.fetchall()
            
            if result != None:
                return result
            # for i in result:
            #     return i

            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()
    
    # 3. 단일 영화 조회 ----------------------------------------------------------------------------------------------------------
    def etlselect(self, id):
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('select * from etl where id=%s', id)

            result = cur.fetchone()
            
            if result != None:
                return result

            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()
    
    # 4. 영화 업데이트 ----------------------------------------------------------------------------------------------------------
    def etlupdate(self, id, title):
        try:
            conn = getConnect()
            cur = conn.cursor()
            
            sql = 'update etl set title=%s where id=%s'
            val = title, id
            cur.execute(sql, val)

            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()
    
    # 5. 영화 삭제 ----------------------------------------------------------------------------------------------------------
    def etldelete(self, id):
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute('delete from etl where id=%s', id)

            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()

# 단위 test
# if __name__ == '__main__':
    # EtlDAO().etlinsert(EtlDTO(1, 'a', 20220914, 100))
    # EtlDAO().etlselectall()
    # print(EtlDAO().etlselect(550))
    # EtlDAO().etlupdate(1, 50)
    # print(EtlDAO().etlselect(1))
    # EtlDAO().etldelete(1)
    # print(EtlDAO().etlselect(1))
