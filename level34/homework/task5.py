#5) შექმენით ფუნქცია რომელიც იღებს რიცხვებს, ზოგი იქნება
#  სტრინგი ზოგი იქნება ინტეჯერი (მაგ: [10, "10"]) და გამოიტანეთ
#  მათი ჯამი. (exception'ებს გაუმკლავდით try/except'ის გარეშე. hint: გამარტივებისთვის გამოიყენეთ list comprehension

def sun(listn):
    j=0
    for i in listn:
        j=int(i)+j
    return j

print(sun(["10",5,"21",6,1]))