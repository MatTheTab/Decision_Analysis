# Project 1

Implementation of PROMETHEE I, PROMETHEE II, SRF and ELECTRE TRI-B methods

## Data set

### Game Dataset
Dataset chosen and constructed by us based on publically available data is related with the topic of video games. We have decided to choose a number of interesting and varied games and obtained various criteria relating to these games from different websites. We would like to apply the methods commonly used in decision analysis to allow the user an easier time deciding about what the ranking and sorting of these games might be. Thanks to intuitive and interpretible criteria and well-known set of alternatives we can easily assess the quality of the system based on the presented results.

### Data set

**ID**: name<br>
**gain**: critic_score, user_score, length, genres, num_of_achievements<br>
**cost**: price<br>

| name                          | price | critic_score | user_score | length | genres                           | num_of_achievements |
|-------------------------------|-------|--------------|------------|--------|----------------------------------|---------------------|
| Dark Souls: Remastered        | 150   | 84           | 83         | 44     | Action, Adventure, RPG           | 41                  |
| Dark Souls III                | 200   | 89           | 90         | 49     | Action, Adventure, RPG           | 43                  |
| Terraria                      | 46    | 81           | 81         | 102    | Survival, Adventure, RPG         | 115                 |
| Baldur's Gate 3               | 250   | 96           | 89         | 107    | Strategy, Adventure, RPG         | 54                  |
| Dave the Diver                | 92    | 90           | 83         | 32     | Adventure, RPG                   | 43                  |
| Rust                          | 153   | 69           | 65         | 37     | Action, Adventure, Survival, FPS | 92                  |
| Hollow Knight                 | 68    | 90           | 91         | 42     | Action, Adventure, Platformer    | 63                  |
| Portal 2                      | 46    | 95           | 89         | 14     | Action, Puzzle, FPS              | 51                  |
| Vampire Survivors             | 20    | 86           | 83         | 25     | Action, RPG, Arcade              | 204                 |
| Hades                         | 115   | 93           | 88         | 49     | Action, RPG, Hack-and-slash      | 49                  |
| Subnautica                    | 139   | 87           | 86         | 43     | Survival, Adventure              | 17                  |
| Dishonored                    | 45    | 88           | 83         | 18     | Action, RPG, FPS                 | 80                  |
| Ori and the Will of the Wisps | 108   | 90           | 89         | 16     | Action, Adventure, Platformer    | 37                  |
| Inside                        | 72    | 93           | 83         | 4      | Adventure, Puzzle                | 14                  |
| The Forest                    | 72    | 83           | 75         | 28     | Action, Survival, Adventure      | 45                  |
| Skyrim                        | 90    | 96           | 86         | 114    | Action, Adventure, RPG           | 75                  |
| Teardown                      | 120   | 80           | 81         | 22     | Action, Puzzle                   | 27                  |
| Dying Light                   | 90    | 74           | 81         | 36     | Action, Survival                 | 78                  |
| Enter the Gungeon             | 68    | 82           | 80         | 62     | Action                           | 54                  |
| Payday 3                      | 169   | 66           | 31         | 10     | Action, FPS                      | 22                  |
| Kao the Kangaroo              | 129   | 65           | 75         | 8      | Action, Adventure                | 26                  |
| Assassin's Creed Unity        | 120   | 72           | 56         | 35     | Action, Adventure, RPG           | 57                  |
| Trials Fusion                 | 80    | 79           | 71         | 23     | Platformer                       | 51                  |
| The Sims 3                    | 28    | 83           | 78         | 78     | RPG                              | 65                  |
| Titan Souls                   | 68    | 74           | 61         | 4      | Action, Adventure                | 27                  |

### Converted genres with preference:

| genre          | points |
|----------------|--------|
| Action         | 4      |
| Adventure      | 4      |
| RPG            | 3      |
| Platformer     | 2      |
| Puzzle         | 2      |
| Hack-and-slash | 2      |
| Arcade         | 2      |
| FPS            | 1      |
| Survival       | 1      |
| Strategy       | 1      |

<br>

| name                          | price | critic_score | user_score | length | genres   | num_of_achievements |
|-------------------------------|-------|--------------|------------|--------|----------|---------------------|
| Dark Souls: Remastered        | 150   | 84           | 83         | 44     | 11       | 41                  |
| Dark Souls III                | 200   | 89           | 90         | 49     | 11       | 43                  |
| Terraria                      | 46    | 81           | 81         | 102    | 9        | 115                 |
| Baldur's Gate 3               | 250   | 96           | 89         | 107    | 8        | 54                  |
| Dave the Diver                | 92    | 90           | 83         | 32     | 7        | 43                  |
| Rust                          | 153   | 69           | 65         | 37     | 10       | 92                  |
| Hollow Knight                 | 68    | 90           | 91         | 42     | 10       | 63                  |
| Portal 2                      | 46    | 95           | 89         | 14     | 7        | 51                  |
| Vampire Survivors             | 20    | 86           | 83         | 25     | 9        | 204                 |
| Hades                         | 115   | 93           | 88         | 49     | 9        | 49                  |
| Subnautica                    | 139   | 87           | 86         | 43     | 5        | 17                  |
| Dishonored                    | 45    | 88           | 83         | 18     | 8        | 80                  |
| Ori and the Will of the Wisps | 108   | 90           | 89         | 16     | 10       | 37                  |
| Inside                        | 72    | 93           | 83         | 4      | 6        | 14                  |
| The Forest                    | 72    | 83           | 75         | 28     | 9        | 45                  |
| Skyrim                        | 90    | 96           | 86         | 114    | 11       | 75                  |
| Teardown                      | 120   | 80           | 81         | 22     | 6        | 27                  |
| Dying Light                   | 90    | 74           | 81         | 36     | 5        | 78                  |
| Enter the Gungeon             | 68    | 82           | 80         | 62     | 4        | 54                  |
| Payday 3                      | 169   | 66           | 31         | 10     | 5        | 22                  |
| Kao the Kangaroo              | 129   | 65           | 75         | 8      | 8        | 26                  |
| Assassin's Creed Unity        | 120   | 72           | 56         | 35     | 11       | 57                  |
| Trials Fusion                 | 80    | 79           | 71         | 23     | 2        | 51                  |
| The Sims 3                    | 28    | 83           | 78         | 78     | 3        | 65                  |
| Titan Souls                   | 68    | 74           | 61         | 4      | 8        | 27                  |

### Decision classes:
- 4: Very promising
- 3: Worth considering
- 2: Not preferrable
- 1: Unacceptable

### Expected pairwise comparisons:
- Payday 3 < Titan Souls
- Kao the Kangaroo < Hades
- Subnautica < Terraria
- Assassin's Creed Unity < Dark Souls: Remastered

### 3.1. Data set questions:

1. What is the domain of the problem about?

A: Evaluation of video game purchase

2. What is the source of the data?

A: SteamDB: https://steamdb.info/sales/, Metacritic: https://www.metacritic.com/game, HowLongToBeat™: https://howlongtobeat.com/, Steam Community: https://steamcommunity.com/. Some genres were selected from the entire sets and turned into numeric values based on decision makers preference. Current (21.03.2024) game prices on Steam were used, might be influenced by discounts.

3. What is the point of view of the decision maker?

A: Customer looking for a good, long but cheap game with an additional preference between genres. They care more about the user score rather than critic score. They like to collect achievements.

4. What is the number of alternatives considered? Were there more of them in the original data set?

A: 25 selected alternatives were considered. Some were chosen pseudo-randomly from the featured page, some from action-tagged featured page and some from the middle/lower part of action-tagged ratings sorted set. The original data set is much much larger.

5. Describe one of the alternatives considered (give its name, evaluations, specify preferences for this
alternative)

A: name: Dark Souls: Remastered, price: 150zł, critic_score: 84, user_score: 83, length: 44h, genres: 11, num_of_achievements: 41. This game is expected to be a good or very good choice, the price is rather high however the scores, length and number of achievements are above average and the genres points are very high.

6. What is the number of criteria considered? Were there more of them in the original data set?

A: 6 criteria were considered. More of them could be created based on the data set.

7. What is the origin of the various criteria? (catalog parameter / created by the decision maker - how?)

A: The price, scores, length and number of achievements are parameters of the datasets, genres was created by collecting information from the dataset and turning them into a numerical value based on decision maker's preference.

8. What are the domains of the individual criteria (discrete / continuous)? Note: in the case of continuous domains, specify the range of the criterion’s variability, in the case of others: list the values. What is the nature (gain / cost) of the individual criteria?

A:
- price - cost - discrete - range: 20-250, integer value
- critic_score - gain - discrete - range: 65-96, integer value
- user_score - gain - discrete - range: 31-91, integer value
- length - gain - discrete - range: 4-114, integer value
- genres - gain - discrete - range: 2-11, integer value derived from objects
- num_of_achievements - gain - discrete - range: 14-204, integer value

9. Are all criteria of equal importance (should they have the same ”weights”)? If not, can the relative
importance of the criteria under consideration be expressed in terms of weights? In this case, estimate
the weights of each criterion on a scale of 1 to 10. Are there any criteria among the criteria that are
completely or almost invalid / irrelevant?

A: There are no invalid / irrelevant criteria.

| criterion           | estimated weight |
|---------------------|--------|
| price               | 6      |
| critic_score        | 7      |
| user_score          | 10     |
| length              | 3      |
| genres              | 8      |
| num_of_achievements | 2      |

10. Are there dominated alternatives among the considered data set? If so, present all of them (dominating and dominated alternative), giving their names and values on the individual criteria.

A:

Dominated:
| name                          | price | critic_score | user_score | length | genres   | num_of_achievements |
|-------------------------------|-------|--------------|------------|--------|----------|---------------------|
| Titan Souls                   | 68    | 74           | 61         | 4      | 8        | 27                  |
| Trials Fusion                 | 80    | 79           | 71         | 23     | 2        | 51                  |
| Payday 3                      | 169   | 66           | 31         | 10     | 5        | 22                  |
| Kao the Kangaroo              | 129   | 65           | 75         | 8      | 8        | 26                  |
| Trials Fusion                 | 80    | 79           | 71         | 23     | 2        | 51                  |
| Titan Souls                   | 68    | 74           | 61         | 4      | 8        | 27                  |
| Teardown                      | 120   | 80           | 81         | 22     | 6        | 27                  |
| Dishonored                    | 45    | 88           | 83         | 18     | 8        | 80                  |
| Dark Souls: Remastered        | 150   | 84           | 83         | 44     | 11       | 41                  |
| Dave the Diver                | 92    | 90           | 83         | 32     | 7        | 43                  |
| Subnautica                    | 139   | 87           | 86         | 43     | 5        | 17                  |
| Ori and the Will of the Wisps | 108   | 90           | 89         | 16     | 10       | 37                  |
| Dying Light                   | 90    | 74           | 81         | 36     | 5        | 78                  |
| Assassin's Creed Unity        | 120   | 72           | 56         | 35     | 11       | 57                  |
| The Forest                    | 72    | 83           | 75         | 28     | 9        | 45                  |

Weakly non-dominated: None

Non-dominated:
| name                          | price | critic_score | user_score | length | genres   | num_of_achievements |
|-------------------------------|-------|--------------|------------|--------|----------|---------------------|
| Baldur's Gate 3               | 250   | 96           | 89         | 107    | 8        | 54                  |
| Dark Souls III                | 200   | 89           | 90         | 49     | 11       | 43                  |
| Rust                          | 153   | 69           | 65         | 37     | 10       | 92                  |
| Vampire Survivors             | 20    | 86           | 83         | 25     | 9        | 204                 |
| Terraria                      | 46    | 81           | 81         | 102    | 9        | 115                 |
| Skyrim                        | 90    | 96           | 86         | 114    | 11       | 75                  |
| Hollow Knight                 | 68    | 90           | 91         | 42     | 10       | 63                  |
| Hades                         | 115   | 93           | 88         | 49     | 9        | 49                  |
| Inside                        | 72    | 93           | 83         | 4      | 6        | 14                  |
| Portal 2                      | 46    | 95           | 89         | 14     | 7        | 51                  |


11. What should the theoretically best alternative look like in your opinion? Is it a small advantage on
many criteria, or rather a strong advantage on few (but key) criteria? Which?

A: The theoretically best alternative should achieve the best results on all criteria. Realistically, due to a high number of overall good choices, it should score very well on the most important (key) criteria (i.e. user_score) while remaining relatively good on the remaining ones.

12. Which of the considered alternatives (provide name and values on individual criteria) seems to be the best / definitely better than the others? Is it determined by one reason (e.g. definitely the lowest
price) or rather the overall value of the criteria? Does this alternative still have any weaknesses?

A:

| name           | price | critic_score | user_score | length | genres   | num_of_achievements |
|----------------|-------|--------------|------------|--------|----------|---------------------|
| Skyrim         | 90    | 96           | 86         | 114    | 11       | 75                  |
| Hollow Knight  | 68    | 90           | 91         | 42     | 10       | 63                  |

Skyrim: slightly below average price but maximum critic score, length and genre points, high user score
and a good number of achievements. This alternative has no apparent weakness.

Hollow Knight: relatively low price, highest user score which is the attribute with the biggest weight, relatively high critic score and genres points, slightly worse performance in length and number of achievements which are the least important criteria.

13. Which of the considered alternatives (provide name and values on individual criteria) seems to be the worst / definitely worse than the others? Is it determined by one reason (e.g. definitely the highest price), or rather the overall value of the criteria? Does this alternative still have any strengths?

A: 

| name                          | price | critic_score | user_score | length | genres   | num_of_achievements |
|-------------------------------|-------|--------------|------------|--------|----------|---------------------|
| Payday 3                      | 169   | 66           | 31         | 10     | 5        | 22                  |
| Assassin's Creed Unity        | 120   | 72           | 56         | 35     | 11       | 57                  |

Payday 3: high price, the worst user score (most important criterion), almost the worst critic score, very low length
and genres points, low number of achievements. There is no positive attribute.

Assassin's Creed Unity: above average price, very low user score and low critic score, below average length, average number of achievements. The only plus is the maximum genres points.

## 3.2. Problem analysis with the use of PROMETHEE I and II

1. Write the preferential information you provided at the input of the method.

A:

2. Enter the final result obtained with the method. Usually, the first result is not the final one, you can slightly adjust the parameter values to your preferences.

A:

3. Compare the complete and partial ranking.

A:

4. Comment on the compliance of the results with your expectations and preferences. Refer, among others, to to the results for the alternatives that you indicated as the best and worst during the data
analysis. What operations were required to obtain the final result (e.g. changing the ranking of criteria, adding blank cards, changing the value of threshold)?

A:

## 3.3. Problem analysis with the use of ELECTRE TRI-B

1. Write the preferential information you provided at the input of the method.

A:
#### Classes:
- Very promising
- Worth considering
- Not preferrable
- Unacceptable

#### Boundary profiles:

| name    | price | critic_score | user_score | length | genres   | num_of_achievements |
|---------|-------|--------------|------------|--------|----------|---------------------|
| b_0     | 250   | 50           | 31         | 20     | 0        | 5                   |
| b_1     | 200   | 67           | 50         | 50     | 3        | 20                  |
| b_2     | 140   | 75           | 73         | 70     | 5        | 50                  |
| b_3     | 90    | 88           | 83         | 85     | 7        | 100                 |
| b_4     | 20    | 96           | 91         | 114    | 11       | 204                 |

2. Enter the final result obtained with the method. Usually, the first result is not the final one, you can slightly adjust the parameter values to your preferences.

A:

3. Comment on the compliance of the results with your expectations and preferences. Refer, among
others, to to the results for the alternatives that you indicated as the best and worst during the data
analysis. What operations were required to obtain the final result (e.g. changing the ranking of criteria, adding blank cards, changing the value of threshold)?

A:

4. Compare the optimistic and pessimistic class assignments.

A:

5. Comment on the compliance of the results with your expectations and preferences. Refer, among
others, to to the results for the alternatives that you indicated as the best and worst during the data
analysis. What operations were required to obtain the final result (e.g. changing the ranking of criteria, adding blank cards, changing the value of threshold, boundaries or the λ parameter)?

A:

## 3.4. Compare method results