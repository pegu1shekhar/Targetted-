APP_ACCESS_TOKEN = ''#your token here
BASE_URL = 'https://api.instagram.com/v1/'

#----------=============######function decaration for get user id from instagram---=====#######

def get_user_id(username,BASE_URL,APP_ACCESS_TOKEN):
  import requests
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info= requests.get(request_url).json()                   #getting user id

  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          return user_info["data"][0]["id"]                     #returing to user info

      else:
          print 'User does not exist!'                          #commit messages
  else:
      print 'Status code other than 200 received!'

#---------==========#######function declaration for user info from instagram---=====######

def user_info(username):
    id= get_user_id(username,BASE_URL,APP_ACCESS_TOKEN)
    import requests
    request_url = (BASE_URL + 'users/%s/?access_token=%s') % (id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()              #getting user info here

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            temp = user_info['data']                          #taking temp asa a variable here
            print "User id:%s" % temp['id']                   #output user id
            print "Usename :%s" % temp['username']            #output user name
            print "Profile pic :"                             #output profile pic
            from urllib import urlretrieve
            name = temp['username'] + '.jpg'
            urlretrieve(temp['profile_picture'],name)

#-----=====#######Import os is to display the download images in images viewer in linux os--====#######

            import os
            os.system("display -delay 5 /root/PycharmProjects/untitled2/%s" % name)
            print "Full name :%s" % temp['full_name']         #output full name
            print "Followers :%d" % temp['counts']['follows'] #output follows
            print "Following :%d" % temp['counts']['followed_by'] #output folloed by
            print "Media :%d" % temp['counts']['media']           #output media
        else:
            print 'User does not exist!'                          #commit messages
    else:
        print 'Status code other than 200 received!'

