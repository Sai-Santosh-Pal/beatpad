import requests
URL = [
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/kick.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/snare.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/hihat.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/clap.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/tom.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/hihat.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/openhat.wav",
    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/67723/tink.wav",
]

def donwload(url):
    filename = url.split("/")[-1]  # get file name from URL
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print("Failed to download file:", response.status_code)

for i in URL:
    donwload(i)