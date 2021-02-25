#http://www.science.smith.edu/~nhowe/teaching/csc151/hw/hw1/
####  using code from https://www.kite.com/python/docs/sys.stdout
import sys
sys.stdout.write("Output")  
####


def shiftLetter(letter, numshifts):
  asciilett = ord(letter)  
  
  if (asciilett >= 65) and (asciilett <= 90): #for uppercase letters
      shiftedascii = (asciilett + numshifts) 
      if (shiftedascii > 90): #incase the shifted values needs to wrap around the alphabet in encrypting
        x = shiftedascii - 90
        shiftedascii = x + 64
      if (shiftedascii < 65): #incase the shifted values needs to wrap around the alphabet in decrypting
        x = 65 - shiftedascii
        shiftedascii = 91 - x 
      else:
        shiftedascii = shiftedascii            
      return chr(shiftedascii)

  elif (asciilett >= 97) and (asciilett <= 122): #for lowercase letter
      shiftedascii = (asciilett + numshifts) 
      if (shiftedascii > 122): #incase the shifted values needs to wrap around the alphabet in encrypting
        x = shiftedascii - 122
        shiftedascii = x + 96
      if (shiftedascii < 97): #incase the shifted values needs to wrap around the alphabet in decrypting
        x = 97 - shiftedascii
        shiftedascii = 123 - x   
      else:
        shiftedascii = shiftedascii   
      return chr(shiftedascii)
  else:
    return chr(asciilett)   


def shiftMessage(message, padshifts):
    msglist = list(message) 
    for i in range (0, len(msglist)):
      x = shiftLetter(msglist[i], padshifts[i]) #applies shiftLetter() for each character in the msglist
      x = str(x) 
      msglist[i] = x #this replaces the list item with its shifted verison 
    encry = "".join(msglist)
    return encry


#returns the encrypted message using shifMessage()  
def encipher(message):
    return shiftMessage(message, padshifts)


#this negates each of the values in our padshifts list so that shiftMessage() can use it as an arguement to decrypt the message 
def decipher(message):
    for i in range (0, len(padshifts)): 
      padshifts[i] = padshifts[i] * -1    
    return shiftMessage(message, padshifts)


msg = ''' "[C]ro eorcc hlhaz bb q dgumqr jldsl dt xdir ckbcuszao, wryw gg, yexnc mljdqtbbbe. Iwo biawc U udkbvl, tq N'o joubveszpm, phuqux pmze hpek vpdwfj. Kgxctr uxuh mmnt qzjo, wlt fn tcpj-nsfmgzhs." -- Txykv Jqjsvegy, "rkr Oquvhy fy dki Ybuokwal," GHZM wbpvoh, mghhcceo vi Igpdhwpr-Ully Obwlpkcu (HIB), EZLXZ, xez PVWUEX, z yuquidlxqji afdcrbxi lor wvzakwll. [zhuid://afv.bi/2SjZpaY] '''

#reads the pad file as a string to the variable  'pad'
with open('pad.txt', 'r') as file:
    pad = file.read()


#creates the list 'padlist' with the number of shifts from each pad character
padlist = list(pad)
padshifts  = []  
for s in padlist:
  num = ord(s)
  num = num - 65
  padshifts.append(num)


def mains():  
  #### using code from https://www.kite.com/python/docs/sys.stdout
  sys.stdout = open("deciphered.txt", "w")

  encrypted = encipher(msg)
  print("Encrypted: " + encrypted + "\n")
  decrypted = decipher(encrypted)
  print("decrypted: " + decrypted + "\n")
  
  sys.stdout.close()
  ####



if __name__ == "__main__":
  mains()




