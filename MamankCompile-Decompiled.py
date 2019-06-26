# uncompyle6 version 3.3.3
# Python bytecode 3.7
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 11:21:56) 
# [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
import os, marshal, sys, time

def runntxt(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.022222222222222223)


os.system('clear')
runntxt('\x1b[34;1m┌┬┐┌─┐┌┬┐┌─┐┌┐┌┬┌─  \x1b[31;1m╔═╗╔═╗╔╦╗╔═╗╦╦  ╔═╗')
runntxt('\x1b[34;1m│││├─┤│││├─┤│││├┴┐  \x1b[31;1m║  ║ ║║║║╠═╝║║  ║╣ ')
runntxt('\x1b[34;1m┴ ┴┴ ┴┴ ┴┴ ┴┘└┘┴ ┴  \x1b[31;1m╚═╝╚═╝╩ ╩╩  ╩╩═╝╚═╝ \x1b[33;1mVersion 1.0 \x1b[34;1m(Private)')
runntxt('\x1b[33;1mTerhindar Dari : Recode')
runntxt('\x1b[1;41;36mSimple Marshal Compiler By SmileBitch21   \x1b[0;0m')
print('\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=')
runntxt('\x1b[33;1m[@] Example : \x1b[36;1m/sdcard/nama.py or nama.py')
print('')
inp = input('\x1b[0;1m[?] Input Your File : ')
file = open(inp).read()
com = compile(file, '', 'exec')
dum = marshal.dumps(com)
file_out = open('ENC' + inp, 'w')
file_out.write('#Tercompiled By : SmileBitch21\n')
file_out.write('#GitHub : https://github.com/SmileBitch21\n')
file_out.write('import marshal\n')
file_out.write('exec(marshal.loads(' + repr(dum) + '))')
file_out.close()
os.system('clear')
runntxt('\x1b[34;1m┌┬┐┌─┐┌┬┐┌─┐┌┐┌┬┌─  \x1b[31;1m╔═╗╔═╗╔╦╗╔═╗╦╦  ╔═╗')
runntxt('\x1b[34;1m│││├─┤│││├─┤│││├┴┐  \x1b[31;1m║  ║ ║║║║╠═╝║║  ║╣ ')
runntxt('\x1b[34;1m┴ ┴┴ ┴┴ ┴┴ ┴┘└┘┴ ┴  \x1b[31;1m╚═╝╚═╝╩ ╩╩  ╩╩═╝╚═╝')
runntxt('\x1b[1;41;36mSimple Marshal Compiler By SmileBitch21   \x1b[0;0m')
print('\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=\x1b[36;1m=')
print('')
runntxt('[√] \x1b[32;1m Tercompiled : ENC' + inp)