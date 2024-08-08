import subprocess


class CMD():
    def output(self, command:str):
        """Output of CALL"""
        output = CMD.call(command=command)
        return output
    
    def call(self, command:str):
        """Use command in cmd"""
        result = b''

        process = subprocess.Popen(['cmd', '/C', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if out:
            result += out.decode('cp866').encode('utf-8')
        if err:
            result += err.decode('cp866').encode('utf-8')
        return result

    def check_validable(self, command:str):
        """Checking th CALL valibility"""
        try:
            return CMD.call(command)
        except:
            return False
        else:
            return True
