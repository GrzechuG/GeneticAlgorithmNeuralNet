import random
st1 = open("inputs.csv",'w+')
st1.write("");
st2 = open("outputs.csv",'w+')
st2.write("");
st1.close()
st2.close()
for i in range(0, 50):
    get=[]
    for j in range(0,5):
        r=random.getrandbits(1)
        #print(r)
        get.append(r);

    inp = open("inputs.csv",'a+')
    out = open("outputs.csv",'a+')
    inp.write((str(get).replace("[","").replace("]",""))+"\n")
    out.write((str(get[::-1]).replace("[","").replace("]",""))+"\n")
    #print("inputs.add(new double[]{"+str(get).replace("[","").replace("]","")+"});")

    #print("outputs.add(new double[]{"+str(get[::-1]).replace("[","").replace("]","")+"});")
