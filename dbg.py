import sys

def trace_calls(frame, event, arg):
    global activated_debugger
    global script_to_debug
    if event != 'call':
        print('Event is not call')
        return
    if not activated_debugger:
        print('Mushi this call...')
        return trace_lines
    co = frame.f_code
    filename = co.co_filename
    func_name = co.co_name
    line_no = frame.f_lineno
    print(f"Call to {func_name} at line {line_no} of {filename}")
    input("Press Enter to continue")
    return trace_lines

def trace_lines(frame, event, arg):
    global activated_debugger
    global script_to_debug
    if event != 'line':
        print('Event is not line')
        return
    co = frame.f_code
    filename = co.co_filename
    func_name = co.co_name
    line_no = frame.f_lineno
    locals_dict = frame.f_locals
    globals_dict = frame.f_globals

    if filename == script_to_debug and not activated_debugger:
        print('Activate Debugger!')
        activated_debugger = True
    
    if not activated_debugger:
        print('Mushi this line...')
        return trace_lines
    #print(f"Executing line {line_no} of {filename} in {func_name}. Locals: {locals_dict}, Globals: {globals_dict}")
    print(f"Executing line {line_no} of {filename} in {func_name}")
    input("Press Enter to continue")
    return trace_lines

def start_debugger(script):
    sys.settrace(trace_calls)
    with open(script) as f:
        code = compile(f.read(), script, 'exec')
        exec(code, {}, {})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debugger.py <script_to_debug.py>")
        sys.exit(1)
    activated_debugger = False
    script_to_debug = sys.argv[1]
    # Trick the target script with new sys.argv
    sys.argv = sys.argv[1:]
    start_debugger(script_to_debug)

