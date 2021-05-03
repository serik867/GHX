import unittest


    
def convert_numeric(text):
    numbers={
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5': 'five',
        '6': 'six',
        '7':'seven',
        '8':'eight',
        '9': 'nine',
        '10':'ten',
        '11':'eleven',
        '12': 'twelve',
        '13':'thirteen',
        '14':'fourteen',
        '15':'fifteen',
        '16':'sixteen',
        '17':'seventeen',
        '18':'eighteen',
        '19':'nineteen',
        '20':'twenty',
        '30':'thirty',
        '40':'fourty',
        '50':'fifty',
        '60': 'sixty',
        '70':'seventy',
        '80':'eighty',
        '90':'ninety'}

    int_number = int(text)

    if text in numbers.keys():
        return numbers.get(text)
    else:
        num_1=(int_number//10)*10
        num_2=int_number%10
        return '{} {}'.format(numbers.get(str(num_1)),numbers.get(str(num_2)))
    
    return None
    

def find_numeric(text):
    words = text.split()

    for i in range(len(words)):
        if words[i].isdigit():
            words[i]=convert_numeric(words[i])

    return ' '.join(words).capitalize()


class ConverTest(unittest.TestCase):

    def test_1(self):
        text='The 2 little men bought 3 fish.'
        result = find_numeric(text)
        expected = 'The two little men bought three fish.'
        self.assertEqual(result, expected)

    def test_2(self):
        text='2 little men bought 31 fish.'
        result = find_numeric(text)
        expected = 'Two little men bought thirty one fish.'
        self.assertEqual(result, expected)
    
    def test_3(self):
        text='The 32 little men bought 93 fish.'
        result = find_numeric(text)
        expected = 'The thirty two little men bought ninety three fish.'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()





