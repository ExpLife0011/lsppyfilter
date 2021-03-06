# ========================================================================================================================
# LspPyFilter
#
# Copyright �2007 Liam Kirton <liam@int3.ws>
# ========================================================================================================================
# LspPyFilter_Basic.py
#
# Created: 15/05/2007
# ========================================================================================================================

import lsppyfilter

import re
import socket
import struct
import sys

# ========================================================================================================================

def connect_filter(pid, tid, sid, ip, port):
	new_ip = ip
	new_port = port

	str_ip = socket.inet_ntoa(struct.pack('!L', ip))
	str_new_ip = socket.inet_ntoa(struct.pack('!L', new_ip))
	print '[%x, %x, %x] connect_filter(%s, %d) => (%s, %d)' % (pid, tid, sid, str_ip, port, str_new_ip, new_port)
	return (new_ip, new_port)

# ========================================================================================================================

def disconnect_filter(pid, tid, sid):
	print '[%x, %x, %x] disconnect_filter()' % (pid, tid, sid)
	
# ========================================================================================================================

def recv_filter(pid, tid, sid, buffer, length):
	print '[%x, %x, %x] recv_filter(%d)' % (pid, tid, sid, length)
	return buffer

# ========================================================================================================================

def send_filter(pid, tid, sid, buffer, length):
	print '[%x, %x, %x] send_filter(%d)' % (pid, tid, sid, length)
	return buffer

# ========================================================================================================================
	
if __name__ == '__main__':
	lsppyfilter.set_connect_filter(connect_filter)
	lsppyfilter.set_disconnect_filter(disconnect_filter)
	lsppyfilter.set_recv_filter(recv_filter)
	lsppyfilter.set_send_filter(send_filter)
	
	print '\"Filters\\LspPyFilter.py\" Loaded.'

# ========================================================================================================================
