import json

with open('corpus/trucs_arno.json', 'r') as file:
    messages = json.load(file)['messages']

# Filtering based on Arno's id
anroMessages = [message['content'] for message in messages if message['author']['id'] == '153947383804329984']
# print(anroMessages)
text = '\n'.join(anroMessages) + '\n'

with open('corpus/corpus.txt', 'wb') as file:
    file.write(text.encode('utf-8'))

print('done')