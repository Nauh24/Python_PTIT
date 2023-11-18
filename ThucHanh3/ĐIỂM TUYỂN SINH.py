def standardize_name(s):
    words = s.split()
    return ' '.join(words)

class Candidate:
    def __init__(self, index, full_name, exam_score, ethnicity, region):
        self.candidate_id = 'TS%02d' % index
        self.full_name = standardize_name(full_name).title()
        self.exam_score = exam_score
        self.ethnicity = ethnicity
        self.region = region

    def bonus_points(self):
        total = 0
        if self.region == '1':
            total += 1.5
        elif self.region == '2':
            total += 1
        if self.ethnicity != 'Kinh':
            total += 1.5
        return total

    def total_score(self):
        return self.exam_score + self.bonus_points()

    def result_status(self):
        if self.total_score() >= 20.5:
            return 'Pass'
        return 'Fail'

    def __str__(self):
        return f"{self.candidate_id} {self.full_name} {'%.1f' % self.total_score()} {self.result_status()}"

if __name__ == '__main__':
    candidates = []
    num_candidates = int(input())
    for i in range(1, num_candidates + 1):
        candidates.append(Candidate(i, input(), float(input()), input(), input()))
    candidates.sort(key=lambda x: (-x.total_score(), x.candidate_id))
    for candidate in candidates:
        print(candidate)
