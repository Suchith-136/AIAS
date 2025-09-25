## Before vs After Summary Report

### Social Media

- **rows (before → after)**: 20 → 2
- **cols (before → after)**: 6 → 8
- **nulls_total (before → after)**: 8 → 0
- **numeric cols (before → after)**: 3 → 5
- **object cols (before → after)**: 3 → 3

Numeric column stats (before/after/delta):

| column | mean_before | mean_after | mean_delta | std_before | std_after | std_delta | min_before | min_after | min_delta | max_before | max_after | max_delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| likes | 18.333 | 20.0 | 1.667 | 23.579 | 0.0 | -23.579 | 5.0 | 20.0 | 15.0 | 100.0 | 20.0 | -80.0 |
| post_id | 10.5 | 1.5 | -9.0 | 5.916 | 0.707 | -5.209 | 1.0 | 1.0 | 0.0 | 20.0 | 2.0 | -18.0 |
| shares | 3.118 | 2.0 | -1.118 | 1.799 | 1.414 | -0.385 | 1.0 | 1.0 | 0.0 | 5.0 | 3.0 | -2.0 |

### Movie Reviews

- **rows (before → after)**: 15 → 15
- **cols (before → after)**: 3 → 4
- **nulls_total (before → after)**: 2 → 0
- **numeric cols (before → after)**: 2 → 2
- **object cols (before → after)**: 1 → 2

Numeric column stats (before/after/delta):

| column | mean_before | mean_after | mean_delta | std_before | std_after | std_delta | min_before | min_after | min_delta | max_before | max_after | max_delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rating | 6.462 | 6.667 | 0.205 | 2.933 | 2.769 | -0.164 | 2.0 | 2.0 | 0.0 | 10.0 | 10.0 | 0.0 |
| review_id | 8.0 | 8.0 | 0.0 | 4.472 | 4.472 | 0.0 | 1.0 | 1.0 | 0.0 | 15.0 | 15.0 | 0.0 |

### Financial Data

- **rows (before → after)**: 30 → 30
- **cols (before → after)**: 3 → 7
- **nulls_total (before → after)**: 9 → 8
- **numeric cols (before → after)**: 2 → 5
- **object cols (before → after)**: 1 → 1

Numeric column stats (before/after/delta):

| column | mean_before | mean_after | mean_delta | std_before | std_after | std_delta | min_before | min_after | min_delta | max_before | max_after | max_delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closing_price | 150.924 | 150.924 | 0.0 | 24.494 | 22.282 | -2.212 | 101.11 | 101.11 | 0.0 | 193.82 | 193.82 | 0.0 |
| volume | 2365.385 | 2365.385 | 0.0 | 1513.656 | 1405.394 | -108.262 | 1000.0 | 1000.0 | 0.0 | 5000.0 | 5000.0 | 0.0 |

### IoT Sensor

- **rows (before → after)**: 50 → 50
- **cols (before → after)**: 4 → 4
- **nulls_total (before → after)**: 20 → 0
- **numeric cols (before → after)**: 2 → 2
- **object cols (before → after)**: 2 → 2

Numeric column stats (before/after/delta):

| column | mean_before | mean_after | mean_delta | std_before | std_after | std_delta | min_before | min_after | min_delta | max_before | max_after | max_delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| humidity | 44.128 | 44.147 | 0.019 | 4.111 | 2.179 | -1.932 | 40.0 | 40.0 | 0.0 | 50.0 | 48.4 | -1.6 |
| temperature | 24.268 | 24.038 | -0.23 | 2.95 | 1.2 | -1.75 | 22.0 | 22.0 | 0.0 | 30.0 | 27.0 | -3.0 |
