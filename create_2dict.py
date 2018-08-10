def create_2_dict():
    dict={}
    for i in range(10):
        dict.setdefault(i,{})
        dict[i][i*i]=i
    for key,values in dict.items():
        print(key)
        print(values)
        for k,v in values.items():
            print(k)
            print(v)

if __name__=="__main__":
    create_2_dict()
