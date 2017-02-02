import sys
import pexpect
from flask import Flask
switch_un = "cscworks"
switch_pw = "kerner2"
app = Flask(__name__)

@app.route('/api/v1/')
def api_v1():
	print("test")
	child = pexpect.spawn('ssh %s@%s' % (switch_un, switch_ip))
    	return 'Hello, World!'

@app.route('/api/v1/interfaceshutdown/<switchname>/<interface>/<port>/')
def interfaceshutdown(switchname,interface,port):
    return 'Switch %s - %s/%s' % (switchname,interface,port)

@app.route('/api/v1/interfaceshutdown/<switchname>/<interface>/<subport>/<port>/')
def interfaceshutdownlong(switchname,interface,subport,port):
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
     child.sendline("interface Gi1/%s/%s" % (subport,port))
     child.expect('\(config-if\)#')
     child.sendline("shut")
     child.expect('\(config-if\)#')
     return "Switch"  
  except pexpect.TIMEOUT:
     return "{error : switch could not be reached}"
  except pexpect.EOF:
     return "{error : switch could not be reached}"

@app.route('/api/v1/interfaceenable/<switchname>/<interface>/<subport>/<port>/')
def interfaceenablelong(switchname,interface,subport,port):
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
     child.sendline("interface Gi1/%s/%s" % (subport,port))
     child.expect('\(config-if\)#')
     child.sendline("no shut")
     child.expect('\(config-if\)#')
     return "Switch"
  except pexpect.TIMEOUT:
     return "{error : switch could not be reached}"
  except pexpect.EOF:
     return "{error : switch could not be reached}"

@app.errorhandler(404)
def page_not_found(error):
    return "No valid API call", 404

