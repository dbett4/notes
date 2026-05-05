# MySPariEdge Grade Reverse Engineering

This is a surrogate model inferred from pulled MySPariEdge data, not the internal formula.

## Working Theory

Projection grades are mostly market-specific thresholds on `abs(projection - line)`.

- Side is inferred from projection edge: projection above line = Over, below line = Under.
- The same absolute edge has different meaning by market. A `0.25` RBI edge can grade high; a `0.25` H+R+RBI edge is closer to middle tier.
- Best Bets appear to use the same grade field plus historical pattern records. The displayed win percentage is not the grade by itself.

## Projection Grade Thresholds

| Market | Grade | Count | Abs Edge Range | Avg Abs Edge | Side Mix |
|---|---|---:|---:|---:|---|
| Earned Runs | A | 2 | 1.20-1.20 | 1.20 | Over:1, Under:1 |
| Earned Runs | A- | 1 | 1.00-1.00 | 1.00 | Over:1 |
| Earned Runs | B+ | 6 | 0.70-0.90 | 0.80 | Over:3, Under:3 |
| Earned Runs | B | 5 | 0.50-0.60 | 0.56 | Over:4, Under:1 |
| Earned Runs | B- | 5 | 0.30-0.40 | 0.32 | Over:2, Under:3 |
| Earned Runs | C+ | 6 | 0.00-0.20 | 0.08 | Over:2, Push:2, Under:2 |
| Hits | A+ | 21 | 0.44-0.56 | 0.48 | Over:13, Under:8 |
| Hits | A | 43 | 0.38-0.49 | 0.41 | Over:34, Under:9 |
| Hits | A- | 34 | 0.34-0.43 | 0.36 | Over:25, Under:9 |
| Hits | B+ | 37 | 0.31-0.35 | 0.32 | Over:30, Under:7 |
| Hits | B | 42 | 0.25-0.31 | 0.29 | Over:39, Under:3 |
| Hits | B- | 42 | 0.15-0.27 | 0.20 | Over:41, Under:1 |
| Hits | C+ | 45 | 0.00-0.15 | 0.08 | Over:36, Push:3, Under:6 |
| Hits + Runs + RBIs | A+ | 28 | 0.77-1.44 | 0.93 | Over:28 |
| Hits + Runs + RBIs | A | 30 | 0.56-0.90 | 0.67 | Over:30 |
| Hits + Runs + RBIs | A- | 39 | 0.39-0.80 | 0.51 | Over:26, Under:13 |
| Hits + Runs + RBIs | B+ | 40 | 0.28-0.63 | 0.38 | Over:32, Under:8 |
| Hits + Runs + RBIs | B | 49 | 0.15-0.35 | 0.24 | Over:25, Under:24 |
| Hits + Runs + RBIs | B- | 39 | 0.07-0.20 | 0.12 | Over:16, Under:23 |
| Hits + Runs + RBIs | C+ | 39 | 0.00-0.11 | 0.04 | Over:10, Push:3, Under:26 |
| Hits Allowed | A+ | 1 | 1.60-1.60 | 1.60 | Over:1 |
| Hits Allowed | A | 2 | 1.20-1.30 | 1.25 | Under:2 |
| Hits Allowed | B+ | 4 | 0.70-0.90 | 0.80 | Over:3, Under:1 |
| Hits Allowed | B | 3 | 0.50-0.60 | 0.57 | Over:1, Under:2 |
| Hits Allowed | B- | 8 | 0.30-0.40 | 0.34 | Over:2, Under:6 |
| Hits Allowed | C+ | 7 | 0.10-0.20 | 0.17 | Over:4, Under:3 |
| RBIs | A+ | 22 | 0.27-0.57 | 0.32 | Over:13, Under:9 |
| RBIs | A | 40 | 0.22-0.27 | 0.25 | Over:6, Under:34 |
| RBIs | A- | 38 | 0.18-0.24 | 0.20 | Over:4, Under:34 |
| RBIs | B+ | 45 | 0.15-0.18 | 0.17 | Over:6, Under:39 |
| RBIs | B | 40 | 0.10-0.15 | 0.13 | Over:5, Under:35 |
| RBIs | B- | 43 | 0.06-0.11 | 0.08 | Over:12, Under:31 |
| RBIs | C+ | 37 | 0.00-0.06 | 0.03 | Over:15, Push:4, Under:18 |
| Runs | A+ | 26 | 0.30-0.41 | 0.33 | Over:14, Under:12 |
| Runs | A | 36 | 0.26-0.31 | 0.28 | Over:6, Under:30 |
| Runs | A- | 44 | 0.18-0.28 | 0.22 | Over:11, Under:33 |
| Runs | B+ | 36 | 0.15-0.23 | 0.17 | Over:8, Under:28 |
| Runs | B | 43 | 0.11-0.18 | 0.13 | Over:12, Under:31 |
| Runs | B- | 43 | 0.05-0.13 | 0.08 | Over:20, Under:23 |
| Runs | C+ | 37 | 0.00-0.05 | 0.03 | Over:16, Push:2, Under:19 |
| Strikeouts | A | 2 | 1.70-2.00 | 1.85 | Over:2 |
| Strikeouts | A- | 1 | 1.00-1.00 | 1.00 | Over:1 |
| Strikeouts | B+ | 5 | 0.70-1.10 | 0.82 | Over:5 |
| Strikeouts | B | 5 | 0.50-0.60 | 0.56 | Over:2, Under:3 |
| Strikeouts | B- | 8 | 0.30-1.40 | 0.57 | Over:5, Under:3 |
| Strikeouts | C+ | 6 | 0.10-0.20 | 0.13 | Over:5, Under:1 |
| Strikeouts | C | 1 | 0.00-0.00 | 0.00 | Push:1 |
| Total Bases | A+ | 30 | 0.82-1.17 | 0.93 | Over:30 |
| Total Bases | A | 41 | 0.65-0.82 | 0.74 | Over:41 |
| Total Bases | A- | 44 | 0.54-0.68 | 0.62 | Over:44 |
| Total Bases | B+ | 39 | 0.43-0.59 | 0.53 | Over:33, Under:6 |
| Total Bases | B | 36 | 0.29-0.48 | 0.38 | Over:29, Under:7 |
| Total Bases | B- | 43 | 0.11-0.29 | 0.20 | Over:27, Under:16 |
| Total Bases | C+ | 32 | 0.01-0.15 | 0.06 | Over:12, Under:20 |
| Walks Allowed | A+ | 1 | 1.40-1.40 | 1.40 | Over:1 |
| Walks Allowed | A | 3 | 0.80-0.80 | 0.80 | Under:3 |
| Walks Allowed | A- | 4 | 0.60-0.70 | 0.65 | Over:2, Under:2 |
| Walks Allowed | B+ | 14 | 0.40-0.50 | 0.46 | Over:10, Under:4 |
| Walks Allowed | B- | 3 | 0.20-0.20 | 0.20 | Over:3 |

## Best Bets Grade Evidence

| Market | Grade | Count | Abs Edge Range | Avg Abs Edge | Side Mix |
|---|---|---:|---:|---:|---|
| Earned Runs | A | 1 | 1.20-1.20 | 1.20 | Over:1 |
| Hits | A+ | 8 | 0.44-0.56 | 0.49 | Under:8 |
| Hits | B | 3 | 0.25-0.31 | 0.28 | Under:3 |
| RBIs | A+ | 9 | 0.27-0.27 | 0.27 | Under:9 |
| RBIs | A | 34 | 0.22-0.27 | 0.25 | Under:34 |
| RBIs | A- | 34 | 0.18-0.24 | 0.20 | Under:34 |
| RBIs | B+ | 39 | 0.15-0.18 | 0.17 | Under:39 |
| RBIs | B | 35 | 0.10-0.15 | 0.13 | Under:35 |
| RBIs | B- | 31 | 0.06-0.11 | 0.08 | Under:31 |
| RBIs | C+ | 18 | 0.01-0.06 | 0.03 | Under:18 |
| Runs | A+ | 12 | 0.30-0.31 | 0.30 | Under:12 |

## Practical Clone

For a local first pass, use market-specific absolute-edge cutoffs learned from this table:

1. Compute `edge = projection - line`.
2. Side is `Over` if edge is positive and `Under` if edge is negative.
3. Within each market, assign the highest grade whose observed absolute-edge range contains the edge.
4. Promote candidates only when the inferred grade is `A+`, `A`, `A-`, or `B+` and model history for that market/side/grade is strong.

This gets us an inspectable approximation. To make it durable, keep daily snapshots and refit thresholds over multiple slates.
