# Python Program for School Administration system

import csv

# Defining function to use csv file
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_No", "Email_ID"])
        writer.writerow(info_list)
        

# main() program
if __name__=='__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter the details of the student #{} (Name Age Contact_No Email_ID): ".format(student_num))
        
        # splitting the function
        student_info_list = student_info.split(" ")
        
        print("\nThe Entered details are: \nName: {}\nAge: {}\nContact_No: {}\nEmail_ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is the entered values correct? (yes/no): ")
        
        if choice_check=='yes':
            write_into_csv(student_info_list)
            condition_check = input("Do you want to continue? Enter (yes/no): ")
            
            if condition_check=="yes":
                condition = True
                student_num = student_num + 1
            elif condition_check=="no":
                condition = False
        elif choice_check=='no':
            print("Please re-enter the values!")