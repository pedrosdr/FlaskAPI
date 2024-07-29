from app import db

class VideoModel:
    def select_all(self):
        cursor = db.cursor()
        query = 'select id, name, views, likes from videos'
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        db.commit()
        res_dict = dict()
        for x in res:
            res_dict[x[0]] = {
                "name": x[1],
                "views": x[2],
                "likes": x[3],
            }
        return res_dict
    
    def select(self, id):
        cursor = db.cursor()
        query = 'select id, name, views, likes from videos where id = %s'
        cursor.execute(query, [id])
        res = cursor.fetchall()
        cursor.close()
        db.commit()
        return {
            id: {
                "name": res[0][1],
                "views": res[0][2],
                "likes": res[0][3]
            }
        }
    
    def insert(self, name, views, likes):
        cursor = db.cursor()
        query = 'insert into videos (name, views, likes) values (%s, %s, %s)'
        cursor.execute(query, (name, views, likes))
        cursor.close()
        db.commit()

    def update(self, id, name, views, likes):
        cursor = db.cursor()
        query = 'update videos set name=%s, views=%s, likes=%s where id=%s'
        cursor.execute(query, (name, views, likes, id))
        cursor.close()
        db.commit()
    
    def delete(self, id):
        cursor = db.cursor()
        query = 'delete from videos where id = %s'
        cursor.execute(query, [id])
        cursor.close()
        db.commit()