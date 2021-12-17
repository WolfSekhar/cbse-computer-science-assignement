
emails = [
    "bestfreevideos@bigbestfreebeststbestmail.info",
    "webhost@bestwarez.ru",
    "coupons@homebestshop.su",
    "fiftypercentoff@bestwebhostingever.de",
    "buyonegetonefree@bestmail.dp.ua",
    "liyrhsaraalania@bestofmail.info",
    "watchlatestmovies@bestboyfilms.org",
    "couponshelp@best-finance.biz",
    "meesai@bestwestern.com.my",
    "nickolasvanilynickolasvanily@bestwayhealth.org",
    "yanonaissobelaissobbelaur@allthebest.com",
    "laptopcoupons@buybesty.su",
    "getfreehotelstay@lovebest.com.ua",
]
myDic = dict()
for email in emails:
    for i in range(4,7):
        iStart = 0
        iend = i
        while(iend <= len(email)):
            eWord = email[iStart:iend]
            iStart += 1
            iend += 1
            counter = 0
            if(not myDic.__contains__(eWord)):
                for mail in emails:
                    if(mail.__contains__(eWord)):
                        times = mail.count(eWord)
                        counter += times
                        myDic[eWord] = counter  

maxvalue = max(sorted(myDic.values()))  

for key,value in myDic.items():
    if(value == maxvalue):
        print(str(value) + " times and the key is : " + key)