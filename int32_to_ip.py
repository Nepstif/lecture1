
int32 = 2149583361


def int32_to_ip(int32):
    ls_ip = list()
    n = 3
    while n >= 0:
        ip_adres = int(int32 / 256 ** n)
        int32 -= ip_adres * 256 ** n
        ls_ip.append(str(ip_adres))
        n -= 1
    str_ip = ".".join(ls_ip)
    return str_ip


print(int32_to_ip(int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
