import json
import os
import hashlib


blockchain_dir=os.curdir+'/blockchain/'

def get_hash(filename):#получает хэш блока с помощью метода sha1
    file=open(blockchain_dir+filename,'rb').read()
    return hashlib.sha1(file).hexdigest()

def get_files():#получает список файлов текущей директории и упорядочивает его
    files=os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])
    

def check_integrity():#проверяет целостность цепочки блоков
    #1.Считает хэш предыдущего блока
    #2.Ещё раз вычисляет хэш предыдущего блока
    #3.Сравнивает
    files = get_files()

    results=[]
    
    for file in files[1:]: 
        h = json.load(open(blockchain_dir+str(file)))['hash']#извлекаем хэш предыдущего блока

        prev_file=str(file-1)

        actual_hash = get_hash(prev_file)

        if h==actual_hash:
            res='ok'
        else:
            res='not ok'
            
        results.append({'block': prev_file,'result':res})
    return results
        
    
def write_block(name,amount,to_whom,prev_hash=''):#функция добавления блока,
    #параметрами которой являются данные о транзакции и хеш предыдущего блока

    files = get_files()
    prev_file=files[-1]

    filename= str(prev_file+1)
    
    prev_hash =get_hash(str(prev_file))

    data = {'name':name,
            'amount':amount,
            'to_whom':to_whom,
            'hash':prev_hash}
    
    with open(blockchain_dir + filename ,'w') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
   

def main():
     write_block(name='olya',amount=8,to_whom='ksu')#добавляет блок
   #print(check_integrity())


if __name__ == '__main__':#для запуска из консоли
    main()
