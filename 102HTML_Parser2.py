from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print(">>> Multi-line Comment" if '\n' in data else ">>> Single-line Comment")
        print(data)
        
    def handle_data(self,data):
        if data.strip():
            print(f">>> Data\n{data}")

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()