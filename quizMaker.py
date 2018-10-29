import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz_num in range(35):
    # Create the quiz
    quiz_file = open("capital_quiz_%s.txt" % (quiz_num + 1), 'w')

    # Create the answer sheet
    answer_file = open("capital_quiz_answers_%s.txt" % (quiz_num + 1), 'w')

    # Write the header
    quiz_file.write("Capital Quiz #%s\nName: \nPeriod \nDate\n\n" % (quiz_num + 1))

    # List of states and shuffle
    states = capitals.keys()
    random.shuffle(states)

    for question_num in range(50):
        #Gets shuffled state in list order and finds that states capital in capitals dictionary
        correct_answer = capitals[states[question_num]]

        #Deletes the only right answer
        wrong_answers = capitals.values()
        del wrong_answers[wrong_answers.index(correct_answer)]

        #Answer needed to be separated to be easier for us to find in list
        answer_options = wrong_answers + [correct_answer]

        random.shuffle(answer_options)

        #Write the questions
        quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
        for  i in range(4):
            quiz_file.write("%s. %s\n" % ('ABCD'[i], answer_options[i]))
        quiz_file.write("\n")

        # answer_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

        quiz_file.close()
        answer_file.close()

