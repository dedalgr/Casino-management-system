import models
import models2
# remove relationship
db = models.DBCtrl()
db2 = models2.DBCtrl()

a = db.get_all(models.CartPrise, order='id')
for i in a:
    obj = db2.make_obj(models2.CartPrise)
    for b in dir(i):
        if b[:1] != '_' and b != 'metadata' and b != 'registry':
            print(b)
            exec('obj.%s = i.%s' % (b, b))
    # print (obj.name)
    db2.add_object_to_session(obj)
db2.commit()