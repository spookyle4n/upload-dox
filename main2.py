# coded by wyatt gierer #

# claiming this script as your own will result in a horrible death #

print(''''\033[31m'

010            001  011      011   110100     10110010010 00110110001
 101          101    111    001   011  101        001         110
  001        110       011 100   1010101100       110         001
   110  00  000          111    000       110     101         101
    010 00 111          010    010          001   001         010
     110 001           100   111             110  111         101     
     
''')

print('''\033[1;32m

		   tiktok:  @jahsehrare
		   instagram: @spookyle4n

''')

use_nouse = str(input(' [?] wanna dox someone? [y/N]: '))
if use_nouse == 'N': exit()

if use_nouse == 'y':
    first_name = input("\n\033[36m[*] First Name: ")
    last_name = input("\n\033[36m[*] Last Name: ")
    address = input("\n\033[36m[*] Address: ")
    date = input("\n\033[36m[*] date: ")
    time = input("\n\033[36m[*] time: ")
    use_nouse = str(input("\n\033[36m[?] you sure you want to do this? ? [y/N]: "))
    if use_nouse == 'N': exit()

print("victims first name : " + " " + first_name + " " + "[*]")
print("victims last name : " + " " + last_name + " " + "[*]")
print("victims address : " + " " + address + " " + "[*]")
print("date of victims attack : " + " " + date + " " + "[*]")
print("time of victims attack : " + " " + time + " " + "[*]")

use_nouse = str(input(' is this information correct? [y/N] + " " + :'))
if use_nouse == 'N': exit()

import time

for i in range(5):
    print('   .\t', end=' ', flush=True)
    time.sleep(1)

import time

for i in range(1000):
    print('nuking [!]', end=' ', flush=True)
    time.sleep(0.05)
