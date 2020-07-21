class Tail(object):

    def __init__(self):
        self.buffer       = str()
        self.tail_command = ['/usr/bin/sudo', '/usr/bin/tail', '-F', '-n0']

    def process(self,filename):

        process = subprocess.Popen(
            self.tail_command + [filename], stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    
        # set non-blocking mode for file
        function_control = fcntl.fcntl(process.stdout, fcntl.F_GETFL)
        fcntl.fcntl(process.stdout, fcntl.F_SETFL, function_control | os.O_NONBLOCK)
    
        function_control = fcntl.fcntl(process.stderr, fcntl.F_GETFL)
        fcntl.fcntl(process.stderr, fcntl.F_SETFL, function_control | os.O_NONBLOCK)
        
        return process
    
    def f(self, filename):

        empty   = None
        process = self.process(filename)
        
        while True:
            reads, writes, errors = select.select(
                [process.stdout, process.stderr], [], [process.stdout, process.stderr], 0.1
            )
            if process.stdout in reads:
                self.buffer += str(process.stdout.read())
                lines = self.buffer.split('\n')
                
                if '' in lines[-1]:
                    #whole line received
                    self.buffer = str()
                else:
                    self.buffer = lines[-1]

                # Start of Python interoperability patch
                if not lines[:-1]:
                    empty = True
                    lines = lines[-1]
                else:
                    empty = False
                    lines = lines[:-1]
    
                if lines and not empty:
                    for line in lines:
                        yield line
                else:
                    yield lines
                # End of Python interoperability patch
                    
            if process.stderr in reads:
                stderr_input = process.stderr.read()
    
            if process.stderr in errors or process.stdout in errors:
                print("Error received. Errors: ", errors)
                process = self.process(filename)
