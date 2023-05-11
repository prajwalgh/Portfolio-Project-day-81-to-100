todo_items=[]
with open("TodoItem.txt","r") as items:
    for i in items:
        todo_items.append(i)
while True:
    print("enter command 'show ,add : item , remove : number ,exit, '")
    input1=input()
    x=input1.split(':')
    if x[0]=='exit':
        break
        print("program stopped")
    if x[0]=="add ":
        todo_items.append(x[1])
    if x[0]=="remove ":
        todo_items.pop(int(x[1])-1)
    if x[0]=="show":
        for i in todo_items:
            print(i)

with open("TodoItem.txt","w") as items:
    for i in todo_items:
        items.write(i)
        items.write("\n")