import requests
import time
from multiprocessing import Process

file_url = "http://speedtest-ny.turnkeyinternet.net/10000mb.bin"


def download(file_url):
    response = requests.get(file_url, stream=True)
    with open("10000mb.bin", "wb") as file:
        chunk_index = 0
        for chunk in response.iter_content(chunk_size=1024 * 1024 * 10):
            # Chunks of 10 megabytes
            if chunk:
                chunk_array = bytearray(chunk)
                file.write(chunk_array)
                print("Writing chunk " + str(chunk_index + 1) + " of 1000")
                chunk_index += 1


def scheduler(file_url):
    while 1:
        download(file_url)
        time.sleep(600)
        # After download, sleep for five minutes then start again


if __name__ == "__main__":
    p1 = Process(target=scheduler, args=(file_url,))
    p1.start()
