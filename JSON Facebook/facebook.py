import pandas as pd
from matplotlib import pyplot as plt
from pprint import pprint
import json

def f1():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    (l1,c1,s1)=(0,0,0)
    (l2,c2,s2)=(0,0,0)
    (l3,c3,s3)=(0,0,0)
    (l4,c4,s4)=(0,0,0)
    for i in dic['data']:
        if (i['like']!='' and i['comment']!='' and i['share']!=''):
            if i['Type']=='Photo':
                l1+=i['like']
                c1+=i['comment']
                s1+=i['share']
            elif i['Type']=='Video':
                l2+=i['like']
                c2+=i['comment']
                s2+=i['share']
            elif i['Type']=='Status':
                l3+=i['like']
                c3+=i['comment']
                s3+=i['share']
            else:
                l4+=i['like']
                c4+=i['comment']
                s4+=i['share']
    li1=[l1,c1,s1]
    li2=[l2,c2,s2]
    li3=[l3,c3,s3]
    li4=[l4,c4,s4]
    cols=['c','g','r']
    lis2=['LIKE','SHARE','COMMENT']
    plt.pie(li1,labels=lis2,colors=cols,startangle=90,shadow=True,explode=(0,0,0),autopct='%1.1f%%')
    plt.title("DISTRIBUTION OF LIKES, COMMENTS\n& SHARES FOR PHOTOS",fontsize=16,color="red")
    plt.legend(['LIKE','SHARE','COMMENT'])
    plt.text(0.5,-1.5,"MAJORITY OF AUDIENCE\nRESPONSE TO PHOTOS\nIS VIA LIKES.")
    plt.show()
    f.close()


def f2():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    (l1,c1,s1)=(0,0,0)
    (l2,c2,s2)=(0,0,0)
    (l3,c3,s3)=(0,0,0)
    (l4,c4,s4)=(0,0,0)
    for i in dic['data']:
        if (i['like']!='' and i['comment']!='' and i['share']!=''):
            if i['Type']=='Photo':
                l1+=i['like']
                c1+=i['comment']
                s1+=i['share']
            elif i['Type']=='Video':
                l2+=i['like']
                c2+=i['comment']
                s2+=i['share']
            elif i['Type']=='Status':
                l3+=i['like']
                c3+=i['comment']
                s3+=i['share']
            else:
                l4+=i['like']
                c4+=i['comment']
                s4+=i['share']
    li1=[l1,c1,s1]
    li2=[l2,c2,s2]
    li3=[l3,c3,s3]
    li4=[l4,c4,s4]
    cols=['y','b','violet']
    lis2=['LIKE','SHARE','COMMENT']
    plt.pie(li2,labels=lis2,colors=cols,startangle=90,shadow=True,explode=(0,0,0),autopct='%1.1f%%')
    plt.title("DISTRIBUTION OF LIKES, COMMENTS\n& SHARES FOR VIDEOS",fontsize=16,color="red")
    plt.legend(['LIKE','SHARE','COMMENT'])
    plt.text(0.5,-1.5,"MAJORITY OF AUDIENCE\nRESPONSE TO VIDEOS\nIS VIA LIKES.")
    plt.show()
    f.close()



def f3():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    (l1,c1,s1)=(0,0,0)
    (l2,c2,s2)=(0,0,0)
    (l3,c3,s3)=(0,0,0)
    (l4,c4,s4)=(0,0,0)
    for i in dic['data']:
        if (i['like']!='' and i['comment']!='' and i['share']!=''):
            if i['Type']=='Photo':
                l1+=i['like']
                c1+=i['comment']
                s1+=i['share']
            elif i['Type']=='Video':
                l2+=i['like']
                c2+=i['comment']
                s2+=i['share']
            elif i['Type']=='Status':
                l3+=i['like']
                c3+=i['comment']
                s3+=i['share']
            else:
                l4+=i['like']
                c4+=i['comment']
                s4+=i['share']
    li1=[l1,c1,s1]
    li2=[l2,c2,s2]
    li3=[l3,c3,s3]
    li4=[l4,c4,s4]
    cols=['g','c','r']
    lis2=['LIKE','SHARE','COMMENT']
    plt.pie(li3,labels=lis2,colors=cols,startangle=90,shadow=True,explode=(0,0,0),autopct='%1.1f%%')
    plt.title("DISTRIBUTION OF LIKES, COMMENTS\n& SHARES FOR STATUS",fontsize=16,color="red")
    plt.legend(['LIKE','SHARE','COMMENT'])
    plt.text(0.5,-1.5,"MAJORITY OF AUDIENCE\nRESPONSE TO STATUS\nIS VIA LIKES.")
    plt.show()
    f.close()



def f4():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    (l1,c1,s1)=(0,0,0)
    (l2,c2,s2)=(0,0,0)
    (l3,c3,s3)=(0,0,0)
    (l4,c4,s4)=(0,0,0)
    for i in dic['data']:
        if (i['like']!='' and i['comment']!='' and i['share']!=''):
            if i['Type']=='Photo':
                l1+=i['like']
                c1+=i['comment']
                s1+=i['share']
            elif i['Type']=='Video':
                l2+=i['like']
                c2+=i['comment']
                s2+=i['share']
            elif i['Type']=='Status':
                l3+=i['like']
                c3+=i['comment']
                s3+=i['share']
            else:
                l4+=i['like']
                c4+=i['comment']
                s4+=i['share']
    li1=[l1,c1,s1]
    li2=[l2,c2,s2]
    li3=[l3,c3,s3]
    li4=[l4,c4,s4]
    cols=['r','violet','c']
    lis2=['LIKE','SHARE','COMMENT']
    plt.pie(li4,labels=lis2,colors=cols,startangle=90,shadow=True,explode=(0,0,0),autopct='%1.1f%%')
    plt.title("DISTRIBUTION OF LIKES, COMMENTS\n& SHARES FOR LINKS",fontsize=16,color="red")
    plt.legend(['LIKE','SHARE','COMMENT'])
    plt.text(0.5,-1.5,"MAJORITY OF AUDIENCE\nRESPONSE TO LINKS\nIS VIA LIKES.")
    plt.show()
    f.close()



def f5():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    (l1,c1,s1)=(0,0,0)
    (l2,c2,s2)=(0,0,0)
    (l3,c3,s3)=(0,0,0)
    (l4,c4,s4)=(0,0,0)
    (ct1,ct2,ct3,ct4)=(0,0,0,0)
    for i in dic['data']:
        if (i['like']!='' and i['comment']!='' and i['share']!=''):
            if i['Type']=='Photo':
                l1+=i['like']
                c1+=i['comment']
                s1+=i['share']
                ct1+=1
            elif i['Type']=='Video':
                l2+=i['like']
                c2+=i['comment']
                s2+=i['share']
                ct2+=1
            elif i['Type']=='Status':
                l3+=i['like']
                c3+=i['comment']
                s3+=i['share']
                ct3+=1
            else:
                l4+=i['like']
                c4+=i['comment']
                s4+=i['share']
                ct4+=1
    li1=[l1,c1,s1]
    li2=[l2,c2,s2]
    li3=[l3,c3,s3]
    li4=[l4,c4,s4]
    li=[sum(li1)/ct1,sum(li2)/ct2,sum(li3)/ct3,sum(li4)/ct4]
    cols=['c','g','r','y']
    lis2=['PHOTOS','VIDEOS','STATUS','LINKS']
    plt.pie(li,labels=lis2,colors=cols,startangle=90,shadow=True,explode=(0,0,0,0),autopct='%1.1f%%')
    plt.title("VARIED RESPONSE OF AUDIENCE TO\nPHOTOS, VIDEOS, STATUS & LINKS\nPER POST OF EACH",fontsize=12,color="red")
    plt.legend(['PHOTOS','VIDEOS','STATUS','LINKS'])
    plt.text(0.5,-1.5,"AUDIENCE IS REALLY\nRESPONSIVE TO VIDEOS\nTHAN ANY OTHER FROM\nOF MEDIA.")
    plt.show()
    f.close()


def f6():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    d={}
    for i in dic['data']:
        if type(i['like'])==int:
            try:
                d[i['Post Month']]+=i['like']
            except:
                d[i['Post Month']]=i['like']
    l2=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    plt.xlabel('MONTH')
    l1=list(d.values())
    l1.reverse()
    plt.ylabel('NUMBER OF LIKES')
    plt.annotate('MAXIMUM IN\nJULY', xy=('JUL', 14150), xytext=('SEP', 11000),
             arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.annotate('MINIMUM IN\nMARCH', xy=('MAR', 2900), xytext=('JAN', 8500),
             arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.grid(True)
    plt.bar(l2,l1,label="NUMBER OF LIKES VS MONTH DISTRIBUTION",color='m')
    plt.title("NUMBER OF LIKES\nOVER THE CALENDAR YEAR",fontsize=16,color="red")
    plt.show()
    f.close()



def f7():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    d={}
    d1={}
    for i in dic['data']:
        if type(i['like'])==int:
            try:
                d[i['Post Month']]+=i['like']
                d1[i['Post Month']]+=1
            except:
                d[i['Post Month']]=i['like']
                d1[i['Post Month']]=1
    l2=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    plt.xlabel('MONTH')
    l1=list(d.values())
    l1.reverse()
    l3=list(d1.values())
    l3.reverse()
    for i in range(12):
        l1[i]=l1[i]/l3[i]
    plt.ylabel('NUMBER OF LIKES PER POST')
    plt.annotate('MAXIMUM IN\nJULY', xy=('JUL', 272), xytext=('OCT', 225),
             arrowprops=dict(facecolor='m', shrink=0.05),)
    plt.annotate('MINIMUM IN\nMARCH', xy=('MAR', 80), xytext=('FEB', 200),
             arrowprops=dict(facecolor='m', shrink=0.05),)
    plt.grid(True)
    plt.bar(l2,l1,label="NUMBER OF LIKES PER POST VS MONTH DISTRIBUTION",color='k')
    plt.title("NUMBER OF LIKES PER POST\nOVER THE CALENDAR YEAR",fontsize=16,color="red")
    plt.show()
    f.close()


def f8():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    d={}
    d1={}
    for i in dic['data']:
        if type(i['like'])==int:
            try:
                d1[i['Post Month']]+=1
            except:
                d1[i['Post Month']]=1
    l2=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    plt.xlabel('MONTH')
    l1=list(d1.values())
    l1.reverse()
    plt.ylabel('NUMBER OF POSTS')
    plt.scatter(l2,l1,label="NUMBER OF POSTS",color='m',s=50)
    plt.plot(l2,l1,label="NUMBER OF POSTS",color='k')
    plt.annotate('MAXIMUM IN\nOCTOBER', xy=('OCT', 59), xytext=('JUL', 55),
             arrowprops=dict(facecolor='y', shrink=0.05),)
    plt.annotate('MINIMUM IN\nJANUARY', xy=('JAN', 25), xytext=('JAN', 35),
             arrowprops=dict(facecolor='y', shrink=0.05),)
    plt.title("NUMBER OF POSTS\nOVER THE CALENDAR YEAR",fontsize=16,color="red")
    plt.show()
    f.close()

    
def f9():
    f = open("facebook.json", "r")
    json_string = f.read()
    dic = json.loads(json_string)
    d={}
    d1={}
    for i in dic['data']:
        if type(i['Total Interactions'])==int:
            try:
                d1[i['Post Month']]+=i['Page total likes']
            except:
                d1[i['Post Month']]=i['Page total likes']
    for i in dic['data']:
        try:
            d[i['Post Month']]+=1
        except:
            d[i['Post Month']]=1
    l2=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    plt.xlabel('MONTH')
    l1=list(d1.values())
    l1.reverse()
    l3=list(d.values())
    l3.reverse()
    for i in range(12):
        l1[i]=l1[i]/l3[i]
    plt.ylabel('TOTAL LIKES OF THE WHOLE PAGE',fontsize=6)
    plt.scatter(l2,l1,label="AVERAGE LIKES OF THE WHOLE PAGE",color='y',s=50)
    plt.plot(l2,l1,label="NUMBER OF POSTS",color='k')
    plt.title("AVERAGE GROWTH OF THE LIKES\nOF THE WHOLE PAGE",fontsize=16,color="red")
    plt.show()
    f.close()
    
