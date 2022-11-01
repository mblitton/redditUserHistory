import requests
import json
import urllib
from urllib.request import urlopen

#define variables for user input


user = input('Hello, who are we searching for?')

print("""
Do you want to see their posts or their comments?
[1] - posts
[2] - comments
Selection:""")
#simple error check, consider putting into some type of while loop so it doesn't exit on incorrect selection.
while True:
    search = input()
    if search == '1':
        search = 'submission'
        break
    elif search == '2':
        search = 'comment'
        break
    else:
        print('Select either 1 or 2')
        continue
    

#request the url, input the user's selections into the url
url = 'https://api.pushshift.io/reddit/' + search + '/search' + '/?author=' + user + '&size=500'

#open the url
response = urlopen(url)
#convert url to json
data = json.loads(response.read())
#find amount of arrays within json
tot = len(data['data'])
#convert total to string for message
strtot = str(tot)

print('There are ' + strtot + ' '+ search + 's' + '\n')
if tot == 0:
    quit()

def getcomments():
    while True:
        count = int(input('How many comments would you like to view? (Enter whole number)' + '\n'))
        #check to make sure user isn't asking for more than available
        if count > tot:
            print('Amount must be less than or equal to total amount available')
            continue
        #break out and move on with function
        elif count <= tot:
            break
    
    #print the comment and link while iterating through the json array.
    count = count
    posts = data
    arr = 0
    amt = 1

    while arr < count:
        #print the comment, then print the link to the comment
        com = posts['data'][arr]
        comment = str(amt) + ': ' + com['body']
        link = 'Link to comment: ' + 'https://reddit.com' + com['permalink']

        print(comment + '\n' + link)

        arr = arr + 1
        amt = amt + 1

def getposts():
    while True:
        count = int(input('How many comments would you like to view? (Enter whole number)' + '\n'))
        if count > tot:
            print('Amount must be less than or equal to total amount available')
            continue
        elif count <= tot:
            break
    count = count
    posts = data
    arr = 0
    amt = 1
    while arr < count:
        sub = posts['data'][arr]
        submission = str(amt) + ': ' + sub['title']
        #print(str(amt) + ': ' + sub['title'])
        link = 'Link to post: ' + sub['full_link']
        #print('Link to post: ' + sub['full_link'])
        print(submission + '\n' + link)
        
        arr = arr + 1
        amt = amt + 1



if search == 'comment':
    getcomments()
    
elif search == 'submission':
    getposts()
