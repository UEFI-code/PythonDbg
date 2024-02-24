import sys

class myCuteDebugger:
    def __init__(self):
        self.activated_debugger = False
        self.script_to_debug = None

    def trace_calls(self, frame, event, arg):
        if event != 'call':
            print(f'Event is not call: {event}!')
            return
        if not self.activated_debugger:
            print('Mushi this call...Game is not started yet!')
            return self.trace_lines
        co = frame.f_code
        filename = co.co_filename
        func_name = co.co_name
        line_no = frame.f_lineno
        print(f"Call to {func_name} at line {line_no} of {filename}")
        input("Press Enter to continue")
        return self.trace_lines
    
    def trace_lines(self, frame, event, arg):
        if event != 'line':
            print(f'Event is not line: {event}!')
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
            return self.trace_lines
        #print(f"Executing line {line_no} of {filename} in {func_name}. Locals: {locals_dict}, Globals: {globals_dict}")
        print(f"Executing line {line_no} of {filename} in {func_name}")
        input("Press Enter to continue")
        return self.trace_lines
    
    def start_debugger(self, script_filename):
        self.script_to_debug = script_filename
        sys.settrace(self.trace_calls)
        with open(self.script_to_debug) as f:
            code = compile(f.read(), self.script_to_debug, 'exec')
            exec(code, {}, {})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debugger.py <script_to_debug.py>")
        sys.exit(1)
    script_to_debug = sys.argv[1]
    # Trick the target script with new sys.argv
    sys.argv = sys.argv[1:]
    myCuteDebugger().start_debugger(script_to_debug)

