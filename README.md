# Easy-Smartcard
Easy Smartcard v0.1 is small tool to communicate with smartr card, send and receive APDU to smart card
 
 1- install pyscard 1.9.9 this plugin its working with python 3.6 (in my case)
 2- install python 3.6
 
 here is two option to work with gui, you  can direct load mainwindow.ui using (PyQt5.uic import loadUi) or convert .ui to .py
 using pyuic -x mainwindow.ui -o mainwindow.py, the mainwindow.py.
 both .ui, .py attached in this project.
 
here is some script to test with EMV card ( VISA DEBIT)

<< 00 A4 04 00 06 A0 00 00 00 03 10
>> (61 34)

<< 00 C0 00 00 34
>> 6F 32 84 07 A0 00 00 00 03 10 10 A5 27 50 0A 56 69 73 61 20 44 65 62 69 74 87 01 02 5F 2D 04 61 72 65 6E 9F 12 0A 56 69 73 61 20 44      65 62 69 74 9F 11 01 01 (90 00)

<< 80 A8 00 00 02 83 00    
>> (61 10)

<< 00 C0 00 00 10
>> 80 0E 3C 00 08 02 03 00 10 01 01 00 10 02 03 01 (90 00)

<< 00 B2 02 0C 00
>> (61 B6)

<< 00 B2 02 0C B6
>> 70 81 B3 90 81 B0 73 80 F2 79 B3 74 BF BD D4 10 0C C8 6F B5 28 42 69 22 AF 70 18 00 B4 28 BD B2 E2 FD 24 7D 0D D9 89 D2 E5 55 E1 37      B8 94 9F 1B 07 58 CC 73 BA 29 93 A3 34 71 0D 75 27 99 60 A6 97 99 D4 5E CB 2A 15 BB 0A 28 00 C0 52 71 D5 DD A4 E9 B4 AD 3E 7A AB 36      C7 9D C4 4A 23 BB 46 F8 AF A5 AA 1C B3 A0 26 C8 0E 42 4D 2C 65 EB D7 40 85 88 1F C3 C9 35 CE DB B3 03 D3 EA AF 34 D6 1E 8D 28 2C FB      D1 CC A8 3D 93 74 57 62 FF 1F D4 B8 71 7B 8A 43 4F A4 DD FC 48 05 8C E6 9B AD 53 C6 60 3C E2 12 41 86 97 92 1B 70 B3 DC 80 5E 28 70      B9 0A EB 26 3E 7F (90 00)

<< 00 B2 03 0C 00
>> (61 2F)

<< 00 B2 03 0C 2F
>> 70 2D 9F 32 01 03 92 24 8A 35 B7 B4 29 F6 69 93 E2 F0 EB 67 29 1C 66 F4 25 A3 83 9C 9F CE 46 A3 D3 5F 9E 57 9C 7D 0D 63 EA 65 C8 EF      8F 01 92 (90 00)

<< 00 B2 01 14 00
>> (61 C8)

<< 00 B2 01 14 C8
>> 70 81 C5 9F 46 81 B0 61 D6 6B 2B 3D 14 0C E3 7C 64 DF 19 0F 35 BF 63 18 21 32 F3 E3 76 3F EC A9 0D 64 ED A8 37 1C 84 7D C9 9E 9A 51      7F 1E 06 C1 FA 93 4B 82 0C 11 7E 0F DD 7B 04 FF 6E A5 02 CE C5 90 B4 F8 23 7F 3B FD 8E 22 F7 AB 47 60 21 9C B5 36 0D 41 F0 EB C9 AD      97 45 91 DD B3 EC 51 30 24 55 D1 89 40 B2 1C C9 9E D5 61 75 8E 9D 72 41 69 C1 E6 25 3E 1D 80 4A 18 5B 7F AA 5C 2A 96 67 DA BF 13 EE      5C AA 65 18 64 A0 38 03 3F 99 20 9F E9 2D F7 0E FC B7 19 C1 C4 65 E0 99 04 6E 58 0A B4 EB C2 FD 01 3A 24 78 7F 17 1B 3D 15 82 43 C0      EA 0B CE B5 AE E4 0B 9F 47 01 03 9F 48 0A 68 9B A8 A1 37 1B 96 56 5A 7B (90 00)

<< 00 B2 02 14 00
>> (61 54)

<< 00 B2 02 14 54
>> 70 52 5A 08 48 30 10 20 00 00 09 37 5F 34 01 01 8E 14 00 00 00 00 00 00 00 00 42 01 44 02 41 02 42 02 5E 02 1F 02 9F 0D 05 F8 68 AC      88 00 9F 0E 05 00 10 00 00 00 9F 0F 05 F8 68 BC 98 00 5F 24 03 20 02 28 5F 28 02 06 82 9F 07 02 FF 00 5F 25 03 18 07 01 (90 00)

<< 00 B2 03 14 00
>> (61 93)

<< 00 B2 03 14 93
>> 70 81 90 5F 20 1A 53 41 42 49 4E 44 41 53 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 5F 30 02 02 21 9F 49 03 9F 37 04 9F      1F 0E 30 30 30 30 30 35 37 36 30 30 30 30 30 30 57 13 48 30 10 20 00 00 09 37 D2 00 22 21 00 00 05 76 00 01 1F 9F 44 01 02 9F 42 02      06 82 9F 08 02 00 97 9F 4A 01 82 8D 17 8A 02 9F 02 06 9F 03 06 9F 1A 02 95 05 5F 2A 02 9A 03 9C 01 9F 37 04 8C 15 9F 02 06 9F 03 06      9F 1A 02 95 05 5F 2A 02 9A 03 9C 01 9F 37 04 (90 00)


here is some script to test with SIM card (read ICCID SIM card, and SPN)

