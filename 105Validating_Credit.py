import re
pattern = r'([456]\d{15}|[456]\d{3}(-\d{4}){3})'
for _ in range(int(input())):
    card_no = input()
    if not re.fullmatch(pattern,card_no):
        print("Invalid")
        continue
        
    card_no = card_no.replace("-","")
    
    if re.search(r'(\d)\1{3,}',card_no):
        print("Invalid")
    else:
        print("Valid")
        