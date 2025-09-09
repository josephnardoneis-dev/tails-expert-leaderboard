#!/usr/bin/env python3
"""
Comprehensive OddsHopper Expert Leaderboard
Real experts from OddsHopper with profile links and expanded data
"""

import sys
sys.path.append('/Users/josephnardone/tails-expert-leaderboard')
from tails_leaderboard import TailsLeaderboard, Pick
from datetime import datetime, timedelta
import random

def create_comprehensive_leaderboard():
    """Create leaderboard with all real OddsHopper experts"""
    leaderboard = TailsLeaderboard()
    
    # Real OddsHopper experts with profile links and simulated performance data
    experts_data = {
        "Defy The Odds": {
            "profile_url": "https://www.oddsshopper.com/experts/defytheodds",
            "followers": 3762,
            "specialties": ["NBA", "NFL", "NCAAF", "NCAAB", "MLB", "NHL", "Soccer", "WNBA", "Tennis", "MMA/Boxing"],
            "bio": "Join our exclusive VIP community and unlock your potential for long-term success",
            "picks": [
                ("NBA", "Lakers vs Warriors", "Spread", "Lakers +3.5", "-110", "2024-09-08", "win"),
                ("NFL", "Chiefs vs Ravens", "Moneyline", "Chiefs ML", "-120", "2024-09-07", "win"),
                ("MLB", "Yankees vs Red Sox", "Total", "Over 9.5", "-105", "2024-09-06", "loss"),
                ("NBA", "Celtics vs Heat", "Player Prop", "Tatum Over 28.5 Pts", "-115", "2024-09-05", "win"),
                ("NFL", "Bills vs Dolphins", "Spread", "Bills -3.5", "-110", "2024-09-04", "win"),
                ("NCAAF", "Alabama vs Georgia", "Total", "Under 52.5", "-105", "2024-09-03", "loss"),
                ("NBA", "Nuggets vs Suns", "Moneyline", "Nuggets ML", "-140", "2024-09-02", "win"),
                ("MLB", "Dodgers vs Padres", "Player Prop", "Betts Over 1.5 Hits", "-110", "2024-09-01", "win"),
                ("NFL", "Packers vs Bears", "Spread", "Packers -2.5", "-110", "2024-08-31", "loss"),
                ("NBA", "Clippers vs Mavs", "Total", "Over 225.5", "-105", "2024-08-30", "win"),
                ("WNBA", "Aces vs Storm", "Spread", "Aces -4.5", "-110", "2024-08-29", "win"),
                ("NHL", "Rangers vs Devils", "Moneyline", "Rangers ML", "-125", "2024-08-28", "win")
            ]
        },
        "DFSnDonuts Picks": {
            "profile_url": "https://www.oddsshopper.com/experts/dfsndonutspicks",
            "followers": 2940,
            "specialties": ["NFL", "NBA", "NCAAF", "MLB", "Soccer", "PGA", "Tennis", "WNBA", "MMA/Boxing", "NHL"],
            "bio": "Full-Time Sports Bettor with a Discord community of 10,000 fellow sports bettors",
            "picks": [
                ("NFL", "Cowboys vs Giants", "Player Prop", "Dak Over 275.5 Pass Yds", "-110", "2024-09-08", "win"),
                ("NBA", "Warriors vs Lakers", "Spread", "Warriors -1.5", "-105", "2024-09-07", "win"),
                ("MLB", "Astros vs Rangers", "Total", "Under 8.5", "-110", "2024-09-06", "win"),
                ("NFL", "49ers vs Rams", "Moneyline", "49ers ML", "-130", "2024-09-05", "loss"),
                ("NCAAF", "Ohio State vs Michigan", "Spread", "Ohio State -7.5", "-110", "2024-09-04", "win"),
                ("NBA", "Bucks vs Nets", "Player Prop", "Giannis Over 30.5 Pts", "-115", "2024-09-03", "win"),
                ("MLB", "Mets vs Phillies", "Total", "Over 9.5", "-105", "2024-09-02", "loss"),
                ("NFL", "Bengals vs Browns", "Spread", "Bengals -3.5", "-110", "2024-09-01", "win"),
                ("NBA", "76ers vs Knicks", "Moneyline", "76ers ML", "+105", "2024-08-31", "win"),
                ("Soccer", "Man City vs Arsenal", "Both Teams Score", "Yes", "-120", "2024-08-30", "win"),
                ("WNBA", "Liberty vs Sun", "Spread", "Liberty -2.5", "-110", "2024-08-29", "loss"),
                ("Tennis", "Djokovic vs Alcaraz", "Set Betting", "Djokovic 3-1", "+160", "2024-08-28", "win")
            ]
        },
        "DKDFS": {
            "profile_url": "https://www.oddsshopper.com/experts/dkdfs",
            "followers": 1800,
            "specialties": ["NBA", "NFL", "WNBA"],
            "bio": "Daily fantasy sports and player prop expert",
            "picks": [
                ("NBA", "Celtics vs Lakers", "Player Prop", "LeBron Over 7.5 Assists", "-110", "2024-09-08", "win"),
                ("NFL", "Eagles vs Cowboys", "Player Prop", "Hurts Over 2.5 Pass TDs", "+105", "2024-09-07", "win"),
                ("WNBA", "Aces vs Storm", "Player Prop", "Wilson Over 25.5 Pts", "-115", "2024-09-06", "loss"),
                ("NBA", "Warriors vs Nuggets", "Player Prop", "Curry Over 4.5 Threes", "+110", "2024-09-05", "win"),
                ("NFL", "Chiefs vs Bills", "Player Prop", "Mahomes Over 275.5 Pass Yds", "-110", "2024-09-04", "win"),
                ("WNBA", "Liberty vs Sun", "Player Prop", "Stewart Over 20.5 Pts", "-110", "2024-09-03", "loss"),
                ("NBA", "Heat vs Bucks", "Player Prop", "Butler Over 22.5 Pts", "-105", "2024-09-02", "win"),
                ("NFL", "Ravens vs Steelers", "Player Prop", "Lamar Over 225.5 Pass Yds", "-110", "2024-09-01", "win"),
                ("WNBA", "Sky vs Fever", "Player Prop", "Clark Over 18.5 Pts", "-115", "2024-08-31", "win"),
                ("NBA", "Clippers vs Suns", "Player Prop", "Durant Over 27.5 Pts", "-110", "2024-08-30", "loss")
            ]
        },
        "Chef T": {
            "profile_url": "https://www.oddsshopper.com/experts/chef-t",
            "followers": 2400,
            "specialties": ["NBA", "MLB", "Soccer", "WNBA", "NFL", "NHL", "PGA", "MMA/Boxing", "NCAAF", "NCAAB"],
            "bio": "I like to cook and watch sports... preferably at the same time",
            "picks": [
                ("MLB", "Dodgers vs Giants", "Moneyline", "Dodgers ML", "-135", "2024-09-08", "win"),
                ("NBA", "Lakers vs Celtics", "Total", "Over 220.5", "-110", "2024-09-07", "win"),
                ("Soccer", "Liverpool vs Chelsea", "Spread", "Liverpool -0.5", "+105", "2024-09-06", "loss"),
                ("NFL", "Packers vs Vikings", "Total", "Under 47.5", "-110", "2024-09-05", "win"),
                ("MLB", "Yankees vs Orioles", "Spread", "Yankees -1.5", "+110", "2024-09-04", "win"),
                ("WNBA", "Mercury vs Dream", "Moneyline", "Mercury ML", "-120", "2024-09-03", "loss"),
                ("NHL", "Bruins vs Rangers", "Total", "Over 6.5", "-105", "2024-09-02", "win"),
                ("PGA", "BMW Championship", "Outright", "Scheffler Top 5", "-110", "2024-09-01", "win"),
                ("MMA", "UFC Main Event", "Method", "Goes Distance", "+120", "2024-08-31", "loss"),
                ("NCAAF", "Texas vs Oklahoma", "Spread", "Texas -3.5", "-110", "2024-08-30", "win"),
                ("NCAAB", "Duke vs UNC", "Total", "Over 145.5", "-105", "2024-08-29", "win")
            ]
        },
        "NarcocopMMA": {
            "profile_url": "https://www.oddsshopper.com/experts/narcocopmma",
            "followers": 437,
            "specialties": ["MMA/Boxing", "WNBA", "NFL", "NBA", "PGA", "NCAAF"],
            "bio": "Won over 200u on MMA in the past 2 years",
            "picks": [
                ("MMA", "Jones vs Miocic", "Moneyline", "Jones ML", "-180", "2024-09-08", "win"),
                ("Boxing", "Fury vs Usyk", "Method", "Goes Distance", "+110", "2024-09-07", "win"),
                ("UFC", "Main Event", "Total Rounds", "Over 2.5", "-120", "2024-09-06", "win"),
                ("MMA", "Co-Main Event", "Moneyline", "Underdog ML", "+150", "2024-09-05", "loss"),
                ("Boxing", "Heavyweight Bout", "Method", "KO/TKO", "+140", "2024-09-04", "win"),
                ("WNBA", "Aces vs Liberty", "Spread", "Aces -3.5", "-110", "2024-09-03", "win"),
                ("UFC", "Women's Title Fight", "Total Rounds", "Under 4.5", "-105", "2024-09-02", "loss"),
                ("NFL", "Chiefs vs Bills", "Moneyline", "Chiefs ML", "-115", "2024-09-01", "win"),
                ("MMA", "Bellator Main Event", "Method", "Submission", "+200", "2024-08-31", "win"),
                ("NBA", "Finals Game", "Total", "Over 210.5", "-110", "2024-08-30", "loss")
            ]
        },
        "She Got Game": {
            "profile_url": "https://www.oddsshopper.com/experts/pettyqueen",
            "followers": 2300,
            "specialties": ["NBA", "MLB", "NFL", "NHL", "Soccer"],
            "bio": "We aim to bring together a community of like-minded individuals who love to gamble",
            "picks": [
                ("NBA", "Storm vs Aces", "Spread", "Storm +4.5", "-110", "2024-09-08", "win"),
                ("MLB", "Braves vs Mets", "Total", "Under 8.5", "-105", "2024-09-07", "win"),
                ("NFL", "Saints vs Falcons", "Moneyline", "Saints ML", "+105", "2024-09-06", "loss"),
                ("NHL", "Lightning vs Panthers", "Spread", "Lightning +1.5", "-110", "2024-09-05", "win"),
                ("Soccer", "Barcelona vs Real Madrid", "Total Goals", "Over 2.5", "-115", "2024-09-04", "win"),
                ("NBA", "Mercury vs Sky", "Player Prop", "Taurasi Over 15.5 Pts", "-110", "2024-09-03", "loss"),
                ("MLB", "Cubs vs Cardinals", "Spread", "Cubs -1.5", "+110", "2024-09-02", "win"),
                ("NFL", "Broncos vs Raiders", "Total", "Under 44.5", "-110", "2024-09-01", "win"),
                ("NHL", "Oilers vs Flames", "Moneyline", "Oilers ML", "-130", "2024-08-31", "win"),
                ("Soccer", "Premier League", "Both Teams Score", "No", "+120", "2024-08-30", "loss")
            ]
        },
        # Adding more from the original free picks page
        "MoneyBall Metrics": {
            "profile_url": "https://www.oddsshopper.com/experts/moneyball-metrics",
            "followers": 1500,
            "specialties": ["MLB", "NBA", "NFL"],
            "bio": "Data-driven sports betting using advanced analytics",
            "picks": [
                ("MLB", "Dodgers vs Padres", "Player Prop", "Ohtani Over 1.5 Total Bases", "-115", "2024-09-08", "win"),
                ("NBA", "Lakers vs Warriors", "Total", "Over 230.5", "-110", "2024-09-07", "win"),
                ("NFL", "Chiefs vs Ravens", "Spread", "Chiefs -2.5", "-110", "2024-09-06", "loss"),
                ("MLB", "Yankees vs Red Sox", "Moneyline", "Yankees ML", "-140", "2024-09-05", "win"),
                ("NBA", "Celtics vs Heat", "Player Prop", "Brown Over 25.5 Pts", "-110", "2024-09-04", "win"),
                ("NFL", "Bills vs Dolphins", "Total", "Over 48.5", "-105", "2024-09-03", "loss"),
                ("MLB", "Astros vs Rangers", "Spread", "Astros -1.5", "+105", "2024-09-02", "win"),
                ("NBA", "Nuggets vs Suns", "Moneyline", "Nuggets ML", "-125", "2024-09-01", "win")
            ]
        },
        "Greg Ehrenberg": {
            "profile_url": "https://www.oddsshopper.com/experts/greg-ehrenberg",
            "followers": 2100,
            "specialties": ["MLB", "WNBA", "NBA"],
            "bio": "Expert MLB and player props analyst",
            "picks": [
                ("MLB", "Noah Cameron Props", "Player Prop", "Over 5.5 K's", "-115", "2024-09-07", "win"),
                ("MLB", "Zack Littell Props", "Player Prop", "Under 6.5 K's", "+105", "2024-09-07", "win"),
                ("WNBA", "Kelsey Plum Props", "Player Prop", "Over 18.5 Points", "-110", "2024-09-06", "loss"),
                ("MLB", "Corbin Burnes Props", "Player Prop", "Over 7.5 K's", "-105", "2024-09-05", "win"),
                ("MLB", "Freddie Freeman Props", "Player Prop", "Over 1.5 Hits", "-120", "2024-09-04", "win"),
                ("WNBA", "A'ja Wilson Props", "Player Prop", "Over 22.5 Points", "-115", "2024-09-03", "win"),
                ("MLB", "Aaron Judge Props", "Player Prop", "Over 1.5 Total Bases", "-110", "2024-09-02", "loss"),
                ("MLB", "Mookie Betts Props", "Player Prop", "Over 1.5 Hits", "-105", "2024-09-01", "win"),
                ("WNBA", "Breanna Stewart Props", "Player Prop", "Over 20.5 Points", "-110", "2024-08-31", "win"),
                ("MLB", "Shohei Ohtani Props", "Player Prop", "Over 1.5 Total Bases", "-115", "2024-08-30", "win")
            ]
        },
        "Ziny Bets": {
            "profile_url": "https://www.oddsshopper.com/experts/ziny-bets",
            "followers": 890,
            "specialties": ["NFL", "NBA", "Soccer"],
            "bio": "Young and hungry bettor with sharp insights",
            "picks": [
                ("NFL", "Eagles vs Cowboys", "Spread", "Eagles -3.5", "-110", "2024-09-08", "win"),
                ("NBA", "Lakers vs Clippers", "Total", "Over 225.5", "-105", "2024-09-07", "win"),
                ("Soccer", "Man City vs Liverpool", "Both Teams Score", "Yes", "-115", "2024-09-06", "loss"),
                ("NFL", "49ers vs Rams", "Moneyline", "49ers ML", "-130", "2024-09-05", "win"),
                ("NBA", "Warriors vs Kings", "Spread", "Warriors -4.5", "-110", "2024-09-04", "win"),
                ("Soccer", "Chelsea vs Arsenal", "Total Goals", "Under 2.5", "+110", "2024-09-03", "loss"),
                ("NFL", "Packers vs Bears", "Total", "Over 45.5", "-110", "2024-09-02", "win"),
                ("NBA", "Nets vs Knicks", "Moneyline", "Knicks ML", "-140", "2024-09-01", "win")
            ]
        },
        "Mikey's Mashers": {
            "profile_url": "https://www.oddsshopper.com/experts/mikeys-mashers",
            "followers": 1750,
            "specialties": ["College Football", "NFL", "MLB"],
            "bio": "Crushing college football and NFL picks all season long",
            "picks": [
                ("College Football", "Florida vs LSU", "Spread", "Florida +9.5", "-110", "2024-09-07", "win"),
                ("MLB", "Pirates vs Orioles", "Total", "Under 8.5", "-105", "2024-09-07", "loss"),
                ("NFL", "Xavier Worthy Props", "Player Prop", "Over 3.5 Receptions", "+120", "2024-09-08", "win"),
                ("College Football", "Alabama vs Georgia", "Spread", "Alabama -3.5", "-115", "2024-09-06", "win"),
                ("NFL", "Mahomes Passing Yards", "Player Prop", "Over 275.5", "-110", "2024-09-05", "loss"),
                ("MLB", "Yankees vs Red Sox", "Moneyline", "Yankees ML", "-140", "2024-09-04", "win"),
                ("College Football", "Ohio State vs Penn State", "Total", "Over 52.5", "-105", "2024-09-03", "win"),
                ("NFL", "Kelce Receiving Yards", "Player Prop", "Over 75.5", "-115", "2024-09-02", "win")
            ]
        },
        "PrizePick Champions": {
            "profile_url": "https://www.oddsshopper.com/experts/prizepick-champions",
            "followers": 1200,
            "specialties": ["NBA", "NFL", "MLB", "WNBA"],
            "bio": "PrizePicks specialists with consistent winning slips",
            "picks": [
                ("NBA", "LeBron James Props", "Player Prop", "Over 25.5 Points", "-110", "2024-09-08", "win"),
                ("NFL", "Josh Allen Props", "Player Prop", "Over 275.5 Pass Yds", "-115", "2024-09-07", "win"),
                ("MLB", "Ronald Acuna Props", "Player Prop", "Over 1.5 Total Bases", "-105", "2024-09-06", "loss"),
                ("WNBA", "A'ja Wilson Props", "Player Prop", "Over 24.5 Points", "-110", "2024-09-05", "win"),
                ("NBA", "Steph Curry Props", "Player Prop", "Over 4.5 Threes", "+110", "2024-09-04", "win"),
                ("NFL", "Travis Kelce Props", "Player Prop", "Over 5.5 Receptions", "-120", "2024-09-03", "loss"),
                ("MLB", "Mookie Betts Props", "Player Prop", "Over 1.5 Hits", "-110", "2024-09-02", "win"),
                ("WNBA", "Breanna Stewart Props", "Player Prop", "Over 21.5 Points", "-105", "2024-09-01", "win")
            ]
        },
        "MoneyBadgerJake": {
            "profile_url": "https://www.oddsshopper.com/experts/moneybadgerjake",
            "followers": 1650,
            "specialties": ["MLB", "NFL", "NBA"],
            "bio": "Consistent winner across multiple sports with solid bankroll management",
            "picks": [
                ("MLB", "Reds vs Cardinals", "Moneyline", "Reds F5 ML", "+105", "2024-09-07", "loss"),
                ("NFL", "Chiefs vs Ravens", "Spread", "Chiefs -2.5", "-110", "2024-09-06", "win"),
                ("MLB", "Braves vs Phillies", "Total", "Over 8.5", "-105", "2024-09-05", "win"),
                ("NFL", "Bills vs Dolphins", "Moneyline", "Bills ML", "-135", "2024-09-04", "loss"),
                ("MLB", "Mets vs Nationals", "Spread", "Mets -1.5", "+110", "2024-09-03", "win"),
                ("NFL", "Cowboys vs Giants", "Total", "Under 47.5", "-110", "2024-09-02", "win"),
                ("MLB", "Cubs vs Brewers", "Moneyline", "Cubs F5 ML", "+115", "2024-09-01", "loss"),
                ("NFL", "49ers vs Rams", "Spread", "49ers -3.5", "-105", "2024-08-31", "win")
            ]
        }
    }
    
    # Add all picks to the database
    for expert_name, data in experts_data.items():
        for i, (sport, game, bet_type, selection, odds, date, result) in enumerate(data["picks"]):
            pick_id = f"{expert_name}_{i+1}_{date}"
            
            # Calculate units won based on odds and result
            if result == "win":
                if odds.startswith("+"):
                    units_won = 1 + (int(odds[1:]) / 100)
                else:
                    units_won = 1 + (100 / abs(int(odds)))
            elif result == "push":
                units_won = 1.0
            else:
                units_won = 0.0
            
            pick = Pick(
                pick_id=pick_id,
                expert_name=expert_name,
                sport=sport,
                game=game,
                bet_type=bet_type,
                selection=selection,
                odds=odds,
                date=date,
                result=result,
                units_risked=1.0,
                units_won=units_won
            )
            
            leaderboard.add_pick(pick)
    
    return leaderboard, experts_data

def display_expert_directory(experts_data):
    """Display expert directory with profile links"""
    print("\n🔗 ODDSSHOPPER EXPERT DIRECTORY")
    print("=" * 80)
    print(f"{'Expert':<25} {'Followers':<10} {'Specialties':<20} {'Profile URL'}")
    print("-" * 80)
    
    for expert_name, data in experts_data.items():
        followers = f"{data['followers']:,}" if data['followers'] else "N/A"
        specialties = ", ".join(data['specialties'][:3]) + "..." if len(data['specialties']) > 3 else ", ".join(data['specialties'])
        print(f"{expert_name:<25} {followers:<10} {specialties:<20} {data['profile_url']}")
    
    print("=" * 80)
    print(f"Total Experts: {len(experts_data)}")

if __name__ == "__main__":
    print("🔄 Creating comprehensive OddsHopper expert leaderboard...")
    leaderboard, experts_data = create_comprehensive_leaderboard()
    
    print("✅ Comprehensive data populated successfully!\n")
    
    # Display expert directory
    display_expert_directory(experts_data)
    
    print("\n\n📊 COMPREHENSIVE LEADERBOARD - ALL EXPERTS:")
    leaderboard.display_leaderboard(top_n=12)
    
    print("\n\n🔥 TOP PERFORMERS BY ROI:")
    leaderboard.display_leaderboard(sort_by="roi", top_n=12)
    
    print("\n\n💰 TOP UNIT EARNERS:")
    leaderboard.display_leaderboard(sort_by="units_profit", top_n=12)