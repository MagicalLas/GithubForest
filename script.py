import datetime
import os
import string

def startDate():
    print('input you wanted start date (YYYY/MM/DD)')
    y = input('Year : ')
    m = input('Month : ')
    d = input('Date : ')
    while(dateCheck(y,m,d)):
        print("error. try again.")
        y = input('Year : ')
        m = input('Month : ')
        d = input('Date : ')
    return (int(y),int(m),int(d))

def endDate():
    print('input you wanted end date (YYYY/MM/DD)')
    y = input('Year : ')
    m = input('Month : ')
    d = input('Date : ')
    while(dateCheck(y,m,d)):
        print("error. try again.")
        y = input('Year : ')
        m = input('Month : ')
        d = input('Date : ')
    return (int(y),int(m),int(d))

def dateCheck(year, month, date):
    y = int(year)
    m = int(month)
    d = int(date)

    if(not(y>=2017 and y<=2018)):
        return True
    if(not(m>0 and m<=12)):
        return True
    if(not(d>0 and d<=31)):
        return True

    if(len(year)!=4):
        return True
    if(len(month)!=2):
        return True
    if(len(date)!=2):
        return True
    return False
def replaceDate(y,m,d):
    d+=1
    
    if(d==29 and m == 2):
        m+=1
        d=1
    if(d>30):
        d=1
        m+=1
    if(m==13):
        y+=1
        m=1
    return (y,m,d)
def compare3(a,b,c,d,e,f):
    if(a!=b):
        return False
    if(c!=d):
        return False
    if(e!=f):
        return False
    return True
today = datetime.date.today()
year = today.year
month = today.month
day = today.day

(y,m,d) = startDate()
(ey,em,ed) = endDate()

while(not compare3(y,ey,m,em,d,ed)):
    git_add = 'git add daily_commit.md'
    git_commit = '''git commit -m "Daily commit used Wonho's version" '''
    file_message = ('''{0}/{1}/{2} : Daily commit sucsessfuly  \r\n'''.format(y,m,d))
    os.system("date {0}/{1}/{2}".format(y,m,d))
    logFile = open("daily_commit.md",'a')
    logFile.writelines(file_message)
    logFile.close()
    os.system(git_add)
    os.system(git_commit)
    (y,m,d) = replaceDate(y,m,d)

os.system("date {0}/{1}/{2}".format(year,month,day))