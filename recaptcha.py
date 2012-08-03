#!/usr/bin/python

import urllib, urllib2

recaptcha_private_key = '...[your private key goes here]...'

recaptcha_server_name = 'http://www.google.com/recaptcha/api/verify'

def to_bytestring (s):
    """Convert the given unicode string to a bytestring, using the standard encoding,
    unless it's already a bytestring"""
    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf-8')

def check (client_ip_address, recaptcha_challenge_field, recaptcha_response_field):
    """Return the recaptcha reply for the client's challenge responses"""
    params = urllib.urlencode(dict(privatekey=recaptcha_private_key,
                                   remoteip=client_ip_address,
                                   challenge=recaptcha_challenge_field,
                                   response=to_bytestring(recaptcha_response_field)))
    data = None
    try:
        f = urllib2.urlopen(recaptcha_server_name, params)
        data = f.read()
        f.close()
    except HTTPError:
        pass
    except URLError:
        pass
    return data

def confirm (client_ip_address, recaptcha_challenge_field, recaptcha_response_field):
    """Return True/False based on the recaptcha server's reply"""
    result = False
    reply = check (client_ip_address, recaptcha_challenge_field, recaptcha_response_field)
    if reply:
        if reply.lower().startswith('true'):
            result = True
    return result
