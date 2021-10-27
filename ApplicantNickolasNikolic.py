class ApplicantNickolasNikolic:
    def __init__(self):
        pass

    def above_below(self, input_list=[0], comparator=0):
        output = {
            "above": 0,
            "below": 0
        }

        for input in input_list:
            if input < comparator:
                output['above'] += 1
            elif input > comparator:
                output['below'] += 1
        
        return output

    def string_rotation(self, input_string="", slide=0):
        if slide <= 0:
            return input_string
        
        offset = input_string[-slide:]
        return offset + input_string[0:-slide]

test = ApplicantNickolasNikolic()
print(test.above_below([1,2,3,4,5,6], 3))
print(test.string_rotation("MyString", 2))

