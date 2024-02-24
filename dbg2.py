import sys

class myCuteDebugger:
    def __init__(self):
        self.activated_debugger = False
        self.script_to_debug = None
    
    def trace_callback(self, frame, event, arg):
        if event == 'return':
            print('Event is return')
            return
        co = frame.f_code
        filename = co.co_filename
        func_name = co.co_name
        line_no = frame.f_lineno
        locals_dict = frame.f_locals
        globals_dict = frame.f_globals

        if filename == self.script_to_debug and not self.activated_debugger:
            print('Activate Debugger!')
            self.activated_debugger = True
        
        if not self.activated_debugger:
            print('Mushi this line...Game is not started yet!')
            return self.trace_callback
        
        print(f"Executing line {line_no} of {filename} in {func_name}, Event: {event}")
        input("Press Enter to continue")
        return self.trace_callback
    
    def start_debugger(self, script_filename):
        self.script_to_debug = script_filename
        sys.settrace(self.trace_callback)
        with open(self.script_to_debug) as f:
            code = compile(f.read(), self.script_to_debug, 'exec')
            exec(code, {}, {})
            print('Goodbye!')
            sys.settrace(None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debugger.py <script_to_debug.py>")
        sys.exit(1)
    script_to_debug = sys.argv[1]
    # Trick the target script with new sys.argv
    sys.argv = sys.argv[1:]
    myCuteDebugger().start_debugger(script_to_debug)

