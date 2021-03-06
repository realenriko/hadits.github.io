proc = subprocess.Popen("php ahmad.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()