import json

f = open('retrieval.json','r')
retrieval = json.load(f)
f.close()

# all relevant documents are retrieved 

eval = []

print(" Give input as 1 - Relevant and 0 - Non-Relevant")

total_relevant = 0
for order in retrieval:
    i = int(input("d"+str(order)+" - "))
    if i == 1:
        total_relevant+=1
        eval.append(1)
    else:
        eval.append(0)    

relevant = 0
retrieved = 0
for i in eval:
    retrieved+=1
    if i == 1:
        opinion = "R"
        relevant+=1
    else:
        opinion = "NR"    
    print(opinion,"Precision :",(relevant/retrieved),"Recall :",(relevant/total_relevant)) 


print("Relevant documents retrieved",relevant)
print("Total no of documents retrieved",retrieved)
print("Total no of relevant documents",total_relevant)
        