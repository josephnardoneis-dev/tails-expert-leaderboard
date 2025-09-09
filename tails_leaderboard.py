#!/usr/bin/env python3
"""
Tails Expert Leaderboard System
Tracks and ranks betting experts from OddsHopper based on their pick performance
"""

import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import sqlite3
from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup
import re

@dataclass
class Pick:
    pick_id: str
    expert_name: str
    sport: str
    game: str
    bet_type: str
    selection: str
    odds: str
    date: str
    result: Optional[str] = None  # 'win', 'loss', 'push', 'pending'
    units_risked: float = 1.0
    units_won: float = 0.0

@dataclass
class ExpertStats:
    name: str
    total_picks: int
    wins: int
    losses: int
    pushes: int
    win_percentage: float
    units_profit: float
    roi: float
    last_10_record: str
    current_streak: str
    best_sport: str

class TailsLeaderboard:
    def __init__(self, db_path: str = "tails_leaderboard.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS picks (
                pick_id TEXT PRIMARY KEY,
                expert_name TEXT,
                sport TEXT,
                game TEXT,
                bet_type TEXT,
                selection TEXT,
                odds TEXT,
                date TEXT,
                result TEXT,
                units_risked REAL,
                units_won REAL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS experts (
                name TEXT PRIMARY KEY,
                total_picks INTEGER,
                wins INTEGER,
                losses INTEGER,
                pushes INTEGER,
                win_percentage REAL,
                units_profit REAL,
                roi REAL,
                last_updated TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_pick(self, pick: Pick):
        """Add a new pick to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO picks 
            (pick_id, expert_name, sport, game, bet_type, selection, odds, date, result, units_risked, units_won)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            pick.pick_id, pick.expert_name, pick.sport, pick.game,
            pick.bet_type, pick.selection, pick.odds, pick.date,
            pick.result, pick.units_risked, pick.units_won
        ))
        
        conn.commit()
        conn.close()
    
    def update_pick_result(self, pick_id: str, result: str, units_won: float = 0.0):
        """Update the result of a pick"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE picks 
            SET result = ?, units_won = ? 
            WHERE pick_id = ?
        """, (result, units_won, pick_id))
        
        conn.commit()
        conn.close()
    
    def calculate_expert_stats(self, expert_name: str) -> ExpertStats:
        """Calculate comprehensive stats for an expert"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM picks 
            WHERE expert_name = ? AND result IS NOT NULL
            ORDER BY date DESC
        """, (expert_name,))
        
        picks = cursor.fetchall()
        conn.close()
        
        if not picks:
            return ExpertStats(
                name=expert_name, total_picks=0, wins=0, losses=0, pushes=0,
                win_percentage=0.0, units_profit=0.0, roi=0.0,
                last_10_record="0-0", current_streak="", best_sport=""
            )
        
        total_picks = len(picks)
        wins = sum(1 for pick in picks if pick[8] == 'win')
        losses = sum(1 for pick in picks if pick[8] == 'loss')
        pushes = sum(1 for pick in picks if pick[8] == 'push')
        
        win_percentage = (wins / total_picks * 100) if total_picks > 0 else 0
        units_profit = sum(pick[10] for pick in picks) - sum(pick[9] for pick in picks)
        total_risked = sum(pick[9] for pick in picks)
        roi = (units_profit / total_risked * 100) if total_risked > 0 else 0
        
        # Last 10 record
        last_10 = picks[:10]
        last_10_wins = sum(1 for pick in last_10 if pick[8] == 'win')
        last_10_losses = sum(1 for pick in last_10 if pick[8] == 'loss')
        last_10_record = f"{last_10_wins}-{last_10_losses}"
        
        # Current streak
        current_streak = self._calculate_streak(picks)
        
        # Best sport
        sport_stats = {}
        for pick in picks:
            sport = pick[2]
            if sport not in sport_stats:
                sport_stats[sport] = {'wins': 0, 'total': 0}
            sport_stats[sport]['total'] += 1
            if pick[8] == 'win':
                sport_stats[sport]['wins'] += 1
        
        best_sport = max(sport_stats.items(), 
                        key=lambda x: x[1]['wins']/x[1]['total'] if x[1]['total'] > 0 else 0,
                        default=("", {"wins": 0, "total": 0}))[0]
        
        return ExpertStats(
            name=expert_name,
            total_picks=total_picks,
            wins=wins,
            losses=losses,
            pushes=pushes,
            win_percentage=round(win_percentage, 1),
            units_profit=round(units_profit, 2),
            roi=round(roi, 1),
            last_10_record=last_10_record,
            current_streak=current_streak,
            best_sport=best_sport
        )
    
    def _calculate_streak(self, picks: List) -> str:
        """Calculate current win/loss streak"""
        if not picks:
            return ""
        
        current_result = picks[0][8]
        if current_result not in ['win', 'loss']:
            return ""
        
        streak = 1
        for pick in picks[1:]:
            if pick[8] == current_result:
                streak += 1
            else:
                break
        
        streak_type = "W" if current_result == 'win' else "L"
        return f"{streak_type}{streak}"
    
    def get_leaderboard(self, sort_by: str = "win_percentage") -> List[ExpertStats]:
        """Get leaderboard sorted by specified metric"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT DISTINCT expert_name FROM picks")
        experts = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        expert_stats = []
        for expert in experts:
            stats = self.calculate_expert_stats(expert)
            if stats.total_picks >= 5:  # Only include experts with at least 5 picks
                expert_stats.append(stats)
        
        # Sort by specified metric
        if sort_by == "win_percentage":
            expert_stats.sort(key=lambda x: x.win_percentage, reverse=True)
        elif sort_by == "units_profit":
            expert_stats.sort(key=lambda x: x.units_profit, reverse=True)
        elif sort_by == "roi":
            expert_stats.sort(key=lambda x: x.roi, reverse=True)
        elif sort_by == "total_picks":
            expert_stats.sort(key=lambda x: x.total_picks, reverse=True)
        
        return expert_stats
    
    def display_leaderboard(self, sort_by: str = "win_percentage", top_n: int = 10):
        """Display formatted leaderboard"""
        leaderboard = self.get_leaderboard(sort_by)[:top_n]
        
        print(f"\n🏆 TAILS EXPERT LEADERBOARD - TOP {top_n}")
        print("=" * 100)
        print(f"{'Rank':<4} {'Expert':<20} {'Record':<12} {'Win%':<6} {'Units':<8} {'ROI%':<6} {'L10':<6} {'Streak':<8} {'Best Sport':<12}")
        print("-" * 100)
        
        for i, expert in enumerate(leaderboard, 1):
            record = f"{expert.wins}-{expert.losses}-{expert.pushes}"
            units = f"+{expert.units_profit}" if expert.units_profit >= 0 else str(expert.units_profit)
            roi = f"+{expert.roi}%" if expert.roi >= 0 else f"{expert.roi}%"
            
            print(f"{i:<4} {expert.name:<20} {record:<12} {expert.win_percentage}%{'':<1} {units:<8} {roi:<6} {expert.last_10_record:<6} {expert.current_streak:<8} {expert.best_sport:<12}")
        
        print("=" * 100)
        print(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def populate_sample_data():
    """Populate the leaderboard with sample data based on OddsHopper experts"""
    leaderboard = TailsLeaderboard()
    
    sample_picks = [
        Pick("1", "Mikey's Mashers", "College Football", "Florida vs LSU", "Spread", "Florida +9.5", "-110", "2024-09-07", "win", 1.0, 1.91),
        Pick("2", "Mikey's Mashers", "MLB", "Pirates vs Orioles", "Total", "Under 8.5", "-105", "2024-09-07", "loss", 1.0, 0.0),
        Pick("3", "Mikey's Mashers", "NFL", "Xavier Worthy Props", "Player Prop", "Over 3.5 Receptions", "+120", "2024-09-08", "win", 1.0, 2.20),
        Pick("4", "Greg Ehrenberg", "MLB", "Noah Cameron Props", "Player Prop", "Over 5.5 K's", "-115", "2024-09-07", "win", 1.0, 1.87),
        Pick("5", "MoneyBadgerJake", "MLB", "Reds vs Cardinals", "Moneyline", "Reds F5 ML", "+105", "2024-09-07", "loss", 1.0, 0.0),
        Pick("6", "Supreme Juice", "NFL", "DJ Moore Props", "Player Prop", "Over 65.5 Rec Yards", "-110", "2024-09-08", "win", 1.0, 1.91),
        Pick("7", "Mike10693", "WNBA", "Storm vs Liberty", "Spread", "Storm +4.5", "-108", "2024-09-07", "win", 1.0, 1.93),
    ]
    
    for pick in sample_picks:
        leaderboard.add_pick(pick)
    
    return leaderboard

if __name__ == "__main__":
    leaderboard = populate_sample_data()
    leaderboard.display_leaderboard()
    
    print("\n\n🔥 TOP PERFORMERS BY ROI:")
    leaderboard.display_leaderboard(sort_by="roi", top_n=5)
    
    print("\n\n💰 TOP UNIT EARNERS:")
    leaderboard.display_leaderboard(sort_by="units_profit", top_n=5)