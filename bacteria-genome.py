input = open("bacteria.fasta").read()
output = open("bacteria.html","w")

count = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i+j] = 0

input = input.replace("\n","")

for k in range(len(input)-1):
    count[input[k]+input[k+1]] += 1

i = 1
for k in count:
	transparency = count[k]/max(count.values())
	output.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 75, 0, "+str(transparency)+"')>"+k+"</div>")

	if i%4 == 0:
		output.write("<div style='clear:both'></div>")
	i+=1

output.close()