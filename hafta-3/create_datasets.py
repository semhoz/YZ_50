import os

english_names_sample = """
emma olivia ava isabella sophia charlotte mia amelia harper evelyn
abigail emily elizabeth mila ella avery sofia camila aria scarlett
victoria madison luna grace chloe penelope layla riley zoey nora
lily eleanor hannah lillian addison aubrey ellie stella natalie zoe
leah hazel violet aurora brooklyn bella claire skylar lucy paisley
everly anna caroline nova genesis emilia kennedy samantha maya willow
kinsley naomi aaliyah elena sarah ariana allison gabriella alice madelyn
cora ruby eva serenity autumn adeline hailey gianna valentina isla
eliana quinn nevaeh ivy sadie piper lydia alexa josephine emery
julia delilah arianna vivian kaylee sophie brielle madeline peyton rylee
clara hadley melanie mackenzie reagan adalynn liliana aubree jade katherine
isabelle natalia raelynn maria athena ximena arya leilani taylor faith
rose kylie alexandra mary margaret lyla ashley amaya eliza brianna
bailey andrea khloe jasmine melody iris isabel norah annabelle valeria
emerson adalyn ryleigh eden emersyn anastasia kayla alyssa juliana charlie
esther ariel cecilia valerie alina molly reese aliyah lilly parker
finley morgan sydney jordyn eloise trinity daisy kimberly lauren genevieve
sara arabella harmony elise remi teagan alexis london sloane laila
lucia diana juliette sienna elliana londyn ayla callie gracie josie
amara jocelyn daniela everleigh mya rachel summer alana brooke alaina
mckenzie catherine amy presley journee rosalie ember brynlee rowan joanna
paige rebecca ana sawyer mariah nicole brooklynn payton marley fiona
georgia lila harley adelyn alivia noelle gemma vanessa journey makayla
angelina adaline catalina alayna julianna leila lola adriana june juliet
jayla river tessa lia dakota delaney selena blakely ada camille
zara malia hope samara vera mckenna briella izabella hayden raegan
michelle angela ruth freya kamila vivienne aspen olive kendall elaina
thea kali destiny amiyah evangeline cali blake elsie juniper alexandria
myla ariella kate mariana lilah charlee daleyza nyla jane maggie
zuri aniyah lucille leia melissa adelaide amina giselle lena camilla
miriam millie brynn gabrielle sage annie logan lilliana haven jessica
kaia magnolia amira adelynn makenzie stephanie nina phoebe arielle evie
lyric alessandra gabriela paislee raelyn madilyn paris makenna kinley gracelyn
talia maeve rylie kiara evelynn brinley jacqueline laura gracelynn lexi
ariah fatima jennifer kehlani alani ariyah luciana allie heidi maci
phoenix felicity joy kenzie veronica margot addilyn lana cassidy remington
saylor ryan keira harlow miranda angel amanda daniella royalty gwendolyn
ophelia heaven jordan madeleine esmeralda kira miracle elle amari danielle
daphne willa haley gia kaitlyn oakley kailani winter alicia serena
nadia aviana demi jada braelynn dylan ainsley alison camryn avianna
bianca skyler scarlet maddison nylah sarai regina dahlia nayeli raven
helen adrianna averie skye kelsey tatum kensley maliyah erin viviana
jenna anaya carolina shelby sabrina mikayla annalise octavia lennon blair
carmen yaretzi kennedi mabel zariah kyla christina selah celeste eve
mckinley milani frances jimena kylee leighton katie aitana kayleigh sierra
kathryn rosemary jolene alondra elisa helena charleigh hallie lainey avah
jazlyn kamryn mira cheyenne francesca antonella wren chelsea amber emory
lorelei nia abby april emelia carter aylin cataleya bethany marlee
carly kaylani emely liana madelynn cadence matilda sylvia myra fernanda
oaklyn elianna hattie dayana kendra maisie malaysia kara katelyn maia
celine cameron renata jayleen charli emmalyn holly azalea leona alejandra
bristol collins imani meadow alexia edith kaydence leslie lilith kora
aisha meredith danna wynter emberly julieta michaela alayah jemma reign
colette kaliyah elliott johanna remy sutton emmy virginia briana oaklynn
adelina everlee megan angelica justice mariam khaleesi macie karsyn alanna
aleah mae mallory esme skyla madilynn charley allyson hanna shiloh
henley macy maryam ivanna ashlynn lorelai amora ashlyn sasha baylee
beatrice itzel priscilla marie jayda liberty rory alessia alaia janelle
kalani gloria sloan dorothy greta julie zahra savanna annabella poppy
amalia zaylee cecelia coraline kimber emmie anne karina kassidy kynlee
monroe anahi jaliyah jazmin maren monica siena marilyn reyna kyra
lilian jamie melany alaya ariya kelly rosie adley dream jaylah
laurel jazmine mina karla bailee aubrie katalina melina harlee elliot
hayley elaine karen dallas irene lylah ivory chaya rosa aleena
braelyn nola alma leyla pearl addyson roselyn lacey lennox reina
aurelia noa janiyah jessie madisyn saige alia tiana astrid cassandra
kyleigh romina stevie haylee zelda lillie aileen brylee eileen yara
ensley lauryn giuliana livia anya mikaela palmer lyra mara marina
kailey liv clementine kenna briar emerie galilea tiffany bonnie elyse
cynthia frida kinslee tatiana joelle armani jolie nalani rayna yareli
meghan rebekah addilynn faye zariyah lea aliza julissa lilyana anika
kairi aniya noemi angie crystal bridget ari davina amelie amirah
annika elora xiomara linda hana laney mercy hadassah madalyn louisa
simone kori jillian alena malaya miley milan sariyah malani clarissa
nala princess amani analia estella milana aya chana jayde tenley
zaria itzayana penny ailani lara aubriella clare lina rhea bria
thalia keyla haisley ryann addisyn amaia chanel ellen harmoni aliana
tinsley landry paisleigh lexie myah rylan deborah emilee laylah novalee
ellis emmeline avalynn hadlee legacy braylee elisabeth kaylie ansley dior
liam noah william james oliver benjamin elijah lucas mason logan
alexander ethan jacob michael daniel henry jackson sebastian aiden matthew
samuel david joseph carter owen wyatt john jack luke jayden
dylan grayson levi isaac gabriel julian mateo anthony jaxon lincoln
joshua christopher andrew theodore caleb ryan asher nathan thomas leo
isaiah charles josiah hudson christian hunter ezra aaron landon adrian
jonathan nolan jeremiah easton elias colton cameron carson robert angel
maverick nicholas dominic jaxson greyson adam ian austin santiago jordan
cooper brayden roman evan ezekiel xavier jose jace jameson leonardo
bryson axel everett jaden kayden kai bryan bentley jasper gael
christopher brody sawyer arthur ryan silicone brandon michelle nathaniel
""".split()

turkish_names_sample = """
ahmet mehmet ali veli huseyin hasan mustafa ibrahim omer osman
yusuf fatih murat hakan serkan emre burak baris kerem koray
can cem kaan doruk efe arda batuhan bugra oguzhan taylan
gokhan engin volkan tolga erdem berk berkay kaan ufuk umut
onur deniz umut guney ruzgar batu yigit ege emir arda
ayse fatma emine zeynep hatice elif merve busra esra kubra
sevgi sitem selin simge pinar deniz derya damla ozlem asli
burcu ceren ezgi gamze hande irem gizem hazal melis neslihan
rabia seda sibel tugba yagmur yaprak yasemin zehra banu funda
berfin pelin nihal nazli nisa tugce bilge ceren bengu duygu
aylin aslihan aysenur beyza binnur canan beste cigdem dilek ebru
ecem eda elvin eylem fulya gonca gulizar ikbal ilknur ipek
jale kader kardelen leyla meltem nazan nesrin nuray nurcan oya
pelin reyhan saadet saadet sevil sevin siber simel sueda suheda
tuba tule tulip ulku vildan yaren yonca zumra ayberk bilgehan
cagri caglar devrim ertugrul feyyaz goktug ilker kursat metehan oguz
onur alp alperen batu batuhan cagatan cihan demir dogan efe
egemen emre emirhan ensar enes eray eren furkan haktan kaan
koray kutay merter metin mikail mirac mukremin nesim oguz oguzhan
oktay polat poyraz ruzgar samet sarper selim semih serhat sertac
sinan tarık tarkan turgut ufuk ulas umut utku yagiz yasin
yigit yigitcan zafer ziya abdullah abdurrahman adem adnan ahmet aydın
arif aziz baha bahadır baki bayram besir bulent bunyamin cafer
celal cemal cevdet cihat cuneyt davut dogan ekrem emin emrah
enver ercan erdal erkan erol eyup faruk fikret galip harun
hidayet hikmet ilhan ismail izzet kadir kamil kazim kenan levent
mahmut mahsum mazhar melih memduh mengu mesut mithat muammer muhsin
murat musa mucahit muzaffer naim necdet necati nihat niyazi nurullah
orhan osman rami ramazan recai recep remzi ridvan rifat riza
sabit sadik salih samet sami sedat selahattin selim selman sefa
suat suleyman tahir taner tarek tayfun tamer tarik tayyar tefik
temel tevfik timur tulga tung turgay turgut ufuk ulu ulas
ulus umut umit unal vedat veysel volkan yasin yasar yavuz
yunus yusuf zafer zekeriya zeki ziya abide adalet adile afra
ahu ayla aysel aysen aysun azra bahar begum belgin beliz
beril berna besra beste betul beyza bilgen binnur birgul birsen
buket burcu canan cans u ceyda ceylan damla defne deniz derya
didem dilek dilara dilber dudu ebru ecem eda ece elvin emel
enise erem erika esma esra eylem fato fato fatmanur feride
figen filiz fulya funda gamze gizem gonca gozde gul gulcan
guldane gulen guler gulhayat gulin gulsen gulsah gulseren gulsum
gulten gunay gunes hande harika hazal hicran hilal hulya ikbal
ilkay ilknur ipek ilter iren imge inci ipek ipek ipek
jale kader kibriya kubra lale leyla melek melike melis melisa
meltem menta merve meryem mine muazzez mug e muzeyyen nalan naz
nazan nazli nebahat nesrin nevin nihan nil nilgun nilufer nisa
nimet nur nuran nuray nurcan nurten oya ozlem ozge ozlem
pelin pinar rabia raife rana rezzan rukiye saadet sabriye sadiye
safiye sahika salime samira sanem saniye sara saray secil seda
sedef sedef seval sevgi sevil sevilay sevin sevinin seym a sezen
sibel simge sinem sitem songul sueda suheda sultan suzan sukran
sukriye tanyeli tara tuba tulay tulin turkan ufuk ulku umran
vildan yagmur yaren yasemin yelda yeliz yildiz yonca yuksel zahide
zehra zeynep ziba ziynet zumrut afra ahsen alara aleyna almila
alara asya azra beren berra bulem cefri cefri ceylin defne
derin dora ebrar ece ecrin ela elisa elvin hira idil
ira lara lina liva mila mina mira nisa okyanus pera
roza sare selene seray sima vera yaren yara zumra
""".split()

# clean english names
english_names = sorted(list(set([w.strip().lower() for w in english_names_sample if w.strip().lower().isalpha()])))
with open('/Users/semihoz/Desktop/week3/names.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(english_names) + '\n')

# clean turkish names
tr_chars = set('abcçdefgğhıijklmnoöprsştuüvyz')
turkish_names = sorted(list(set([w.strip().lower() for w in turkish_names_sample if all(c in tr_chars for c in w.strip().lower())])))
with open('/Users/semihoz/Desktop/week3/names_tr.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(turkish_names) + '\n')

print(f"Dataset created: {len(english_names)} English names, {len(turkish_names)} Turkish names.")
