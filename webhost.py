import socket
import uselect
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

poller          = uselect.poll()
handlers        = {}
notFoundHandler = None
docPath         = "/"
tplData         = {}

mimeTypes = { 
    ".html": "text/html",
    ".css":  "text/css",
    ".js":   "application/javascript",
    ".json": "application/json",
    ".jpg":  "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png":  "image/png",
    ".ico":  "image/x-icon",
    ".svg":  "image/svg+xml",
}

def begin(port=80):
    server.bind(("0.0.0.0", port))
    server.listen(1)
    poller.register(server, uselect.POLLIN)

def close():
    poller.unregister(server)
    server.close()

def handleClient():
    res = poller.poll(1)
    if res:
        (sock, addr) = server.accept()
        sock.settimeout(5.0)
        handle(sock)
        sock.close()

def __fileExist(path):
    try:
        stat = os.stat(path)
        return stat[0] & 0x8000 == 0x8000
    except:
        return False

def __getMime(path):
    for ext in mimeTypes:
        if path.endswith(ext):
            return mimeTypes[ext]
    return "text/plain"

def __sendFile(socket, path):
    try:
        f = open(path, "rb")
        while True:
            data = f.read(128)
            if data == b"":
                break
            socket.write(data)
        f.close()
    except Exception as e:
        print("Fehler beim Senden:", e)

def err(socket, code, message):
    socket.write("HTTP/1.1 " + code + " " + message + "\r\n")
    socket.write("Content-Type: text/html\r\n\r\n")
    socket.write("<h1>" + code + " " + message + "</h1>")

def ok(socket, code, *args):
    if len(args) == 1:
        content_type = "text/plain"
        msg = args[0]
    elif len(args) == 2:
        content_type = args[0]
        msg = args[1]
    else:
        raise TypeError("ok() takes 3 or 4 positional arguments")
    socket.write("HTTP/1.1 " + code + " OK\r\n")
    socket.write("Content-Type: " + content_type + "\r\n\r\n")
    socket.write(msg)

def handle(socket):
    global docPath, handlers, notFoundHandler

    try:
        currLine = str(socket.readline(), "utf-8")
    except:
        currLine = ""

    request = currLine.split(" ")
    if len(request) != 3:
        return

    (method, url, version) = request

    if "?" in url:
        (path, query) = url.split("?", 2)
    else:
        (path, query) = (url, "")

    args = {}
    if query:
        for argPair in query.split("&"):
            arg = argPair.split("=")
            if len(arg) == 2:
                args[arg[0]] = arg[1]

    while True:
        header = socket.readline()
        if header == b"" or header == b"\r\n":
            break

    if version not in ("HTTP/1.0\r\n", "HTTP/1.1\r\n"):
        err(socket, "505", "Version Not Supported")
        return

    if method != "GET":
        err(socket, "501", "Not Implemented")
        return

    # Registrierte Routen pruefen
    if path in handlers:
        handlers[path](socket, args)
        return

    # Datei im docPath suchen
    # Pfad zusammenbauen: docPath + path ohne fuehrenden Slash
    # z.B. docPath="website/", path="/css/style.css" -> "website/css/style.css"
    stripped = path.lstrip("/")
    filePath = docPath.rstrip("/") + "/" + stripped

    # Sonderfall: Wurzel-Anfrage
    if path == "/" or path == "":
        filePath = docPath.rstrip("/") + "/index.html"

    if __fileExist(filePath):
        mime = __getMime(filePath)
        socket.write("HTTP/1.1 200 OK\r\n")
        socket.write("Content-Type: " + mime + "\r\n\r\n")
        if filePath.endswith(".p.html"):
            f = open(filePath, "r")
            for l in f:
                socket.write(l.format(**tplData))
            f.close()
        else:
            __sendFile(socket, filePath)
    else:
        if notFoundHandler:
            notFoundHandler(socket, path)
        else:
            err(socket, "404", "Not Found")

def onPath(path, handler):
    global handlers
    handlers[path] = handler

def onNotFound(handler):
    global notFoundHandler
    notFoundHandler = handler

def setDocPath(path):
    global docPath
    docPath = path

def setTplData(data):
    global tplData
    tplData = data
