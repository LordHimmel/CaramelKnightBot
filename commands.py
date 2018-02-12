import random


def roll(args):
    D=0
    message=''
    result=0
    if (len(args)==1)and(args[0].count("д")==1):
        try:
            dice=args[0]
            for i in range (0,int(dice[:dice.find("д")])):
                D=random.randint(1,int(dice[dice.find('д')+1:]))
                message=message+'['+str(D)+'] '
                result+=D
        except:
                return "Прости, но я тебя не поняла. \nНапиши что-то вроде 1д6 ли 100д500"
    if result==0:
        return "Прости, но я тебя не поняла. \nНапиши что-то вроде 1д6 ли 100д500"
    else:
        return message+"\nитоговый результат = "+str(result)


comms = {"кинь":roll}



def calculate(msg):
    msg=msg.replace('/','')
    args=msg.split()
    
    try:
        return comms[args[0]](args[1:])
    except:
        return "Что-то пошло не так т..т"
