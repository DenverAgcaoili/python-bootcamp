student_scores = [98, 75, 100, 86, 100, 3]

# TODO: Print the average score
score_sum = sum(student_scores)
score_len = len(student_scores)

average_score = score_sum/score_len
print(f"Average score is: {average_score}")

# TODO: Print the rankings, highest to lowest
print(sorted(student_scores,reverse=True))
