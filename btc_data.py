import requests
res = requests.get("http://bitcoincharts.com/charts/chart.json?m=mtgoxUSD&SubmitButton=Draw&r=&i=&c=0&s=&e=&Prev=&Next=&t=M&b=B&a1=WMA&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&")
data = res.json()

