import OSC

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

if __name__ == "__main__":
    s = OSC.OSCServer(('127.0.0.1', 12345))  # listen on localhost, port 57120
    s.addMsgHandler('/openbci', handler)     # call handler() for OSC messages received with the /startup address
    s.serve_forever()