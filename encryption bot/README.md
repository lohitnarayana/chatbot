# ENCRYPTION BOT
Encryption bot is a kind of rule based chatbot which encrypts the given text or sentence 
same way it decrypts the given text or sentence

algorithm used for encryption and decryption is rsa (Rivest, Shamir and Adleman)

chat bot interface is done using flask

how to execute?
1) pip install -r requirements.txt
2) set path cd "path of file"
3) python main.py
4) http://127.0.0.1:5000

rsa description :
	The RSA algorithm holds the following features −

		RSA algorithm is a popular exponentiation in a finite field over integers including prime numbers.

		The integers used by this method are sufficiently large making it difficult to solve.

		There are two sets of keys in this algorithm: private key and public key.

You will have to go through the following steps to work on RSA algorithm −
step 1 : 
		The initial procedure begins with selection of two prime numbers namely p and q, and then calculating their product N
						N=p*q
step 2 :
		 Consider number e as a derived number which should be greater than 1 and less than (p-1) and (q-1). The primary condition will be that there should be no common factor of (p-1) and (q-1) except 1
		 				N1 = (p-1)*(q-1)
step 3 :
		find e such that gcd( N1 , e) equals to 1
					gcd( N1 , e) == 1
step 4 :
		find d such that (d * e mod N1) ==  1
		or (d * _ )mod N1 == 1
		 find the value that satisfies 
step 5 :
 		public key will be in the formate 
 				{e,N}
step 6 :
		private key will be in the formate
				{d,N}

step 7 : for cipher text we use
			cipher_text = (M power e) mod N
			where M is the text we need to encrypt
		 
		 for decrypt the cipher text we use
			M = (cipher_text power d)mod N


