# Pandemic P

1. Why is Paul George so highly sought after?!?  
OKC, Clippers, Celtics all paid exorbitant prices for him, even more-so in hindsight
### Basic Stats:
- Points, Rebounds, Assists, TOV, eFG% (Per 100 possessions)  
Use for initial comparisons - box and whisker for regular season, individual dots for individual playoff games per year
### Advanced Stats:
- PER, TS%, OWS, DWS, WS/48, OBPM, DBPM, VORP/WORP  
Adjusted shooting will be a better comparison statistic  
Comparing similar players through **a)** usage percentage, **b)** audience player skill perception

2. Do the stats back how much he gets paid?
- 4 year, 190 mil - clippers
- 4 year, 212 mil - 76ers

Ways to scrape data:
- https://pypi.org/project/nba-api/
- https://jaebradley.github.io/basketball_reference_web_scraper/development/

## Useful Links:
- https://www.reddit.com/r/nbadiscussion/comments/gvmsr6/adjusted_shooting_and_how_measures_of_shooting/
- https://www.basketball-reference.com/about/glossary.html

## Formulas:
$$\text{Per 100 possession}=\text{Stat per game}\times\frac{48\text{ min}}{\text{min per game}}\times\frac{100 \text{ possessions}}{\text{ team pace}}$$  
$$\text{Pace}=48\times(\frac{\text{Team Possessions + Opponent Possessions}}{2\times(\frac{\text{Team Minutes Played}}{5})})$$  
$$\text{Poss}=0.5\times(\text{TmPoss + OppPoss})$$  
$\text{TmPoss}=\text{TmFGA}+[0.4\times\text{TmFTA}]-[1.07\times(\frac{\text{TmORB}}{\text{TmORB + OppDRB}})\times(\text{TmFGA - TmFG})]+\text{TmTOV}$
- Switch Tm with Opp and vice-versa to find OppPoss
