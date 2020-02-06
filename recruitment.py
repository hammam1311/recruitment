def main():
	#write your code here
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	name = input("What is your name ? ")
	age = input ("how old are you ? ")
	exp = input("How many years of experience do you have?")
	cv['skills'] = []
	y=1
	for x in skills :

		print( str(y) +" "+ x )
		y+=1

	s1 = input("What skill do you have from the list above ? ")
	s2 = input("What other skill do you have from the list above ? ")
	s11=int(s1)-1
	s22=int(s2)-1

	cv['skills'].append(skills[s11])
	cv['skills'].append(skills[s22])

	if int(age) >=25 and int(age) <= 40 :
		if exp >= 5 :
			if int(s1) == 6 or int(s2) == 6 :
				print ("you have been accepted")
			else:
				print("you have been rejected")
		else:
			print("you have been rejected")
	else:
		print("you have been rejected")



if __name__ == '__main__':
	main()
