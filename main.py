from Input_module import get_score
from logic_module import calculate_grade
from output_module import display_result

def main():
    score = get_score()
    grade = calculate_grade(score)
    display_result(score, grade)

main()