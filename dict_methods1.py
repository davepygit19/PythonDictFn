d={'product':'car','maker':'Suzuki','Name':'Celerio','model':2018,'transmission':'AMT','fuel':'petrol',
   'variant':'vxi(opt)','color':'pearl white'}
print(d)
print(type(d))
#using Slice Operator
print(d['Name'])
# print(d['Insurance']) #if no key value present its show error message
#using get methods
print(d.get('product'))
print(d.get('Insurance'))# if no key present its shows none not error message.
# print keys value the keys() method
print(d.keys())
for i in d.keys(): #iterate key using for loop
    print(i)
 # print values in dictionary the values() method
print(d.values())
for i in d.values():#iterate value using for loop
    print(i)