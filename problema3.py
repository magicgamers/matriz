def EliminacaoGauss():
    x=float(input('primeiro numero:'))
    y=float(input('segundo numero:'))
    z=float(input('terceiro numero:'))
    i=float(input('quarto numero:'))
    s1=(x,y,z,i)
    x=float(input('primeiro numero:'))
    y=float(input('segundo numero:'))
    z=float(input('terceiro numero:'))
    i=float(input('quarto numero:'))
    s2=(x,y,z,i)
    x=float(input('primeiro numero:'))
    y=float(input('segundo numero:'))
    z=float(input('terceiro numero:'))
    i=float(input('quarto numero:'))
    s3=(x,y,z,i)
    if True:
        #etapa 1
        c1=s2[0]/s1[0]
        c3=s2[1]-c1*s1[1]
        c5=s2[2]-c1*s1[2]
        c7=s2[3]-c1*s1[3]
        c2=s3[0]/s1[0]
        c4=s3[1]-c2*s1[1]
        c6=s3[2]-c2*s1[2]
        c8=s3[3]-c2*s1[3]
        c1=s2[0]-c1*s1[0]
        c2=s3[0]-c2*s1[0]
        if True:
            #etapa 2
            s2=(c1,c3,c5,c7)
            s3=(c2,c4,c6,c8)
            o1=s3[1]/s2[1]
            o2=s3[2]-o1*s2[2]
            o3=s3[3]-o1*s2[3]
            o4=s3[1]-o1*s2[1]
            s3=(c1,o4,o2,o3)
            if o3==0:
                print( 'Sistema Possível Inderteminado (SPI)')
            elif o2==0:
                print( 'Sistema Impossível (SI)')
            elif o3!=0 and o2!=0:
                z=o3/o2
                y=(s2[3]-(s2[2]*z))/s2[1]
                x=(s1[3]-((s1[1]*y)+(s1[2]*z)))/s1[0]
                print('z =',z)
                print('x =',x)
                print('y =',y)
                print('Solução (x,y,z) =','(',x,',',y,',',z,')')
                print('[',x,'\n',y,'\n',z,']')
def EliminacaoGaussEscalonado():
    x=float(input('primeiro numero:'))
    y=float(input('segundo numero:'))
    z=float(input('terceiro numero:'))
    i=float(input('quarto numero:'))
    s1=(x,y,z,i)
    y=float(input('segundo numero:'))
    z=float(input('terceiro numero:'))
    i=float(input('quarto numero:'))
    s2=(y,z,i)
    z=float(input('terceiro numero:'))
    i=float(input('quarto numero:'))
    s3=(z,i)
    if s3[1]==0:
        print( 'Sistema Possível Inderteminado (SPI)')
    elif s3[0]==0:
        print( 'Sistema Impossível (SI)')
    elif s3[1]!=0 and s3[0]!=0:
        z=s3[1]/s3[0]
        y=(s2[2]-(s2[1]))/s2[0]
        x=(s1[3]-(s1[2]*z)-(s1[1]*y))/s1[0]
        print('z =',z)
        print('x =',x)
        print('y =',y)
        print('Solução (x,y,z) =','(',x,',',y,',',z,')')
        print('[',x,'\n',y,'\n',z,']')
while True:
    q=int(input('Sistema estar escalonado?\n 1 - Sim \n 2 - Não \n'))
    if q==2:
        EliminacaoGauss()
        break
    elif q==1 :
        EliminacaoGaussEscalonado()
        break
    print('Erro, tente novamente!')
        
    
        
