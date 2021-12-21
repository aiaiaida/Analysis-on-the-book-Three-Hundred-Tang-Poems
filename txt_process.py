from collections import Counter
with open("/Users/aada/Desktop/cl_project/唐詩三百首.txt") as f:
    data =f.readlines()
    stripped = []
    for line in data:
        line2 = line.replace("\n","")
        if "(" and ")" in line:
            a = line.find("(")
            b = line.find(")")
            line_strip = line.replace("\n","")
            line2 = line_strip.replace(line[a:b+1],"")
        stripped.append(line2)
    for i in stripped:
        if i == "":
            stripped.remove(i)
    print(stripped)
    a = 0
    poets = []
    content = ""
    for i in stripped:
        if "作者" in i:
            poets.append(i[3:])
        if "詩文" in i:
            content += i[3:]
            a+=1
    #print(poets)
    #print(Counter(poets))
    print(a)
    with open("content_cleaned.txt","w") as out:
        out.write(content) 
    
    



    

        

    
