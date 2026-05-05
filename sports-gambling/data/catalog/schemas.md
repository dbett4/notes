# d + bet Canonical Betting Spine

## Conclusion

Every sport-specific model should map into the same betting spine: events, participants, markets, odds snapshots, feature sets, signals, results, and validation runs. Sport-specific details belong in feature tables, not in one-off signal schemas.

## Entities

### Event

A scheduled contest or fight.

Required fields:

- `sport`
- `league`
- `season`
- `event_id`
- `event_date`
- `start_time`
- `home_team`
- `away_team`
- `status`

### Participant

A team, player, pitcher, goalie, fighter, or lineup member linked to an event or season.

Required fields:

- `sport`
- `participant_type`
- `participant_id`
- `display_name`
- `team_id`
- `source`

### Market

A bettable market definition, independent of sportsbook price.

Required fields:

- `sport`
- `event_id`
- `market`
- `selection`
- `line`
- `player_id`
- `player_name`
- `prop_category`

### Odds Snapshot

One observed sportsbook price for one market at one timestamp.

Required fields:

- `sport`
- `event_id`
- `market`
- `selection`
- `line`
- `book`
- `american_odds`
- `observed_at`
- `is_open`
- `is_close`

### Feature Set

Versioned model inputs generated before a signal.

Required fields:

- `sport`
- `feature_set`
- `feature_version`
- `generated_at`
- `source_files`
- `row_count`
- `notes`

### Signal

A model or source recommendation before execution.

Required fields:

- `sport`
- `event_id`
- `market`
- `selection`
- `line`
- `signal_source`
- `signal_probability`
- `source_odds`
- `source_book`
- `source_timestamp`
- `rank`
- `confidence`
- `feature_version`

### Result

The settled outcome of an event or player stat market.

Required fields:

- `sport`
- `event_id`
- `market`
- `selection`
- `line`
- `final_score`
- `stat_result`
- `settlement`
- `settled_at`

### Validation Run

Evidence that a signal source has or lacks edge.

Required fields:

- `sport`
- `signal_source`
- `sample_start`
- `sample_end`
- `settled_bets`
- `avg_clv`
- `roi`
- `hit_rate`
- `avg_odds`
- `calibration_notes`

## Duplicate Recommendation Identity

The same underlying bet should collapse to one recommendation row using:

`date + event_id + market + selection + line + player_id/player_name + pick`

Sportsbook prices are execution context, not separate primary recommendations.

