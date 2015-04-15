operators = {'plus':'+', 'minus':'-', 'multiplied':'*', 'divided':'/'}

def calculate(question):
    question_words = question.split(' ')
    if question_words[:2] == ['What', 'is']:
        question_words = question_words[2:]
        num1 = question_words.pop(0)
        op = question_words.pop(0)
        num2 = question_words.pop(0)
        if num2 == 'by':
            num2 = question_words.pop(0)
        if num2[-1] == '?':
            num2 = num2[:-1]
        try:
            int(num1)
            int(num2)
        except:
            raise ValueError('Invalid number')
        try:
            expression = num1 + operators[op] + num2
        except:
            raise ValueError('Invalid operator')
        val = eval(expression)
        if question_words:
            return calculate('What is ' + str(val) + ' ' + ' '.join(question_words))
        else:
            return val
    else:
        raise ValueError('Invalid question')
