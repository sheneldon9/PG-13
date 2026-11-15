# Pandemic P

1. Was Playoff P a statistically real thing and is it still a thing now?  
Did his stats rise/drop/stay the same come playoff time?
### Basic Stats:
- Points, Rebounds, Assists, TOV, eFG% (Per 100 possessions)  
Use for initial comparisons - box and whisker for regular season, individual dots for individual playoff games per year
### Advanced Stats:
- PER, TS%, OWS, DWS, WS/48, OBPM, DBPM, VORP/WORP  
Adjusted shooting will be a better comparison statistic

2. How does his production and cap hit per year compare to other star players?  
Compare with other players through **a)** usage percentage, **b)** salary cap hit to see if he is more or less bang for the buck
- Consistently top 10 in yearly salary since 2018
- Usage percentage around 30% since 2014

Ways to scrape data:
- https://pypi.org/project/nba-api/
- https://jaebradley.github.io/basketball_reference_web_scraper/development/

## Useful Links:
- https://www.basketball-reference.com/players/g/georgpa01.html
- https://www.reddit.com/r/nbadiscussion/comments/gvmsr6/adjusted_shooting_and_how_measures_of_shooting/
- https://www.basketball-reference.com/about/glossary.html
- https://www.salaryswish.com/players/paul-george
- https://www.espn.com/nba/salaries
- https://www.basketball-reference.com/contracts/players.html

## Formulas:
$$\text{Per 100 possession}=\text{Stat per game}\times\frac{48\text{ min}}{\text{min per game}}\times\frac{100 \text{ possessions}}{\text{ team pace}}$$  
$$\text{Pace}=48\times(\frac{\text{Team Possessions + Opponent Possessions}}{2\times(\frac{\text{Team Minutes Played}}{5})})$$  
$$\text{Poss}=0.5\times(\text{TmPoss + OppPoss})$$  
$\text{TmPoss}=\text{TmFGA}+[0.4\times\text{TmFTA}]-[1.07\times(\frac{\text{TmORB}}{\text{TmORB + OppDRB}})\times(\text{TmFGA - TmFG})]+\text{TmTOV}$
- Switch Tm with Opp and vice-versa to find OppPoss
