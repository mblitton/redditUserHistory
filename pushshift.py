import requests
import json
import urllib
from urllib.request import urlopen

#define variables for user input


#create a function that searches for user, if no user, input new username or quit

def startSearch():
    while True:
        user = input('Hello, who are we searching for?')
        #basic user search if any result is > 0
        url = 'https://api.pushshift.io/reddit/search/?author=' + user + '&size=500'

        #open the url
        response = urlopen(url)
        #convert url to json
        data = json.loads(response.read())
        #find amount of arrays within json
        tot = len(data['data'])
        #convert total to string for message
        strtot = str(tot)
        if tot == 0:
            print('username not in database. Would you like to try a different username?\n')
            ans = input()
            if ans == 'y':
                startSearch()
            elif ans == 'n':
                quit()
            else:
                print('Enter y for yes, n for no\n')
                break
        else:
            startSearch.user = user
            break

def getcomments():
    while True:
        count = input('There are ' + strtot + ' '+ search + 's, how many comments would you like to view? (Enter whole number)' + '\n')
        try:
            count = int(count)
        except:
            print('Please enter a whole number\n')
            continue
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
        #print the comment, then print the link to the comment
        com = posts['data'][arr]
        comment = str(amt) + ': ' + com['body']
        link = 'Link to comment: ' + 'https://reddit.com' + com['permalink']

        print(comment + '\n' + link)

        arr = arr + 1
        amt = amt + 1

def getposts():
    while True:
        count = input('There are ' + strtot + ' '+ search + 's, how many posts would you like to view? (Enter whole number)' + '\n')
        try:
            count = int(count)
        except:
            print('Please enter a whole number\n')
            continue
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

startSearch()

print("""
  #      Do you want to see their posts or their comments?
  #      [1] - posts
  #      [2] - comments
  #      Selection:""")
while True:
    submit = input()
    if submit == '1':
        search = 'submission'
        break
    elif submit == '2':
        search = 'comment'
        break
    else:
        print('Select either 1 or 2')
        continue    
#request the url, input the user's selections into the url
url = 'https://api.pushshift.io/reddit/' + search + '/search' + '/?author=' + startSearch.user + '&size=500'

#open the url
response = urlopen(url)
#convert url to json
data = json.loads(response.read())
#find amount of arrays within json
tot = len(data['data'])
#convert total to string for message
strtot = str(tot)
while True:        
    if tot > 0:
        break
    elif tot == 0:
        print('There are no results. Would you like to try a different username?\n')
        ans = input()
        if ans == 'y':
            break
        elif ans == 'n':
            quit()
        else:
            print('Please enter y for yes, n for no\n')

if search == 'comment':
    getcomments()
    
elif search == 'submission':
    getposts()
