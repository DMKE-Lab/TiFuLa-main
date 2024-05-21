import os
from pandas.io import json
from tqdm import tqdm

def txtToJson(path):
    filename = os.listdir(path)
    filejson=dict()
    for fn in tqdm(filename):
        p=os.path.join(path,fn)
        try:
            f=open(p,mode="r",encoding="utf-8")
            data=f.read().replace(" ","").replace("\n","")
            filejson[fn.rstrip(".txt")]=data
            f.close()
        except Exception:
            f = open(p, mode="r", encoding="gbk")
            data=f.read().replace(" ","").replace("\n","")
            filejson[fn]=data
            f.close()
    return filejson,len(filejson)

def saveInJsonFile(data,path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(filejson, ensure_ascii=False))

readpath=r""
filejson,length=txtToJson(readpath)
print(filejson)

save_path=r""
saveInJsonFile(filejson,save_path)
