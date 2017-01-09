
gtotal=0
total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
import pandas as pd
df = pd.read_csv("DB.txt.tmp")
df2=pd.read_csv("neg.txt")

sentences = input("Enter a sentence ")
sentence= sentences.split(".")
for i in range (0,len(sentence),1):
    tokens =sentence[i].split()
    for j in range(0,len(tokens),1):
        tokens[j]=(tokens[j].lower())
    for j in range(0,len(tokens),1):
        value = tokens[j]
        df1=df[df['word'] == value]
        if df1.empty:
            pass
        else:
            new= df1.iloc[0]['score']
            total[i]=total[i] +new
    for k in range(0,len(tokens),1):
        value = tokens[k]
        df3=df2[df2['nword'] == value]
        if df3.empty:
            pass
        else:
            if (total[i]==0):
                total[i]= total[i]-1
            else:
                total[i]=(-1)*total[i]

for i in range(0,len(sentence),1):
    gtotal=gtotal+total[i]
print(gtotal)
if(gtotal>0):
    print("Positive Statement")
elif (gtotal==0):
    print("Neutral Statement")
else:
    print("Negative Statemnt")