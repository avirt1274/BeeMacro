import subprocess


class CMD():
    def __init__(self) -> None:
        pass
    
    def call(command:str):
        """Use command in cmd"""
        result = b''

        process = subprocess.Popen(['cmd', '/C', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if out:
            result += out.decode('cp866').encode('utf-8')
        if err:
            result += err.decode('cp866').encode('utf-8')
        return result

    def check_validable(command:str):
        """Checking th CALL valibility"""
        try:
            return CMD.call(command)
        except:
            return False
        else:
            return True
