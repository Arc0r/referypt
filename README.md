# referypt
An encryption based on referencing charakters inside a string

## Basic behaviour
Atomatically creates a random organized Key from the base template "abcdefghijklmnopqrstuvwxylzäöü 1234567890,.-;:_!?=ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜ+#-"
It will also provide the encrypted message in the format of integers ( references to the charackters ) seperated by dots e.g. "7.4.11.11.14.26"

## Support of Custom Keys and Messages
Since the encryption process is quit simple, you can manually make a key file and message.
For Example:
The Message "7.4.11.11.14.26" referencing "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.-:" to form the word "HELLO"
Something like 
"0.1.2.2.3" with the key "HALO"
would work to, but with less chars in the message, it is easy to encode.

## Future improvements
better key generation with multiple repeating chars like 'hllooaaloh' so that the same letter in the message reference diffrent parts of the key.
Could transform '7.4.11.11.14.26' to '8.23.86.17.34' which makes less sence, since you can not know that 86 and 17 reference the same letter.
also maybe encode the padding it self to make coping more easy (base64 or something)
