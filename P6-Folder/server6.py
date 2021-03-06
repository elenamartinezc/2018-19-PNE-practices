import http.server
import socketserver
import termcolor
from Seq import Seq

# Define the Server's port
PORT = 8008


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def validSequence(self, s):
        valid = 'ACTG'
        for letter in s:
            if letter not in valid:
                return False
        return True

    def treatingDNA(self, s1, command):
        print("Calculating", command)
        if command == "len":
            return s1.len()
        elif command == "complement":
            return s1.complement().get_strbase()
        elif command == "reverse":
            return s1.reverse().get_strbase()
        elif command == "countA":
            return s1.count('A')
        elif command == "countT":
            return s1.count('T')
        elif command == "countG":
            return s1.count("G")
        elif command == "countC":
            return s1.count("C")
        elif command == "percA":
            return s1.perc("A")
        elif command == "percT":
            return s1.perc("T")
        elif command == "percG":
            return s1.perc("G")
        elif command == "percC":
            return s1.perc("C")
        else:
            return "ERROR"


    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open("form.html", 'r')
            contents = f.read()
        elif '/seq' in self.path:
            contents = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title> SERVER RESPONSE </title>
            </head>
            <body style = "background-color: pink">"""

            petition = self.path.split('=')[1]
            slicing = petition.split('&')
            dna = slicing[0]
            contents = contents + "<p>Sequence: "+dna+"</p>"
            if self.validSequence(dna):
                s1 = Seq(dna)
                if 'len=on' in self.path:
                    length = s1.len()
                    contents = contents + "<p>Longitud: " + str(length) + "</p>"
                operation = self.path.split('operation=')[1].split("&")[0]
                contents = contents + "<p>Operation: " + operation + "</p>"
                base = self.path.split('base=')[1].split("&")[0]
                contents = contents + "<p>Base: " + base + "</p>"
                command = operation + base
                final = self.treatingDNA(s1, command)
                contents = contents + "<p>Answer to the operation: " + str(final) + "</p>"
            else:
                contents = contents + "<p>Error</p>"

            contents = contents + """<br> <a href="/"> [Main page] </a>
                       </body></html>"""


        else:
            f = open('error.html','r')
            contents = f.read()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")