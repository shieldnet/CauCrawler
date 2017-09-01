import time

def _log(input_str, FUNCTION_STR):
    t = time.localtime()
    BASE_LOG = str(time.asctime(t)) + " :: " + FUNCTION_STR + input_str
    print(BASE_LOG)