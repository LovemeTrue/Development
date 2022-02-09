import speedtest

download_speed = speedtest.Speedtest().download()

print(download_speed / (2 ** 20))


upload_speed = speedtest.Speedtest().upload()

print(upload_speed / (2 ** 20))
