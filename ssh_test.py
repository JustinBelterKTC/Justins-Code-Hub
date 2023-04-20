pip3 install paramiko
import paramiko as pk

def start_connection():
  u_name = 'root'
  passwd = 'nagiosxi'
  port = 22
  r_ip = '192.168.5.67'
  
  myconn = paramiko.SSHClient()
  myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  session = myconn.connect(r_ip, username=u_name, password=passwd, port=port)

  remote_cmd = 'ip addr'
  (stdin, stdout, stderr) = myconn.exec_command(remote_cmd)
  print("{}".format(stdout.read()))
  print("{}".format(type(myconn)))
  myconn.close()
  
if __name__ == '__main__':
  start_connection()
