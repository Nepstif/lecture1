
url = "http://github.com/carbonfive/raygun"


def domain_name(url):
    if "www" in url:
      return url.split(".",2)[1]
    else:
        url_domen = url.split("://")[1]
        return url_domen.split(".",1)[0]


print(domain_name(url))


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"