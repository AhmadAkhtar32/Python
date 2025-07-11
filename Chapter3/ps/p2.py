#replacing in python
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>","Ahmad").replace("<|Date|>","10July-2025"))