from flask import Flask,request, jsonify
import requests
from bs4 import BeautifulSoup
app= Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    text=0
    total=0
    if request.method == 'POST':
        # text = str(request.args["product_name"])
        text= request.form.get('product_name')
        if text is None:
            return "product name not found …"
        

#         url="https://www.cosdna.com/eng/product.php"
#         x=text.split()
#         after_join='+'.join(x)
#         print(after_join)


# # https://www.cosdna.com/eng/product.php?q=dove+shampoo+care&sort=featured
#         url2=url+"?q="+format(after_join)+"&sort=featured"
#         print(url2)
#         r=requests.get('https://www.cosdna.com/eng/product.php?q=dove&sort=featured')
#         htmlContent=r.content
#         soup=BeautifulSoup(htmlContent,'html.parser')
#         print(soup)
#         anchors=soup.find_all('a')
        # print(anchors)
        total=30
        return jsonify({"product":text,"prediction": total})

if __name__ == '__main__':
    app.run(debug=True)
 

