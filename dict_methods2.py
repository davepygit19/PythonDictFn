dic_va={'product':'car','maker':'Suzuki','Name':'Celerio','model':2018,'transmission':'AMT','fuel':'petrol',
   'variant':'vxi(opt)','color':'pearl white'}
#items()---> method
for i in dic_va.items():#items is a method print each key and values
    print(i)
    print(type(i))
for i in dic_va.items():
    for j in i:
        print(j)
#copy()--->method
dic_va2= dic_va.copy()
print(dic_va2)
#clear----->method
dic_va2.clear()
print(dic_va2)
#pop() --------> method
dic_va.pop('model')
print(dic_va)
#popitems()-----------> method
dic_va.popitem()# its remove the last key and value
print(dic_va)
#Add key and values
dic_va['model']=2018# only one key and must update
print(dic_va)
dic_va.update({'color': 'pearl white'})
print(dic_va)
#change the value
dic_va['maker']='maruthi suzuki'
print(dic_va)