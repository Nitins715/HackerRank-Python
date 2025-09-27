from html.parser import HTMLParser

N = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for element in attrs:
                attribute_name = element[0]
                attribute_value = element[1]
                print(f"-> {attribute_name} > {attribute_value}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for element in attrs:
                attribute_name = element[0]
                attribute_value = element[1]
                print(f"-> {attribute_name} > {attribute_value}")


parser = MyHTMLParser()

for _ in range(N):
    current_line = input()
    if parser.feed(current_line):
        print(parser.feed(current_line))
        
        