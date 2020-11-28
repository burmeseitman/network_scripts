import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''HTTP GET'''


def http_get(target_host, target_port, page_name):
    request = ("GET /" + page_name + " HTTP/1.1\r\nHost: " + target_host + "\n\n").encode()
    client.connect((target_host, target_port))
    client.send(request)
    response = client.recv(4096)
    print(response.decode())


'''HTTP Login POST'''


def http_post(target_host, target_port, page_name, username, password):
    request = ("POST /" + page_name + " HTTP/1.1\r\n" +
               "Host: " + target_host + "\r\n" +
               "Accept: Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n" +
               "Content-Type: application/x-www-form-urlencoded\r\n" +
               "Accept-Language: en-US,en;q=0.5\r\n" +
               "Connection: keep-alive\r\n" +
               "Cookie: login=" + username + "/" + password + "\r\n" +
               "Upgrade-Insecure-Requests: 1\r\n" +
               "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n" +
               "uname=" + username + "&pass=" + password + "\n\n").encode()

    client.connect((target_host, target_port))
    client.send(request)
    response = client.recv(8192)
    print(response.decode())


print("HTTP Socket:")
print("1: GET")
print("2: POST")
print("3: Exit")
option = input("Select HTTP Option (GET/POST) : ")

if option == 1:
    http_get("testphp.vulnweb.com", 80, "login.php")
elif option == 2:
    http_post("testphp.vulnweb.com", 80, "userinfo.php", "test", "test")
elif option == 3:
    exit()


