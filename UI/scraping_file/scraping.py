import requests
import time
from bs4 import BeautifulSoup
import csv

class Get_data:
  # URLと属性は必須、クラスは必要に応じて選択可能
  def __init__(self,URL):
    self.url = URL
  
  def get_element_class(self,element: str,target_class: str) -> list:
    #属性とクラスが指定されてない場合
    if( (element == "" and target_class == "") ):
      soup = BeautifulSoup(url.text,"html.parser")
      result = soup.find_all(self.element)
      return result

    elif(element != "" or (element != "" and target_class == "") ):
      self.element = element
      url = requests.get(self.url,timeout=4)
      soup = BeautifulSoup(url.text,"html.parser")
      result = soup.find_all(self.element)
      result = delete_Newline(result)

    else:
      self.element = element
      self.target_class = target_class
      url = requests.get(self.url,timeout=4)
      soup = BeautifulSoup(url.text,"html.parser")
      result = soup.find_all(self.element,class_=self.target_class)
      result = delete_Newline(result)

    url.close()
    return result


def delete_Newline(result: list, ) -> list:
  #     改行コードの削除
  index= 0
  for i in result:
    result[index] =  i.get_text()
    index+=1            

  for i in range(index):
    result[i] = result[i].rstrip('\n')
  return result


def write_csv(name):#引数のデータ型に注意
    with open('database.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for value in name:
          writer.writerow(value)
          
        csvfile.close()

if __name__ == '__main__':
  URL = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=030&bs=040&ta=13&sc=13114&sc=13201&cb=0.0&ct=3.0&mb=0&mt=9999999&et=9999999&cn=9999999&co=3&co=4&kz=1&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&po2=99&pc=100'
  sc = Get_data(URL)

  #項目の数だけ変数を書く
  a = sc.get_element_class("a","")
  print(a)
  tatemono = sc.get_element_class("a","js-cassetLinkHref")
  price = sc.get_element_class("div","detailbox-property-point")
  data = [[tatemono[i],price[i]] for i in range(len(tatemono))]
  #write_csv(data)
  print("file is closed")