import sys

with open(r'C:\Users\user\Desktop\speechToText\finaltext.txt', 'rb') as file:  
    text = file.read()

# res = {}
# texts = []
final_lst = []
text = text.decode("utf-16")
text = text.split('\r\n')

file_text = [text[x].split(':') for x in range(1, len(text), 3)]
# one coherent speech
with open(sys.argv[1], 'w') as file:
    file.write('{0}: {1}'.format(file_text[-1][0].strip(), file_text[-1][1]))


# when there are pauses in the speech 

# for x, i in enumerate(file_text):
#     res[x] = i[1].strip()

# for k, v in res.items():
#     if eval(v) not in texts:
#         texts.append(eval(v))
#     #print('{0}: [{1}]'.format(k, v))
# print(texts)

# print('\n')

# for i in range(len(texts)-1):
#     if texts[i] in texts[i+1]:
#         final_lst.append(texts[i+1])

# print(final_lst)
