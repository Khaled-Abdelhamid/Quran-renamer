#!/usr/bin/env python
# coding: utf-8

from glob import glob
from tqdm import tqdm
import click
import os
       
arabic_names={1:"001-الفاتحة",
2:"002-البقرة",
3:"003-آل عمران",
4:"004-النساء",
5:"005-المائدة",
6:"006-الأنعام",
7:"007-الأعراف",
8:"008-الأنفال",
9:"009-التوبة",
10:"010-يونس",
11:"011-هود",
12:"012-يوسف",
13:"013-الرعد",
14:"014-ابراهيم",
15:"015-الحجر",
16:"016-النحل",
17:"017-الإسراء",
18:"018-الكهف",
19:"019-مريم",
20:"020-طه",
21:"021-الأنبياء",
22:"022-الحج",
23:"023-المؤمنون",
24:"024-النور",
25:"025-الفرقان",
26:"026-الشعراء",
27:"027-النمل",
28:"028-القصص",
29:"029-العنكبوت",
30:"030-الروم",
31:"031-لقمان",
32:"032-السجدة",
33:"033-الأحزاب",
34:"034-سبأ",
35:"035-فاطر",
36:"036-يس",
37:"037-الصافات",
38:"038-سورة ص",
39:"039-الزمر",
40:"040-غافر",
41:"041-فصلت",
42:"042-الشورى",
43:"043-الزخرف",
44:"044-الدخان",
45:"045-الجاثية",
46:"046-الأحقاف",
47:"047-محمد",
48:"048-الفتح",
49:"049-الحجرات",
50:"050-سورة ق",
51:"051-الذاريات",
52:"052-الطور",
53:"053-النجم",
54:"054-القمر",
55:"055-الرحمن",
56:"056-الواقعة",
57:"057-الحديد",
58:"058-المجادلة",
59:"059-الحشر",
60:"060-الممتحنة",
61:"061-الصف",
62:"062-الجمعة",
63:"063-المنافقون",
64:"064-التغابن",
65:"065-الطلاق",
66:"066-التحريم",
67:"067-الملك",
68:"068-القلم",
69:"069-الحاقة",
70:"070-المعارج",
71:"071-نوح",
72:"072-الجن",
73:"073-المزمل",
74:"074-المدثر",
75:"075-القيامة",
76:"076-الإنسان",
77:"077-المرسلات",
78:"078-النبأ",
79:"079-النازعات",
80:"080-عبس",
81:"081-التكوير",
82:"082-الإنفطار",
83:"083-المطففين",
84:"084-الانشقاق",
85:"085-البروج",
86:"086-الطارق",
87:"087-الأعلى",
88:"088-الغاشية",
89:"089-الفجر",
90:"090-البلد",
91:"091-الشمس",
92:"092-الليل",
93:"093-الضحى",
94:"094-الشرح",
95:"095-التين",
96:"096-العلق",
97:"097-القدر",
98:"098-البينة",
99:"099-الزلزلة",
100:"100-العاديات",
101:"101-القارعة",
102:"102-التكاثر",
103:"103-العصر",
104:"104-الهمزة",
105:"105-الفيل",
106:"106-قريش",
107:"107-الماعون",
108:"108-الكوثر",
109:"109-الكافرون",
110:"110-النصر",
111:"111-المسد",
112:"112-الإخلاص",
113:"113-الفلق",
114:"114-الناس"}

english_names = {1:"001 - Al-Fatiha",
    2:"002 - Al-Baqara",
    3:"003 - Aal-e-Imran",
    4:"004 - An-Nisa",
    5:"005 - Al-Maeda",
    6:"006 - Al-An'aam",
    7:"007 - Al-A'raf",
    8:"008 - Al-Anfal",
    9:"009 - At-Tawba",
    10:"010 - Yunus",
    11:"011 - Hud",
    12:"012 - Yusuf",
    13:"013 - Ar-Ra'd",
    14:"014 - Ibrahim",
    15:"015 - Al-Hijr",
    16:"016 - An-Nahl",
    17:"017 - Al-Isra",
    18:"018 - Al-Kahf",
    19:"019 - Maryam",
    20:"020 - Taha",
    21:"021 - Al Anbiya",
    22:"022 - Al-Hajj",
    23:"023 - Al-Mumenoon",
    24:"024 - An-Noor",
    25:"025 - Al-Furqan",
    26:"026 - Ash-Shuara",
    27:"027 - An-Naml",
    28:"028 - Al-Qasas",
    29:"029 - Al-Ankaboot",
    30:"030 - Ar-Room",
    31:"031 - Luqman",
    32:"032 - As-Sajda",
    33:"033 - Al-Ahzab",
    34:"034 - Saba",
    35:"035 - Fatir",
    36:"036 - Ya-seen",
    37:"037 - As-Saaffat",
    38:"038 - Sad",
    39:"039 - Az-Zumar",
    40:"040 - Ghafir",
    41:"041 - Fussilat",
    42:"042 - Ash-Shura",
    43:"043 - Az-Zukhruf",
    44:"044 - Ad-Dukhan",
    45:"045 - Al-Jathiya",
    46:"046 - Al-Ahqaf",
    47:"047 - Muhammad",
    48:"048 - Al-Fath",
    49:"049 - Al-Hujraat",
    50:"050 - Qaf",
    51:"051 - Adh-Dhariyat",
    52:"052 - At-Tur",
    53:"053 - An-Najm",
    54:"054 - Al-Qamar",
    55:"055 - Ar-Rahman",
    56:"056 - Al-Waqi'a",
    57:"057 - Al-Hadid",
    58:"058 - Al-Mujadala",
    59:"059 - Al-Hashr",
    60:"060 - Al-Mumtahana",
    61:"061 - As-Saff",
    62:"062 - Al-Jumu'a",
    63:"063 - Al-Munafiqoon",
    64:"064 - At-Taghabun",
    65:"065 - At-Talaq",
    66:"066 - At-Tahrim",
    67:"067 - Al-Mulk",
    68:"068 - Al-Qalam",
    69:"069 - Al-Haaqqa",
    70:"070 - Al-Maarij",
    71:"071 - Nooh",
    72:"072 - Al-Jinn",
    73:"073 - Al-Muzzammil",
    74:"074 - Al-Muddaththir",
    75:"075 - Al-Qiyama",
    76:"076 - Al-Insan",
    77:"077 - Al-Mursalat",
    78:"078 - An-Naba",
    79:"079 - An-Nazi'at",
    80:"080 - Abasa",
    81:"081 - At-Takwir",
    82:"082 - Al-Infitar",
    83:"083 - Al-Mutaffifin",
    84:"084 - Al-Inshiqaq",
    85:"085 - Al-Burooj",
    86:"086 - At-Tariq",
    87:"087 - Al-A'la",
    88:"088 - Al-Ghashiya",
    89:"089 - Al-Fajr",
    90:"090 - Al-Balad",
    91:"091 - Ash-Shams",
    92:"092 - Al-Layl",
    93:"093 - Ad-Dhuha",
    94:"094 - As-Sharh",
    95:"095 - At-Tin",
    96:"096 - Al-'alaq",
    97:"097 - Al-Qadr",
    98:"098 - Al-Bayyina",
    99:"099 - Az-Zalzala",
    100:"100 - Al-'adiyat",
    101:"101 - Al-Qari'a",
    102:"102 - At-Takathur",
    103:"103 - Al-Asr",
    104:"104 - Al-Humaza",
    105:"105 - Al-Fil",
    106:"106 - Quraish",
    107:"107 - Al-Ma'un",
    108:"108 - Al-Kauther",
    109:"109 - Al-Kafiroon",
    110:"110 - An-Nasr",
    111:"111 - Al-Masadd",
    112:"112 - Al-Ikhlas",
    113:"113 - Al-Falaq",
    114:"114 - An-Nas"
}


base_directory="2" # the  name of the directory that contains the audio files
out_directory=f"{base_directory}_renamed" # the out directory

# if the out directory doesn't exist then create it
if not os.path.exists(out_directory): os.mkdir(out_directory)

# search for multiple file formats
types = (f'{base_directory}/*.MP3',
         f'{base_directory}/*.mp3',
         f'{base_directory}/*.m4a',
         f'{base_directory}/*.wav') # the tuple of file 

# get all files with thses extensions
files_grabbed = []
for files in types:
    # print(len(glob(files)))
    files_grabbed.extend(glob(files))

for file in tqdm(files_grabbed,total=len(files_grabbed)):
    
    base_name= os.path.basename(file) # get only the file name without the full path
    file_name, file_extension = os.path.splitext(base_name) #split the file name and the extension
    file_name=file_name.replace("-"," ").replace("_"," ").strip() #clean the file name from any non alph numeric chacter

    # get all the numbers in the file name even if there are some text in the file name
    number = [int(token) for token in file_name.split() if token.isdigit()]

    print("file_name: ",file_name)

    print("file_extension: ",file_extension)

    print("base_name: ",base_name)

    print("number: ",*number)
    
    # if the number were found and exist in the names dictionary then rename it and put it in the out directory
    if len(number)>0:
        if  number[0] in arabic_names.keys():
            new_name= arabic_names[number[0]]
            
            new_name=f"{out_directory}/{new_name}{file_extension}"
            os.rename(file, new_name)

    print(100*"*")
            









