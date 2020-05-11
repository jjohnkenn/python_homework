homework = "You have to do strings for homework"
print(homework)
homework="this is a homework"
print(homework)
#multiline_string
# homework="""
#         you have to 
#         do strings 
#         for 
#         """
print(homework)

print(homework[-1])
print(homework[1])
print(homework[0])

for i in range(0,len(homework)):
    print(homework[i])
    
print(len(homework))
print(homework[17])
print(homework.upper())
print(homework.lower())
print(homework.capitalize())
homework = homework  +  "  today done"
print(homework)