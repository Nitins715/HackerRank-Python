from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self,tag,attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")
        
    def handle_startendtag(self,tag,attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_comment(self,data):
        pass
        
html = '\n'.join(input() for _ in range(int(input())))
MyHTMLParser().feed(html)