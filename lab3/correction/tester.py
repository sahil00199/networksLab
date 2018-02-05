from decode import decode
from encode import encode

def string(n):
	if n==0 :
		yield ""
	else:
		a = string(n-1)
		while True:
			b = next(a)
			yield b+ "1"
			yield b+ "0"

for n in range(21):
    s = string(n)
    for i in range(2**n):
            st= next(s)
            encoded=encode(st)
            for j in range(n):
                    for k in range(j+1,n):
                            wr= st[0:j]+str((int(st[j])+1)%2)+st[j+1:k]+str((int(st[k])+1)%2)+st[k+1:n] 
                    # if wr[j]=="0":
                    # 	wr[j]="1"
                    # else:
                    # 	wr[j]="0"
                    # for k in range(i+1,n):
                    # 	if wr[k]=="0":
                    # 		wr[k]="1"
                    # 	else:
                    # 		wr[k]="0"
                            rec= decode(wr+encoded)
                            if rec==st:
                                    continue
                            else:
                                    print(str(n) + st+" "+wr)
    print("completed brute force for i = " + str(n))




