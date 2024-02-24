import dbg2
import types

def my_new_cute_handler(self, filename, func_name, line_no, event, locals_dict, globals_dict):
    if event == 'return':
        print('Event is return')
        return
    if func_name == '<module>' and event == 'call':
        print(f'Seams like our module {filename} is being initialized...')
        return
    print(f"Executing line {line_no} of {filename} in {func_name}, Event: {event}")
    input("Press Enter to continue")

if __name__ == "__main__":
    myCuteDbgger = dbg2.myCuteDebugger()
    # Let's replace the original handler with our new handler
    myCuteDbgger.my_cute_handler = types.MethodType(my_new_cute_handler, myCuteDbgger)
    myCuteDbgger.start_debugger()