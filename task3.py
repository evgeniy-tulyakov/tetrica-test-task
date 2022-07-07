def appearance(intervals):
    elapsed_time = 0
    for i in range(0, len(intervals['pupil']), 2):
        if intervals['pupil'][i + 1] <= intervals['lesson'][0]:
            continue
        if intervals['pupil'][i] >= intervals['lesson'][1]:
            continue

        if intervals['pupil'][i] <= intervals['lesson'][0] <= intervals['pupil'][i + 1]:
            intervals['pupil'][i] = intervals['lesson'][0]
        if intervals['pupil'][i] <= intervals['lesson'][1] <= intervals['pupil'][i + 1]:
            intervals['pupil'][i + 1] = intervals['lesson'][1]

        for k in range(0, len(intervals['tutor']), 2):
            if intervals['tutor'][k + 1] <= intervals['lesson'][0]:
                continue
            if intervals['tutor'][k] >= intervals['lesson'][1]:
                continue

            if intervals['tutor'][k] <= intervals['lesson'][0] <= intervals['tutor'][k + 1]:
                intervals['tutor'][k] = intervals['lesson'][0]
            if intervals['tutor'][k] <= intervals['lesson'][1] <= intervals['tutor'][k + 1]:
                intervals['tutor'][k + 1] = intervals['lesson'][1]

            if intervals['lesson'][0] <= intervals['pupil'][i] <= intervals['lesson'][1]:
                pupil_start = intervals['pupil'][i]
                if intervals['lesson'][0] <= intervals['tutor'][k] <= intervals['lesson'][1]:
                    tutor_start = intervals['tutor'][k]
                    if tutor_start <= pupil_start <= intervals['tutor'][k + 1]:
                        appear_start = pupil_start
                    elif pupil_start <= tutor_start <= intervals['pupil'][i + 1]:
                        appear_start = tutor_start
                    else:
                        continue

                    if tutor_start <= intervals['pupil'][i + 1] <= intervals['tutor'][k + 1]:
                        appear_end = intervals['pupil'][i + 1]
                    elif pupil_start <= intervals['tutor'][k + 1] <= intervals['pupil'][i + 1]:
                        appear_end = intervals['tutor'][k + 1]
                    if appear_end != appear_start:
                        elapsed_time += appear_end - appear_start

    return elapsed_time


tests = [
    {'data': {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473],
    },
    'answer': 3117,},
]

if __name__ == '__main__':
    test_answer = appearance(tests[0]['data'])
    assert test_answer == tests[0]['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
