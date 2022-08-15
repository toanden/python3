import random

def game_start():
    pc_choice = random.choice(["keo", "bua", "bao"])
    player_choice = input("keo, bua, bao?.........")
    return player_choice, pc_choice

def check_win(key):
    check = {("bua","bua"): "hoa", ("bua","keo"): "thang", ("bua","bao"): "thua", ("keo","bua"): "thua", ("keo","keo"): "hoa", ("keo","bao"): "thang", ("bao","bua"): "thang", ("bao","keo"): "thua", ("bao","bao"): "hoa",}
    return check[key]

turn = 1
result = list()
while True:
    print(f"ROUND {turn}!!!!!")
    result.append(check_win(game_start()))
    turn += 1
    if turn > 5: break

thang, hoa, thua = [result.count("thang"), result.count("hoa"), result.count("thua")]
print(thang, hoa, thua)