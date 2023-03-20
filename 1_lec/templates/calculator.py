
def calcBMI(height,weight):
   
    stdw=(height-100)*0.85
    obestiy = weight/stdw*100
    if obestiy <= 90:
       result = '저체중'
       picture = "/static/image/b.jpg"
    elif 90<obestiy<=110:
        result ='정상'
    elif 110<obestiy<=120:
        result ='과체중'
    else:
        result='비만'

    return result , picture