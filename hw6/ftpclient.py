from ftplib import FTP

ftp = FTP()
HOST = 'localhost'
PORT = 21
ftp.connect(HOST, PORT)

print(ftp.login(user="vladimir", passwd="2002"))

tmp = []

def getAns(data):

    def fun(a):
        global tmp
        tmp.append(a)

    return fun

def getAll(ftp, cur_dir=""):

    ls = ""

    global tmp
    tmp = []
    data = ftp.retrlines('LIST', callback=getAns(ls)).split("\n")

    dirs = []
    files = []

    for line in tmp:
        if line[0] == 'd':
            dirs.append(line.split()[8])
        else:
            files.append(line.split()[8])

    # print(dirs, files)

    for file in files:
        print('f: ' + cur_dir + "/" + file)

    for dir in dirs:
        try:
            new_cur_dir = cur_dir + "/" + dir
            print('d: ' + new_cur_dir)
            # ftp.cwd(dir)
            ftp.sendcmd('CWD ' + dir)
            getAll(ftp, new_cur_dir)

            # print('-: ' + new_cur_dir)
            ftp.sendcmd('CDUP')
            # print('+: ' + new_cur_dir)
        except Exception as inst:
            print(inst)

def ftp_upload(ftp_obj, path):
    with open(path, 'rb') as fobj:
        ftp.storbinary('STOR ' + path, fobj, 1024)

def ftp_download(ftp_obj, path):
    with open(path, 'wb') as f:
        ftp_obj.retrbinary('RETR ' + path, f.write)

while True:
    line = input(": ")
    command = line.split()

    # print(command)

    match command:
        case ["upload", file_path]:
            ftp_upload(ftp, file_path)

        case ["download", file_path]:
            ftp_download(ftp, file_path)

        case ["all"]:
            getAll(ftp)

        case ["close"]:
            ftp.close()
            break

        case ["quit"]:
            ftp.quit()
            break
        
        case _:
            print('Command not found: ' + line)