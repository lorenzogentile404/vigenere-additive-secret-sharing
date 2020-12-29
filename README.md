# vigenere-addittive-secret-sharing

A Python script implementing a didactical addittive secret sharing scheme inspired by the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

## How it works

In order to split the string `s` of length `ł` into `n` shares it is enough to compute `n-1` random strings `s_1,...,s_{n-1}` of length `l`, then compute the last share as `s_n = s - (s_1 + ... + s_{n-1})`, where `+` and `-` operators works as in the Vigenère cipher.

Note that this is equivalent to convert each char of `s` to an element of the addittive group of integers modulo `26` (`Z_26`) according to the alphabetic order `A = 0, B = 1, ..., Z = 25`. Then use addittive secret sharing for each element. Finally, for `i = 1,...,n` convert the share number `i` of each element to char and concat them. The obtained value represents the Vigenère share number `i`.

For didactical purposes, a table to manually compute operations is below:

![alt text](https://raw.githubusercontent.com/lorenzogentile404/vigenere-addittive-secret-sharing/main/Vigen%C3%A8re_square_shading.svg.png)

## Examples of usage

### Encrypt Vigenère
```console
user@host:~/vigenere-addittive-secret-sharing$ python vigenere_addittive_secret_sharing.py 
Insert expression: meetmeatdawn + worm
meetmeatdawn + worm
isvfisrfzonz
Result: isvfisrfzonz
```

### Decrypt Vigenère
```console
user@host:~/vigenere-addittive-secret-sharing$ python vigenere_addittive_secret_sharing.py 
Insert expression: isvfisrfzonz - worm
isvfisrfzonz - worm
meetmeatdawn
Result: meetmeatdawn
```

### Compute Vigenère shares
```console
user@host:~/vigenere-addittive-secret-sharing$ python vigenere_addittive_secret_sharing.py 
Insert expression: share meetmeatdawn 3
Shares: emqisnqpkwca + znmtzjgvrahb + jfcsviejcenm
```

### Sum Vigenère shares
```console
user@host:~/vigenere-addittive-secret-sharing$ python vigenere_addittive_secret_sharing.py 
Insert expression: emqisnqpkwca + znmtzjgvrahb + jfcsviejcenm
emqisnqpkwca + znmtzjgvrahb + jfcsviejcenm
dzcbrwwkbwjb + jfcsviejcenm
meetmeatdawn
Result: meetmeatdawn
```

```
