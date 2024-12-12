import datetime
def sveiciens(vards):
    return f"Čau, {vards}!"

def datuma_paradisana():
    return f"Šodien ir {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == "__main__":
    lietotaja_vards = input("Ievadi savu vārdu: ")
    print(sveiciens(lietotaja_vards))
    print(datuma_paradisana())
