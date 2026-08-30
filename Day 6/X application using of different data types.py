Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'''These are illustrative implementations, not X's proprietary source code.

1. String'''
"These are illustrative implementations, not X's proprietary source code.\n\n1. String"
#Used for usernames, tweet text, hashtags, profile names, etc.
username = "Kanth"
tweet_text = "Learning python today"
hashtag = "#python"
print(username)
Kanth

= RESTART: C:/Users/rohit/OneDrive/Desktop/python_course_work/Day  (6)/X application using of different data types.py
rahul123
Learning Python today!
#Integer
followers = 1250
following = 430
likes = 87
post_id = 10025
print("Followers:", followers)
Followers: 1250
print("Likes:", likes)
Likes: 87
#Strings-Used for usernames, tweet text, hashtags, profile names, etc.
#Integer-Used for things such as follower counts, following counts, likes, reposts, and post IDs

#Float:
#Used when a value can contain decimals, such as an engagement rate or location coordinates.
lattitude = 17.3850
longitude = 78.4867
print("Location:", lattitude,longitude)
Location: 17.385 78.4867

#Boolean:
#Used for yes/no states, such as whether an account is verified, whether a post is liked, or whether an account is following another account.
is_verified = True
is_liked = False
is_following = True
print("Verified:",is_verified)
Verified: True
print("Liked:",is_liked)
Liked: False

#Set:
#A set is useful when you need unique values, for example unique hashtags or users followed by an account.
hashtags = {"SSMB","indvsaus","testcricket","cr7"}
print(hashtags)
{'testcricket', 'cr7', 'SSMB', 'indvsaus'}
>>> 
>>> #Dictionary
>>> #A dictionary is very useful for representing a user's profile or a post because it stores key-value pairs.
>>> user = {
...     "username": "rahul123",
...     "name": "Rahul",
...     "followers": 1250,
...     "verified": True
... }
... 
... print(user["username"])
... print(user["followers"])
SyntaxError: multiple statements found while compiling a single statement
>>> user = {
...     "username":"rahul1123"
...     "name":"Rahul",
...     
SyntaxError: '{' was never closed
>>> user = {
...     "username":"rahul1123",
...     "name":"Rahul","follower":1250,"verified":True}
...     
>>> print(user["username"])
...     
rahul1123
>>> print(user["followers"])
...     
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(user["followers"])
KeyError: 'followers'
>>> #List
...     
>>> A list can represent a timeline containing multiple posts, a list of followers, or notifications.
...     
SyntaxError: invalid syntax
