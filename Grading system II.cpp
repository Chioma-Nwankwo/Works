#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Student {

    private:
    int student_ID;
    string name;
    public:
    void getStudentDetails() {
        cout << "Enter the student's name: ";
        cin >> ws;  // To ignore leading whitespace
        getline(cin, name);
        cout << "Enter the student's ID number: ";
        cin >> student_ID;
    }

    string getName() const {
        return name;
    }
};

class Course {

    private:
    string courseName;
    string courseCode;
    double score;
    double creditscore;
    
    public:
    Course(string cn, string cc, double sc, double cs) : courseName(cn), courseCode(cc), score(sc), creditscore(cs) {}

    string getCourseName() const { return courseName; }
    string getCourseCode() const { return courseCode; }
    double getScore() const { return score; }
    double getCreditscore() const{ return creditscore;}
};

// Function to get course details from user
void inputCourses(vector<Course>& courses) {
    int numCourses;
    cout << "Enter number of courses: ";
    cin >> numCourses;

    for (int i = 0; i < numCourses; ++i) {
        string courseName;
        string courseCode;
        double score;
        double creditscore;

        cout << "Enter course name: \n";
        cin >> ws;  // To ignore leading whitespace
        getline(cin, courseName);

        cout << "Enter course code: ";
        cin >> ws;  // To ignore leading whitespace
        getline(cin, courseCode);

        cout << "Enter score for " << courseName << ": ";
        cin >> score;
        
        cout <<"Enter the number of credits for "<<courseName <<": ";
        cin >> creditscore;

        courses.emplace_back(courseName, courseCode, score, creditscore);
    }
}

class Grades {

    private:
    vector<Course> courses;
    public:
    Grades(const vector<Course>& c) : courses(c) {}

    double calculateFinalGrade() const {
        double sum = 0;
        for (const auto& course : courses) {
            sum += course.getScore();
        }
        return courses.empty() ? 0 : sum / courses.size();
    }
    
    double calculateCGPA() const {
    	double sum = 0;
    	double total = 0;
    	for (const auto& course : courses) {
    		sum += course.getScore();
    		total += course.getCreditscore();
		}
		return courses.empty() ? 0 : sum / total;
	}
	

    void displayGrades(const Student& student) const {
        cout << "Grades for " << student.getName() << ":\n";
        for (const auto& course : courses) {
            cout << "  " << course.getCourseName() << ": " << course.getScore() << "\n";
        }
        cout << "Final Grade: " << calculateFinalGrade() << "\n";
    }
    
    void displayCGPA(const Student& student) const {
    	cout << "CGPA for " << student.getName() << ":\n";
        for (const auto& course : courses) {
            cout << "  " << course.getCourseName() << ": " << course.getScore() << "\n";
        }
        cout << "Final Grade: " << calculateFinalGrade() << "\n";
        cout << "Final CGPA: " << calculateCGPA() <<"\n";
		
    	int option;
        cout << "Enter the option you want:"<<endl;
        cout <<"1. First class"<<endl;
        cout <<"2. Second class upper"<<endl;
        cout <<"3. Second class lower"<<endl;
        cout <<"4. Third class"<<endl;
        cin >> option;
        switch (option)
        {
        	case 1:
        		if(calculateCGPA()>=4.5 && calculateCGPA()<5.0){
        			cout << "First Class";
				}
				break;
			case 2:
				if(calculateCGPA()>=3.5 && calculateCGPA()<4.5){
        			cout << "Second Class Upper";
				}
				break;
			case 3:
				if(calculateCGPA()>=2.0 && calculateCGPA()<3.5){
        			cout << "Second Class Lower";
				}
				break;
			case 4: 
			    if(calculateCGPA()>=1.0 && calculateCGPA()<2.0){
        			cout << "Third Class";
				}
				break;
			case 5:
				if(calculateCGPA()<1.0){
        			cout << "Fail, Repeat Class";
				}
				break;
			default:
				cout << "No record was found";
				break;
			 	
		}
	}        
};

int main() {
    Student student;
    student.getStudentDetails();

    vector<Course> courses;
    inputCourses(courses);

    Grades grades(courses);
    grades.displayGrades(student);
    grades.displayCGPA(student);

    return 0;
}
