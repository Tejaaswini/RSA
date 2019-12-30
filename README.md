# RSA
RSA (Rivest–Shamir–Adleman) is an asymmetric algorithm used by modern computers to encrypt and decrypt messages. Also called public key cryptography.

RSA algorithm:

      1. Generate two large random primes, p and q, of approximately equal size such that their product n=pq is of the required
         bit length.
      2. Compute n=pq and ϕ=(p−1)(q−1).
      3. Choose an integer e, 1<e<ϕ, such that gcd(e,ϕ)=1.
      4. Compute the secret exponent d, 1<d<ϕ, such that ed≡1modϕ.
      5. The public key is (n,e) and the private key (d,p,q). Keep all the values d, p, q and ϕ secret.
      
What is Tkinter?

Python offers multiple options for developing GUI of which tkinter is most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python along with tkinter outputs the fastest and easiest way to create the GUI applications.

For **Python 2.X** the name of the module is called **Tkinter** and in **Python 3.X** it is called **tkinter**

Tkinter Documentation (https://docs.python.org/3/library/tk.html)
