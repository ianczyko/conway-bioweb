# -*- mode: Python; -*-
import os, platform, subprocess, re, time, ConfigParser, shutil, sys, signal, fileinput

MYAPP_VER_MAJOR = '0'
MYAPP_VER_MINOR = '09'
MYAPP_VER_COMPILATION = '0'
MYAPP_VER_INSTALL = '1'

#odczytuje wersje kompilacji z wersji repozytorium
ver_repository = subprocess.Popen('hg sum', shell=True, stdout=subprocess.PIPE).communicate()[0]
try:
    MYAPP_VER_COMPILATION = re.search('(?<=parent: )\d+', ver_repository).group()
except BaseException:
    pass

MYAPP_VER_STRING = str(MYAPP_VER_MAJOR) + '.' + str(MYAPP_VER_MINOR) + '.' + MYAPP_VER_COMPILATION

#web
WWW_BROWSER_WINDOWS='chrome'
WWW_BROWSER_LINUX='google-chrome'
WEB_SRV_PREFIX = 'srvmyapp'
WEB_SRV_HOST = '127.0.0.1'
WEB_SRV_PORT = '50007'
WEB_CLIENT_HOST = '127.0.0.1'
WEB_CLIENT_PORT = '9000'

#database
DB_NAME='mydb'
DB_USER='mydb'
DB_PASSWORD='mydb'

Export('MYAPP_VER_MAJOR MYAPP_VER_MINOR MYAPP_VER_COMPILATION MYAPP_VER_INSTALL')
Export('WWW_BROWSER_WINDOWS WWW_BROWSER_LINUX')
Export('WEB_SRV_PREFIX WEB_SRV_HOST WEB_SRV_PORT WEB_CLIENT_HOST WEB_CLIENT_PORT')
Export('DB_NAME DB_USER DB_PASSWORD')

vars = Variables('custom.py')
vars.Add(EnumVariable('r','Run the application, l: local lighttpd + gunicorn at \''+ WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT +'\''\
                      ', d: django internal at \''+ WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT +'\'',
                      'no', allowed_values = ('l', 'd', 'no'), map={}, ignorecase=2) )
vars.Add(EnumVariable('t','Run the unit tests, \'w\' Python web, \'j\' Javascript client, \'c\' C++ library, \'f\' functional ',
                      'no', allowed_values = ('w', 'j', 'c', 'f', 'no'), map={}, ignorecase=2) )
vars.Add(BoolVariable('cov','Set to 1 to run the coverage reports for python server',0) )
vars.Add(BoolVariable('syncdb','Set to 1 to clean application files and recreate tables in database',0) )
vars.Add(BoolVariable('zip','Set to 1 to build zip package',0) )
vars.Add(BoolVariable('doxygen', 'Set 1 to generate documentation. The file Doxyfile_in is required',0) )
additional_help_text = ""

env = Environment(variables=vars)

Help("""
type 'scons' to build the program and libraries. Settings specific for this project are listed below.
"""
     +
     vars.GenerateHelpText(env)
     +
     additional_help_text)

if (platform.system() == "Linux"):
    WWW_BROWSER = WWW_BROWSER_LINUX
    BROWSER_CMD = WWW_BROWSER_LINUX + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT + ' &'
else:
    WWW_BROWSER = WWW_BROWSER_WINDOWS
    BROWSER_CMD = 'start "" ' + WWW_BROWSER_WINDOWS + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT

def addToLD(path):
    if "LD_LIBRARY_PATH" in os.environ:
        os.environ["LD_LIBRARY_PATH"]= os.environ["LD_LIBRARY_PATH"] + ':' + os.path.abspath(path)
    else:
        os.environ["LD_LIBRARY_PATH"]= os.path.abspath(path)

if env['r'] == 'l':
    os.system(BROWSER_CMD)
    os.system('lighttpd -f client/lighttpd.develop')

    if platform.system() == "Linux":
        os.system('gunicorn --chdir build_web --timeout 0 --workers 1 --bind \'{addr}:{port}\' wsgi:application'.format(addr=WEB_SRV_HOST, port=WEB_SRV_PORT))
    elif platform.system() == "Windows":
        os.system('python3 build_web/manage.py runfcgi daemonize=false method=threaded host=' + WEB_SRV_HOST + ' port=' + WEB_SRV_PORT)

    if (platform.system() == "Linux"):
        os.system('kill `cat client/lighttpd.pid`')
    else:
        os.system('taskkill /F /T /IM lighttpd.exe')
elif env['r'] == 'd':
    os.system(BROWSER_CMD)
    os.system('python3 build_web/manage.py runserver ' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT)
elif env['t'] == 'w':
    if(platform.system() == "Linux"):
        os.system('python3 build_web/manage.py test version current calcpy')
    elif(platform.system() == "Windows"):
        os.system('python3 build_web\manage.py test version current calcpy')
elif env['t'] == 'j':
    child_process = subprocess.Popen('python3 client/tests/srv.py ', shell=True, stdout=subprocess.PIPE)
    if(platform.system() == "Linux"):
        os.system( WWW_BROWSER + ' ' + os.getcwd() + '/client/unit_test_out.html --disable-web-security')
        os.system("kill " + str(child_process.pid))
    else:
        os.system( 'start "" ' + WWW_BROWSER + ' ' + os.getcwd() + '/client/unit_test_out.html --disable-web-security')
        os.system('taskkill /F /T /PID %d' % child_process.pid)
elif env['cov'] == 1:
    if(platform.system() == "Linux"):
        os.system("coverage run --source build_web/ build_web/manage.py test version current calcpy")
        print("\n")
        os.system("coverage report -m")
        print("\n")
elif env['t'] == 'c':
    if(platform.system() == "Linux"):
        addToLD('./calc')
        os.system('calc/calc_test')
    elif(platform.system() == "Windows"):
        os.system('calc\calc_test.exe')
elif env['t'] == 'f':
    if platform.system() == "Linux":
        os.system('lighttpd -f client/lighttpd.develop')
        command = ['gunicorn', '--chdir', 'build_web', '--log-level','critical',
                   '--timeout', '0', '--workers', '1',
                   '--bind', WEB_SRV_HOST + ':' + WEB_SRV_PORT,
                   'wsgi:application']
        child_process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE)
        os.system('python3 functional_tests.py ' + WWW_BROWSER + ' ' + WEB_CLIENT_HOST + ' ' + WEB_CLIENT_PORT + ' ' + 'f')
        child_process.kill()
        os.system('kill `cat client/lighttpd.pid`')
    else:
        print('Functional tests not available under '+ str(platform.system()) )
elif env['syncdb'] == 1:
    os.system('python3 build_web/manage.py syncdb --noinput')
elif env['zip'] == 1:
    dir_name = os.path.split(os.getcwd())[-1]
    package_name = 'bioweb_' + MYAPP_VER_STRING + '_' + MYAPP_VER_INSTALL + '_' + str(dir_name)
    os.system('zip ' + package_name + '.zip * -r -x client/bower_components/\*')
elif env['doxygen'] == 1:
    f = open('Doxyfile_in', "r")
    w = open('Doxyfile', "w")
    for line in f:
        m = re.match(r'^PROJECT_NUMBER.*$', line)
        if m:
            w.write('PROJECT_NUMBER = ' + MYAPP_VER_STRING + '\n')
        else:
            w.write(line)
    os.system('doxygen')
    env.SideEffect('Doxygen', 'Doxygen_in')
else: #build app
    SConscript(['calc/SConscript', 'web/SConscript', 'client/SConscript'], exports=['env'] )

env.Clean('.','../doc/doxygen')
env.Clean('.','Doxyfile')
