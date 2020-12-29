# vigenere-additive-secret-sharing

A Python script implementing a didactical additive secret sharing scheme inspired by the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

## How it works

In order to split the string `s` of length `l` into `n` shares it is enough to compute `n-1` random shares `s_1,...,s_{n-1}` as strings of the same length `l`, then compute the last share as `s_n = s - (s_1 + ... + s_{n-1})`, where `+` and `-` operators works as in the Vigenère cipher.

Note that this is equivalent to convert each char of `s` to the corresponding element of the additive group of integers modulo `26` (`Z_26`) according to the alphabetic order `A = 0, B = 1, ..., Z = 25`. Then use additive secret sharing for each element. Finally, for `i = 1,...,n` convert the share number `i` of each element to char and concat them. The obtained value represents the Vigenère share number `i`.

For didactical purposes, a table to manually compute `+` and `-` operations between strings is available below:

![alt text](https://raw.githubusercontent.com/lorenzogentile404/vigenere-additive-secret-sharing/main/Vigen%C3%A8re_square_shading.svg.png)

## Privacy preserving addition

The presented additive secret sharing scheme can be used to compute privacy preserving addition among strings. Below an example with `3` parties computing `s = s_1 + s_2 + s_3` is described:

- Each party `P_i` splits its secret `s_i` into `3` ordered shares `s_i1`,`s_i2`, `s_i3` and sends `s_ij` to each other party `P_j`. Note that party `P_i` keeps `s_ii` secret, so the privacy of `s_i` is preserved.

- Then each party `P_i` owns `s_ji` for `j = 1,2,3`, *i.e*, party `P_i` owns all shares number `i` of each secret, so it computes the partial sum `p_i = s_1i + s_2i + s_3i` and brodcasts it to the other parties.

- Finally, each party party `P_i` sums up its partial sum with the those received from the other parties `s = p_1 + p_2 + p_3`. Note that the result is correct since `p_1 + p_2 + p_3 = (s_11 + s_21 + s_31) + (s_12 + s_22 + s_32) + (s_13 + s_23 + s_33) = (s_11 + s_12 + s_13) + (s_21 + s_22 + s_23) + (s_31 + s_32 + s_33) = s_1 + s_2 + s_3 = s`.

The following table shows how the scheme works with actual inputs. In this case `P_1` owns `s_1 = "secreta"`, `P_2` owns `s_2 = "secretb"`, `P_3` owns `s_3 = "secretc"` and they want to compute `s = s_1 + s_2 + s_3 = "cmgzmfd"` while preserving the privacy of their inputs:   

```
| Party     | Secrets to add | First shares (P_1) | Second shares (P_2) | Third shares (P_3) | Hor. sums |
|-----------|----------------|--------------------|---------------------|--------------------|-----------|
| P_1       | secreta        | qbtozkz            | wbpmeem             | gcurbfp            | secreta   |
| P_2       | secretb        | dgvihlj            | ysofadn             | rgtexff            | secretb   |
| P_3       | secretc        | vfwqkpx            | grnrnjm             | ritkhvt            | secretc   |
| Ver. sums | cmgzmfd        | omkmqkf            | akqirql             | oqgfffn            | cmgzmfd   |
```

## Examples of usage

### Encrypt Vigenère
```console
user@host:~/vigenere-additive-secret-sharing$ python vigenere_additive_secret_sharing.py 
Insert expression: meetmeatdawn + worm
meetmeatdawn + worm
isvfisrfzonz
Result: isvfisrfzonz
```

### Decrypt Vigenère
```console
user@host:~/vigenere-additive-secret-sharing$ python vigenere_additive_secret_sharing.py 
Insert expression: isvfisrfzonz - worm
isvfisrfzonz - worm
meetmeatdawn
Result: meetmeatdawn
```

### Compute Vigenère shares
```console
user@host:~/vigenere-additive-secret-sharing$ python vigenere_additive_secret_sharing.py 
Insert expression: share meetmeatdawn 3
Shares: emqisnqpkwca + znmtzjgvrahb + jfcsviejcenm
```

### Sum Vigenère shares
```console
user@host:~/vigenere-additive-secret-sharing$ python vigenere_additive_secret_sharing.py 
Insert expression: emqisnqpkwca + znmtzjgvrahb + jfcsviejcenm
emqisnqpkwca + znmtzjgvrahb + jfcsviejcenm
dzcbrwwkbwjb + jfcsviejcenm
meetmeatdawn
Result: meetmeatdawn
```
