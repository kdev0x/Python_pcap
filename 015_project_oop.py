class MyString:
    def __init__(self, string):
        self.value = string 
    
    def count_characters(self):
        return len(self.value)

    def count_x_character(self, charcter):
        return self.value.count(charcter)

    def get_first_character(self):
        return self.value[0]

    def get_last_character(self):
        return self.value[-1]

    def get_with_format(self, start, end):
        return start + self.value + end
        
    def print_characters(self):
        for char in self.value:
            print(char)

    def has_character(self, letter):
        return letter in self.value
    
    def is_alpha(self , char):
              if self.value[char].isalpha():
                return True
              else:
                return False
               

    def is_digit(self, index):
        return self.value[index] in "0123456789"

    def is_space(self, user_input):
        if  ' ' in self.value[user_input] == True:
            return True
        else:
            return False

   
x = MyString('We9lcome to Python')
print(x.count_characters())
print(x.count_x_character("e"))
print(x.get_first_character())
print(x.get_last_character())
print(x.get_with_format("<p>", "</p>"))
x.print_characters()
print(x.has_character("W"))
print(x.has_character("z"))
print(x.is_digit(2))
print(x.is_digit(9))
print(x.is_space(2))
print(x.is_space(8))
print(x.is_alpha(2))


# print(x.is_alpha(2))
# print(x.is_alpha(4))
# print(x.is_digit(2))
# MyString attributes(data):
  # value(string)

# MyString services(actions):
    # 01. count_characters
    # 02. count_x_character
    # 03. get_first_character
    # 04. get_last_character
    # 05. get_with_format
    # 06. print_characters
    # 07. has_character
    # 08. is_alpha 
    # 09. is_digit 
    # 10. is_space 
    # 11. has_space
    # 12. has_punctuation (Homework) J

