# -*- coding utf-8 -*-
# @Time : 2023/12/26 19:11
import random

from Crypto.Util.number import *
flag = b'*'*42

e = random.randint(0,2**64)

nbits = 2048
pad = lambda m: m + b'\x00' * (nbits // 8 - len(m) - 1)

p, q = getPrime(nbits // 2), getPrime(nbits // 2)
n = p * q
m = bytes_to_long(pad(flag))
print(len(pad(flag)))
c1 = (pow(m, 8, n) + pow(e, 3, n)) % n
c2 = (pow(m, 6, n) + pow(e, 2, n)) % n

assert len(flag) < 45
print(f"{n = }\n{c1 = }\n{c2 = }")
# n = 21591309125127568360191469245648179213101200314275681167806891421001002208555407334141866878615465048821876928963394065201616843423328788368880777072143397139726607176524723009329201276059962337011360672755504583292090110989693007138486191173034651514206081268358772973496044163293692713688324147640827109129603494052524949278266578044950622093263025079557500216464732387132795260864212736148961631773029069945159209378567085182970172027362453348160274308014829554775936013127944611636173583727668094948580653768919041685052914113640276654247164780515161963748454634271653440272162179353770135346801273520218630975583
# c1 = 10242685893928016549553289428867281405314675729523006642497346931765477840572126582447305233158372733359013787643459902669508598381289106769416421880752838504398561348463659390127177989564820280963704962912804132353781304189694751592587616935176199138371941814109972322159084182810594778946894314381317841784878348145558522439570881989108596344860603603687907513697417198522831367637363709842649055665549235770130904811522054115157694099362633822425075863727993683739827308312579800169935121182709241908676718512380740479872163392576843857780232291372359637603808237251775170134930855168348366700706216982926696827277
# c2 = 14505857655376150682111769804216257256125216816379436427354243031750891362218267707338834281761236038465885378021694333309468610892350021263684421170967681465969547559213925997131326563534985779369245988336586130066282402494124640581173448889551857490577136107820812144698509485130466547090186149907595400909008770236962062757028176844674635195809803121773776445225808435421820107290796303316109683166588226000277893045106933582720187736969318657023544060611534183029018859908858382326140286227071130028071435985726042100962839207178266283934327088058729902795224862410848518482881042198136448823296963016328918063651