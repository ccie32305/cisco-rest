import sys
import pexpect
from flask import Flask
switch_un = "none"
switch_pw = "none"

def interfacechange(switch_un,switch_pw,switchname,fullinterface,command):
  try:
     child = pexpect.spawn('telnet %s' % switchname)
     child.timeout = 1
     child.expect('Username:')
     child.sendline(switch_un)
     child.expect('Password:')
     child.sendline(switch_pw)
     child.expect('#')
     child.sendline("conf t")
     child.expect('\(config\)#')
     child.sendline("interface %s" % fullinterface)
     child.expect('\(config-if\)#')
     child.sendline("%s" % command)
     child.expect('\(config-if\)#')
     return "{success : %s - %s}" % (switchname,fullinterface)
  except pexpect.TIMEOUT:
     return "{error : switch could not be reached}"
  except pexpect.EOF:
     return "{error : switch could not be reached}"
 
 
app = Flask(__name__)

@app.route('/api/v1/')
def api_v1():
    	return '{success : cisco-rest-api'

@app.route('/api/v1/interfaceshutdown/<switchname>/<interface>/<port>/')
def interfaceshutdown(switchname,interface,port):
    fullinterface = interface + '/' + port
    return interfacechange(switch_un,switch_pw,switchname,fullinterface,'shut')

@app.route('/api/v1/interfaceshutdown/<switchname>/<interface>/<subport>/<port>/')
def interfaceshutdownlong(switchname,interface,subport,port):
    fullinterface = interface + '/' + subport + '/' + port
    return interfacechange(switch_un,switch_pw,switchname,fullinterface,'shut')

@app.route('/api/v1/interfaceenable/<switchname>/<interface>/<subport>/<port>/')
def interfaceenablelong(switchname,interface,subport,port):
    fullinterface = interface + '/' + subport + '/' + port
    return interfacechange(switch_un,switch_pw,switchname,fullinterface,'no shut')

@app.errorhandler(404)
def page_not_found(error):
    return "{error : no valid API call}", 404

