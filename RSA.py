 stri=int("".join(s))
    print(stri)
    m=stri


###########################################################################################################################









#  x= P=[] + "," +Q=[]+","+phy_n+","+n+","+E+","+D

    message=[]
    Cipher=[]

    #Cipher=[]

    mess=m
    me=m
    ct=0
@@ -230,48 +213,22 @@ def checkprime_q(q):
    P=[971,157,127,211,421]
    Q=[4783,3709,7547,6869,3001]
    r=randint(0,4)











    n=P[r]*Q[r]
    num=n
    phy_n=(P[r]-1)*(Q[r]-1)

    def GCD(m,n):
            if(m==0):
                return n
            return GCD(n%m,m)



            return GCD(n%m,m)          


    for e in range(2,phy_n):
            if(GCD(e,phy_n)==1):         
                E = e
                break














    def calc_d(E,phy_n):


@@ -283,19 +240,13 @@ def calc_d(E,phy_n):
        if(bhy==1):
            return a%phy_n




        # for d in range(2,phy_n):
        #     res=(E*d)%phy_n
        #     if(res==1):
        #         D=d
        #         break
        # return D
    D = calc_d(E,phy_n)


    return n,E,D


#Main#
message="HEY"
n,E,D=calc()
pla,mes=preprocess_message(message,n)
@@ -321,14 +272,6 @@ def to_plain(D,n,Cipher,mes):
    plain=[]
    l=0 

    # for i in Cipher:
    #     temp=Cipher[l]**D
    #     m=temp%n
    #     plain.append(m)
    #     l+=1
    # return plain


    print("from RSA:",Cipher)

    for k in range(len(Cipher)):  
@@ -403,9 +346,6 @@ def to_plain(D,n,Cipher,mes):









@@ -416,15 +356,7 @@ def to_plain(D,n,Cipher,mes):






# P=[]
# Q=[]  

# P,Q,phy_n,n,E,D=calc() 
mess="how old are you soly iam tell you that you are so good student and each one have a good day and it's so good yaaaaaaaaa issssaaaaaaaaa"
#RSA(mess,n,E,D)

