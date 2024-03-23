import time
import hashlib
import itertools

#for encrypting passwords
def hash(guess):
    hash = hashlib.sha256(guess.encode('utf-8'))
    return hash.hexdigest()
start_time = time.time()
data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','=','_','+']
password = ''
guess = ''
hash_guess=''
if hash_guess != password:
    for i in range(len(data)):
        for subset in itertools.permutations(data, i):
            guess = ''.join(subset)
            hash_guess = hash(guess)
            print(guess)
            if hash_guess == password:
                print(f"Your password is " + guess)
                print(time.time() - start_time)
                exit()

print(f"Your password is " + guess)
