import pandas as pd
metadata = pd.read_json('train.json', lines=True)

dataset = metadata[['reviewText','summary', 'overall']]
dataset.sample(5)
dataset.dropna()
print(dataset.dtypes)
for i in range (len(dataset)):
    if(float(dataset['overall'][i])==5.0):
        f = open("E:\\CSC2515\\project\\basictext\\train2\\5\\"+str(i)+".txt", 'w')
        f.write( str(dataset['summary'][i])+ str(dataset['reviewText'][i]) )
        f.close()
    if(float(dataset['overall'][i])==4.0):
        f = open("E:\\CSC2515\\project\\basictext\\train2\\4\\"+str(i)+".txt", 'w')
        f.write( str(dataset['summary'][i])+ str(dataset['reviewText'][i]) )
        f.close()
    if(float(dataset['overall'][i])==3.0):
        f = open("E:\\CSC2515\\project\\basictext\\train2\\3\\"+str(i)+".txt", 'w')
        f.write( str(dataset['summary'][i])+ str(dataset['reviewText'][i]) )
        f.close()
    if(float(dataset['overall'][i])==2.0):
        f = open("E:\\CSC2515\\project\\basictext\\train2\\2\\"+str(i)+".txt", 'w')
        f.write( str(dataset['summary'][i])+ str(dataset['reviewText'][i]) )
        f.close()
    if(float(dataset['overall'][i])==1.0):
        f = open("E:\\CSC2515\\project\\basictext\\train2\\1\\"+str(i)+".txt", 'w')
        f.write( str(dataset['summary'][i])+ str(dataset['reviewText'][i]) )
        f.close()