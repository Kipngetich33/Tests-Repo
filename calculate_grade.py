while True:
    def get_limit(limit,mark):
        limits = {'assigment':50,'test':40,'tut_exercises':20,'final_exam':100}
        requested_limit= limits[limit]
        non_limit = True
        while non_limit:
            if mark >= 0 and mark <= requested_limit:
                non_limit = False
            else:
                print("The input should be between 0 and "+str(requested_limit))
                mark = int(input(": "))
        return mark

    def check_integer(category):
        string_input = True
        while string_input:
            mark = input(": ")
            if mark.isdigit():
                string_input = False
            else:
                print("The input should be an integer")
        return get_limit(category,int(mark))

    def get_marks(category):
        category = category
        print("Enter "+category+" marks")
        mark = check_integer(category)
        return mark

    def get_final_marks(category,mark):
        limits = {'assigment':50,'test':40,'tut_exercises':20,'final_exam':100}
        propotions = {'assigment':20,'test':20,'tut_exercises':10,'final_exam':50}
        requested_limit = limits[category]
        requested_propotion = propotions[category]
        final_mark = int(mark)/int(requested_limit) * int(requested_propotion)
        return final_mark

    def determine_grade(final_mark):
        if final_mark <49:
            return 'Fail'
        elif final_mark >= 50 and final_mark <= 64:
            return 'Pass'
        elif final_mark >= 65 and final_mark <= 74:
            return 'Credit'
        elif final_mark >= 75 and final_mark <= 84:
            return 'Distinction'
        else:
            return 'High Distinction'



    def main():
        assigment_mark = get_marks('assigment')
        test_mark = get_marks('test')
        tut_excercise_mark = get_marks('tut_exercises')
        final_exam_mark = get_marks('final_exam')

        assigment_final_mark = get_final_marks('assigment',assigment_mark)
        test_final_mark = get_final_marks('test',test_mark)
        tut_final_mark = get_final_marks('tut_exercises',tut_excercise_mark)
        final_exam_final_mark = get_final_marks('final_exam',final_exam_mark)

        print("    ")
        print("Student Grade Calculation:")
        print("    ")
        print("................ Raw Mark ...........Final")
        print("Assingemt (50)......."+str(assigment_mark)+"..............."+str(assigment_final_mark)+" /20")
        print("Test (40)............"+str(test_mark)+".............."+str(test_final_mark)+" /20")
        print("Tut Excercise (20)..."+str(tut_excercise_mark)+"..............."+str(tut_final_mark)+" /10")
        print("Final Exam (100)......"+str(final_exam_mark)+"................"+str(final_exam_final_mark)+" /50")
        final_total = assigment_final_mark+test_final_mark+tut_final_mark+final_exam_final_mark
        print("    ")
        print("Total Mark: "+str(final_total))
        print("Grade: "+str(determine_grade(final_total)))
        print("    ")
        print("**********************************************************************")
        print("Calculate New Student's Marks")
        print("    ")




    if __name__ == '__main__':
        main()
    