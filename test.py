# Python Auto Dis Parser 1.0.1
# Author : HAMAYUN-TECH | HAMAYUN KHAN
# https://linktr.ee/khan
# https://fb.me/hamayun khan
# ------------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[0;32m Paste Token : ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        e = raw_input('\x1b[1;91m[?] \x1b[1;92mWant to pick up token?\x1b[1;97m[y/n]: ')
        if e == '':
            keluar()
        elif e == 'y':
            login()
        else:
            keluar()


def get(data):
    print '[*] Generate access token '
    try:
        os.mkdir('cookie')
    except OSError:
        pass

    b = open('cookie/token.log', 'w')
    try:
        r = requests.get('https://api.facebook.com/restserver.php', params=data)
        a = json.loads(r.text)
        b.write(a['access_token'])
        b.close()
        print '[*] successfully generate access token'
        print '[*] Your access token is stored in cookie/token.log'
        menu()
    except KeyError:
        print '[!] Failed to generate access token'
        print '[!] Check your connection / email or password'
        os.remove('cookie/token.log')
        menu()
    except requests.exceptions.ConnectionError:
        print '[!] Failed to generate access token'
        print '[!] Connection error !!!'
        os.remove('cookie/token.log')
        menu()


def phone():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')


logo = '\n\x1b[1;95m\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\x1b[1;95m\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\n\x1b[1;95m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x95\xae\n\x1b[1;95m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\xa3\xe2\x94\xab\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x95\xad\xe2\x95\xaf\n\x1b[1;95m\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\n\x1b[1;95m\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x94\xa3\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x95\xaf\n\x1b[1;95m\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb0\xe2\x95\xaf\n\n\x1b[1;94m-----------------------------------------------\n\n\x1b[1;92mCoder   :\x1b[1;96mhamayun khan\n\x1b[1;92mGithub  :\x1b[1;96mhttps://github.com/hamayun143\n\x1b[1;92mFacebook:\x1b[1;96mhamayun khan\n\x1b[1;92mWhatsapp :\x1b[1;96m03319258250\n\x1b[1;92mNote :\x1b[1;96mThis Is only For Educational Purpose\n\x1b[1;92mNew Update :\x1b[1;96m100% Work If You Login With Acces Token\n\n\x1b[1;94m-----------------------------------------------'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print '\n\x1b[1;95m\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\x1b[1;95m\xe2\x94\x83\xe2\x95\xad\xe2\x94\x81\xe2\x95\xae\xe2\x94\x83\n\x1b[1;95m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x95\xae\n\x1b[1;95m\xe2\x94\x83\xe2\x94\x83\xe2\x95\xb1\xe2\x94\x83\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\xa3\xe2\x94\xab\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x95\xad\xe2\x95\xaf\n\x1b[1;95m\xe2\x94\x83\xe2\x95\xb0\xe2\x94\x81\xe2\x95\xaf\xe2\x94\x83\xe2\x95\xad\xe2\x95\xae\xe2\x94\x83\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\xe2\x94\x83\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\n\x1b[1;95m\xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x94\xa3\xe2\x95\xaf\xe2\x95\xb0\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x95\xaf\n\x1b[1;95m\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb0\xe2\x95\xaf\n\n\x1b[1;94m-----------------------------------------------\n\n\x1b[1;92mCoder   :\x1b[1;96mHamayun Tech\n\x1b[1;92mGithub  :\x1b[1;96mhttps://github.com/hamayun143\n\x1b[1;92mFacebook:\x1b[1;96mHamayun khan\n\x1b[1;92mYoutube :\x1b[1;96mEmpty\n\x1b[1;92mNote :\x1b[1;96mThis Is only For Educational Purpose\n\x1b[1;92mNew Update :\x1b[1;96m Identity Problem Fixed 100% If You Login With Acces Token\n\n\x1b[1;94m-----------------------------------------------'
CorrectUsername = 'Dec'
CorrectPassword = 'code'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[0;31m\xf0\x9f\x94\x90 Tool Username : ')
    if username == CorrectUsername:
        password = raw_input('\x1b[0;31m\xf0\x9f\x94\x90Tool Password : ')
        if password == CorrectPassword:
            print 'Logged in successfully as ' + username
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[0;31mWrong Password'
            os.system('xdg-open https://www.facebook.com/ham143mah')
    else:
        print '\x1b[0;31mWrong Username'
        os.system('xdg-open https://www.facebook.com/ham143mah')

def lisensi():
    os.system('clear')
    login()


def login(session, email, password):
    
    '''
    Attempt to login to Facebook. Returns user ID, xs token and
    fb_dtsg token. All 3 are required to make requests to
    Facebook endpoints as a logged in user. Returns False if
    login failed.
    '''

    # Navigate to Facebook's homepage to load Facebook's cookies.
    response = session.get('https://m.facebook.com')
    
    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)
    
    # If c_user cookie is present, login was successful
    if 'c_user' in response.cookies:

        # Make a request to homepage to get fb_dtsg token
        homepage_resp = session.get('https://m.facebook.com/home.php')
        
        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()

        return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
    else:
        return False 

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Login to Facebook')
    parser.add_argument('email', help='Email address')
    parser.add_argument('password', help='Login password')

    args = parser.parse_args()

    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
    })

    fb_dtsg, user_id, xs = login(session, args.email, args.password)
    
    if user_id:
        print '{0}:{1}:{2}'.format(fb_dtsg, user_id, xs)
    else:
        print 'Login Failed'
