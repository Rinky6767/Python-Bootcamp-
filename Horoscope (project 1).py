import string
st="Horoscope"
print("\n")
print(st.center(60,'*'))
#printing avilable option.
print("\n\tFollowing are the option you can choose. \n\t1) If you don't know your horoscope \n\t2) Horoscope of 20th september. \n\t3) In depth information of your horoscope. \n\t4) Daily horoscope detail link.")
op_num=int(input("\n\tEnter your option number:: "))
if(op_num==1):
	print("\n\t1) Aries  -  March 21 to April 19 \n\t2) Taurus -  April 20 to May 20 \n\t3) Gemini -  May   21 to June 21\n\t4) Cancer -  June  22 to July 22 ")
	print("\t5) Leo    -  July  23 to August 22 \n\t6) Virgo  - August 23 to September 22 \n\t7) Libra  - September 23 to october 23 \n\t8) Scorpio- October 24 to November 22")
	print("\n\t9) Sagittarius -  November 23  to December 21 \n\t10) Capricorn  -  December 22  to January 19 \n\t11) Aquarius   -  January 20  to February \n\t12) Pisces     -  February 19 to March 20.")
#printing the name of horoscope.
elif(op_num==2):
	print("\tFollowing are the Horoscope\n \t1) Aries \n \t2) Taurus  \n \t3) Gemini  \n \t4) Cancer  \n \t5) Leo  \n \t6) Virgo  \n \t7) Libra  \n \t8) Scorpio  \n \t9) Saggittarius  \n \t10) Capricorn  \n \t11) Aquarius  \n \t12) Pisces")
	ho_num=int(input("\n\tEnter the number of your Horoscope: "))
	if(ho_num==1): #details of horoscope
	   print("\n=>\tToday, you may have mental peace. \n\tYou are likely to be busy with friends and family. \n\tYou may enjoy your domestic life, it may increase       \t understanding with your spouse. \n\tThere is a new partnership in your business. \n\tNew innovations may help your business to grow. \n\tDisputes in the partnerships may be resolved now.")
	elif(ho_num==2):
	   print("\n=>\tToday your good health may make you happy.\n\t Your health-related issues are now resolved.\n\tYou may control your worthless expenditures and new\n\tsources of income may likely be opened, which may \n\tboost your financial health. \n\tSingles may find soul mates in the same community.")
	elif(ho_num==3):
	   print("\n=>\tToday the moon is positive. \n\tYou may have some sort of energy; you may be able to\n\t perform at work efficiently. \n\tYou may also help some needy person, which may \n\t create your prestige among people around you. \n\tYou may spend your time studying intellectual stuff.\n\tYou may also plan for higher study to groom your \n\tcareer.")
	elif(ho_num==4):
	    	print("\n=>\tToday until evening,you may be impatient,\n\thave a lack of confidence,\n\twhich may reflect into your way of working. \n\tParent's health may make you upset.\n\tKid's notorious behaviour may make you upset.\n\tYou should try to focus yourself and try to \n\tavoid scattering your energy into many holes.\n\tInvestments in risky assets are advised to avoid now.")
	elif(ho_num==5):
	   print("\n=>\tToday you may be happy. You are likely to plan\n\t for an overseas work-related journey, which will\n\t increase your business in the near future. \n\tSpending money on luxury stuff may improve your\n\t lifestyle.\n\t But you are advised not to drive yourself\n\ttowards glamour or addictions; it may affect your \n\tfinancial health.")
	elif(ho_num==6):
	     	print("\n=>\tToday, you advised us to control you way of \n\tspeaking,your harsh speaking may affect your family \n\tharmony.\n\tYou may spend your hard-earned money in buying some\n\tworthless\n\tstuff to maintain your social status, it is\n\tadvised to not to keep your money loose\n\t in the pocket.")
	elif(ho_num==7):
	     	print("\n=>\tToday, you may be busy in kid career or\n\textracurricular activities.\n\tYou may take some advice from someone to choose\n\tcareer options.\n\tYou may meet consultants or specialists also.\n\tYou may also hear good news regarding kids' results.\n\tYou may also invest some capital into your family\n\tbusiness.")
	elif(ho_num==8):
	       	print("\n=>\tToday you must control your way of speaking, shall\n\tbe careful in terms of hidden enemies and opponents.\n\tYou may be a victim of a conspiracy. \n\tIt is advised to make investments in risky assets.\n\tYou must avoid lending money to anyone; it may not \n\tbe recoverable easily.\n\t You are advised to do meditation and yoga to \n\tcome out from stress.\n\tLove birds are advised to be involved in \n\tcontroversies.\n\tStudents are advised to work hard.")
	elif(ho_num==9):
	   print("\n=>\tToday, job seekers may get a new job; there\n\tare chances of promotions in their current job.\n\tIn the business, I may get new clients, which will \n\tbe helpful in the growth in terms of profits.\n\tSingles are likely to find their good match.\n\tIn domestic life, you must avoid hiding anything\n\tfrom your spouse; otherwise, it will create\n\t distance in your relationship.")
	elif(ho_num==10):
	       	print("\n=>\tToday is a day of success in terms of profession.\n\tYour plans are now going to give positive results in\n\tterms of profits.\n\tThere may be good news related to your past\n\tinvestments in terms of gains.\n\tYour creativity may help you to improve your\n\tprofessional skills.\n\tJob seekers are likely to get a suitable job.\n\tStudents may have good focus after self-analysis.\n\tYou may be able to understand the feelings of\n\tyour spouse.")
	elif(ho_num==11):
	   print("\n=>\tToday until afternoon, you may be upset.\n\tAfternoon onwards elders blessings may protect you\n\tfrom this messy situation.\n\tYour willpower may help you to complete your\n\tdelayed projects.\n\tIt is advised to avoid arguments in domestic life.\n\tBy the evening, you may have gained in terms of past\n\tinvestments.")
	elif(ho_num==12):
	   print("\n=>\tToday, the moon is not positive, there are chances\n\tthat you may not feel well, you might have health \n\tissues.\n\tYou are advised not to make investments in\n\tnew business projects, otherwise,\n\tyou may face losses.\n\tStudents are advised to avoid the fantasy and should\n\twork hard in their studies.\n\tYou are also avoiding rash driving.")
	else:
	     	print("\n\t=>Sorry,Invailed Number..")
elif(op_num==3): #option 3
	print("\n\tFollowing are the Horoscope\n \t1) Aries \n \t2) Taurus  \n \t3) Gemini  \n \t4) Cancer  \n \t5) Leo  \n \t6) Virgo  \n \t7) Libra  \n \t8) Scorpio  \n \t9) Saggittarius  \n \t10) Capricorn  \n \t11) Aquarius  \n \t12) Pisces")
	det_num=(int(input("\n\tEnter the number of your horoscope::")))
	if(det_num==1):
		print("\n\tA) Date of Birth : March 21 - April 19 \n\n\tB) Strength      : 1)Hopeful \n\t\t\t2)Active\n\t\t\t3)Energetic\n\t\t\t4)Honest \n\t\t\t5)Versatile\n\t\t\t6)Brave\n\t\t\t7)Adventurous")
		print("\n\tC) Weakness     : 1)Impulsive \n\t\t\t2)Naive\n\t\t\t4)Self-willed\n\t\t\t5)Belligerent\n\t\t\t6)Impatien")
		print("\n\tD)Symbol        : Ram\n\tE)Element       : Fire\n\tF)Sign Ruler    : Mars\n\tG)Lucky Color   : Red\n\tH)Lucky Number  : 5\n\tI)Jewelry       : Ruby")
		print("\tJ)Best Match    :1)Leo\n \t\t\t2) Sagittarius\n\t\t\t3)Aries")
	elif(det_num==2):
		print("\n\tA) Date of Birth: April 20 - May 20\n\n\tB)Strength    : 1)Romantic\n\t\t\t2)Decisive\n\t\t\t3)Logical\n\t\t\t4)Diligent\n\t\t\t 5)Ardent\n\t\t\t6)Patient\n\t\t\t7)Talented")
		print("\n\tC)Weakness  : 1)Prejudiced \n\t\t\t2)Dependent\n\t\t\t3)Stubborn\n\tD)Symbol    : Bull\n\tE)Element   : Earth\n\tF)Sign Ruler: Venus\n\tG)Lucky Color  : Pink\n\tH)Lucky Number : 6\n\tI)Jewelry   : Emerald, Jade\n\tJ)Best Match: Capricorn, Virgo and Taurus")
	elif(det_num==3):
		print("\n\tA)Date of Birth: May 21 - June 21\n\n\tB)Strength     : 1)Multifarious\n\t\t\t2)Perspicacious\n\t\t\t3)Smart\n\t\t\t4)Cheerful\n\t\t\t5)Quick-witted\n\t\t\t6)Clement\n\t\t\t7)Charming\n\tC)Weakness    : 1)Fickle\n\t\t\t2)Gossipy\n\t\t\t3)amphibian")
		print("\n\tD)Symbol      : Twins\n\tE)Element     : Air\n\tF)Sign Ruler  : Mercury\n\tG)Lucky Color : Yellow\n\tH)Lucky Number: 7\n\tI)Jewelry     : Opal\n\tJ)Best Match  : Aquarius, Libra and Gemini")
	elif(det_num==4):
		print("\n\tA)Date of Birth: June 22 - July 22\n\n\tB)Strength: 1) Have strong sixth sense\n\t\t\t2)Subjective\n\t\t\t3)Gentle\n\t\t\t4)Swift\n\t\t\t5)Imaginative\n\t\t\t6)Careful\n\t\t\t7)Dedicated.\n\tC)Weakness: 1)Greedy\n\t\t\t2)Possessive\n\t\t\t3)Sensitive\n\t\t\t4)Prim")
		print("\n\tD)Symbol       : Crab\n\tE)Element      : Water\n\tF)Sign Ruler   : Moon\n\tG)Lucky Color  : Green\n\tH)Lucky Number : 2\n\tI)Jewelry      : Pearl\n\tI)Best Match   : Pisces, Scorpio and Cancer")
	elif(det_num==5):
		print("\n\tA)Date of Birth: July 23 - August 22\n\n\tB)Strength: 1)Proud\n\t\t\t2)Charitable\n\t\t\t3)Reflective\n\t\t\t4)Loyal\n\t\t\t5)Enthusiastic\n\tC)Weakness: 1)Arrogant\n\t\t\t2)Vainglorious\n\t\t\t3) Indulgent\n\t\t\t4)Wasteful\n\t\t\t5)Willful\n\t\t\t6)Self-complacent")
		print("\n\tD)Symbol       : Lion\n\tE)Element      : Fire\n\tF)Sign Ruler   : Sun\n\tG)Lucky Colors : Red, Gold, Yellow\n\tH)Lucky Number : 19\n\tI)Jewelry      : Gold\n\tJ)Best Match   : Aries, Sagittarius and Leo")
	elif(det_num==6):
		print("\n\tA)Date of Birth: August 23 - September 22\n\n\tB)Strength: 1)Helping\n\t\t\t2)Elegant\n\t\t\t3)Perfectionist\n\t\t\t4)Modest\n\t\t\t5)Practical\n\t\t\t6)Clearheaded\n\tC)Weakness: 1)Picky\n\t\t\t2)Nosey\n\t\t\t3)Tortuous\n\t\t\t4)Confining")
		print("\n\tD)Symbol       : Virgin maiden\n\tE)Element      : Earth\n\tF)Sign Ruler   : Mercury\n\tG)Lucky Color  : Gray\n\tH)Lucky Number : 7\n\tI)Jewelry      : Sapphire, Amber\n\tJ)Best Match   : Sagittarius, Taurus and Gemini")
	elif(det_num==7):
		print("\n\tA)Date of Birth: September 23 - October 23\n\n\tB)Strength: 1)Idealistic\n\t\t\t2)Equitable\n\t\t\t3)Strong social skills\n\t\t\t4)Aesthetic\n\t\t\t5)Charming\n\t\t\t6)Artistic\n\t\t\t7)Beautiful\n\n\tC)Weakness: 1)Hesitant\n\t\t\t2)Narcissistic\n\t\t\t3)Lazy\n\t\t\t4)Perfunctory\n\t\t\t5)Freewheeling")
		print("\n\tD)Symbol       : Scales\n\tE)Element      : Air\n\tF)Sign Ruler   : Venus\n\tG)Lucky Color  : Brown\n\tH)Lucky Number : 3\n\tI)Jewelry      : Coral, Amber\n\tJ)Best Match   : Aquarius, Gemini and Libra")
	elif(det_num==8):
		print("\n\tA)Date of Birth: October 24 - November 22\n\n\tB)Strength: 1)Mysterious\n\t\t\t2)Rational\n\t\t\t3)Intelligent\n\t\t\t4)Independent\n\t\t\t5)Intuitive\n\t\t\t6)Dedicated\n\t\t\t7)Insightful\n\tC)Weakness: 1)Suspicious\n\t\t\t2)Fanatical\n\t\t\t3)Complicated\n\t\t\t4)Possessive\n\t\t\t5)Arrogant\n\t\t\t6)Self-willed\n\t\t\tExtreme")
		print("\n\tD)Symbol        : Scorpion\n\tE)Element       : Water\n\tF)Sign Ruler    : Pluto, Mars\n\tG)Lucky Colors  : Purple, Black\n\tH)Lucky Number  : 4\n\tI)Jewelry       : Jasper, Black Crystal\n\tJ)Best Match    : Cancer, Capricorn and Pisces")
	elif(det_num==9):
		print("\n\tA)Date of Birth: November 23 - December 21\n\n\tB)Strength: 1)Insightful\n\t\t\t2)Superior\n\t\t\t3)Rational\n\t\t\t4)Brave\n\t\t\t5)Beautiful\n\t\t\t6)Lively\n\t\t\t7)Optimistic\n\n\tC)Weakness:1)Forgetful\n\t\t\t2)careless\n\t\t\t3)rash")
		print("\n\tD)Symbol       : Archer\n\tE)Element      : Fire\n\tF)Sign Ruler   : Jupiter\n\tG)Lucky Color  : Light Blue\n\tH)Lucky Number : 6\n\tI)Jewelry      : Amethyst\n\tJ)Best Match   : Virgo, Leo and Aries")
	elif(det_num==10):
		print("\n\tA)Date of Birth: December 22 - January 19\n\n\tB)Strength:1)Excellent\n\t\t\t2) Intelligent\n\t\t\t3)Practical\n\t\t\t4)Reliable\n\t\t\t5)Perseverant\n\t\t\t6)Generous7)Persistent\n\n\tC)Weakness:1)Stubborn\n\t\t\t2)Lonely\n\t\t\t3)Suspicious")
		print("\n\tD)Symbol       : Goat\n\tE)Element      : Earth\n\tF)Sign Ruler   : Saturn\n\tG)Lucky Colors : Brown, Black, Dark Green\n\tH)Lucky Number : 4\n\tI)Jewelry      : Black Jade\n\tJ)Best Match   : Virgo, Taurus and Pisces")
	elif(det_num==11):
		print("\n\tA)Date of Birth: January 20 - February 18\n\n\tB)Strength: 1)Original\n\t\t\t2)Tolerant\n\t\t\t3)Ideal\n\t\t\t4)Calm\n\t\t\t5)Friendly\n\t\t\t6)Charitable\n\t\t\t7)Independent\n\t\t\t8)Smart\n\t\t\t9)Practical\n\n\tC)Weakness: 1)Changeful\n\t\t\t2)Disobedient\n\t\t\t3)Liberalistic\n\t\t\t4)Hasty\n\t\t\t5)Rebel")
		print("\n\tD)Symbol      : Water carrier\n\tE)Element     : Air\n\tF)Sign Ruler  : Uranus\n\tG)Lucky Color : Bronze\n\tH)Lucky Number: 22\n\tI)Jewelry     : Black Pearl\n\tJ)Best Match  : Gemini, Libra and Aquarius")
	elif(det_num==12):
		print("\n\tA)Date of Birth: February 19 - March 20\n\n\tB)Strength: 1)Conscious\n\t\t\t2)Aesthetic\n\t\t\t3)Platonic\n\t\t\t4)Dedicated\n\t\t\t5)Kind\n\t\t\t6)With good temper\n\n\tC)Weakness: 1)Recessive\n\t\t\t2)Sentimental\n\t\t\t3)Indecisive\n\t\t\t4)Unrealistic")
		print("\n\tD)Symbol       : Fish\n\tE)Element      : Water\n\tF)Sign Ruler   : Neptune\n\tG)Lucky Color  : White\n\tH)Lucky Number : 11\n\tI)Jewelry      : Ivory Stone\n\tJ)Best Match   : Scorpio, Cancer and Capricorn")
	else:
		print("\n\tInvalid Number")
elif(op_num==4):
		print("\n\t=> Below is the link Where you can check your daily \n\thoroscope.")
		print("\n\t=> Note this link is not provided with any intention\n\t of advertisment")
#link for checking horoscope 
		print("\n\t==> https://m.timesofindia.com/astrology/horoscope/horoscope-today-21-september-2020-check-astrological-prediction-for-aries-taurus-gemini-cancer-and-other-signs/amp_articleshow/78213974.cms")
else:
		print("\n\tSorry, It's aInvalid Number..")
		
	
	