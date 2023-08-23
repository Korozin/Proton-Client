if __name__ == "__main__":
    print("This is a module that is imported by 'uGecko.py'. Don't run it directly.")
    exit()
else:
    import re

def IP_Verification(ip: str) -> bool:
	if not bool(re.compile(r'[^0-9.]').search(ip)):
		ip_split = ip.split('.')
		if len(ip_split) != 4: return False
		try: return all(0 <= int(p) < 256 for p in ip_split)
		except ValueError: return False
	else: return False

def Code_Verification(code: str) -> bool:
    lines = code.strip().split('\n')
    for line in lines:
        if '#' in line:
            if len(line.strip()) != 18: return False
        else:
            if len(line.strip()) != 17: return False
            parts = line.strip().split()
            if len(parts) != 2: return False
            if len(parts[0]) != 8 or len(parts[1]) != 8: return False
            if not all(c in '0123456789ABCDEFabcdef' for c in (parts[0]+parts[1])): return False
    return True
