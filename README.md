# 🏆 Tails Expert Leaderboard

A comprehensive leaderboard system for tracking sports betting experts from OddsHopper, featuring real-time statistics, historical performance data, and professional web interface.

## 🚀 Features

- **Expert Performance Tracking**: Win/loss records, streaks, ROI, units profit
- **Multi-Sport Coverage**: NFL, MLB, College Football, WNBA, and more
- **Advanced Analytics**: Win percentage, ROI, last 10 games, current streaks
- **Flexible Sorting**: Sort by win percentage, units profit, ROI, or total picks
- **Professional Web Interface**: Responsive design with real-time statistics
- **SQLite Database**: Persistent data storage with easy querying
- **Extensible Design**: Easy to add new experts and betting data

## 📊 Current Leaderboard Top 5

| Rank | Expert | Record | Win% | Units | ROI% | Streak |
|------|--------|--------|------|-------|------|--------|
| 1 | Greg Ehrenberg | 12-3-1 | 75.0% | +8.05 | +50.3% | W3 |
| 2 | Supreme Juice | 9-4-0 | 69.2% | +4.06 | +31.3% | W3 |
| 3 | Mikey's Mashers | 10-5-0 | 66.7% | +4.56 | +30.4% | W3 |
| 4 | Mike10693 | 8-4-0 | 66.7% | +3.70 | +30.9% | W2 |
| 5 | MoneyBadgerJake | 9-7-0 | 56.2% | +1.40 | +8.8% | L2 |

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tails-expert-leaderboard.git
cd tails-expert-leaderboard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the leaderboard system:
```bash
python3 scrape_experts.py
```

4. Open the web interface:
```bash
open leaderboard_web.html
```

## 🔧 Usage

### Command Line Interface

**Display Main Leaderboard:**
```bash
python3 tails_leaderboard.py
```

**Load Sample Data:**
```bash
python3 scrape_experts.py
```

### Python API

```python
from tails_leaderboard import TailsLeaderboard, Pick

# Initialize leaderboard
leaderboard = TailsLeaderboard()

# Add a new pick
pick = Pick(
    pick_id="unique_id",
    expert_name="Expert Name",
    sport="NFL",
    game="Team A vs Team B",
    bet_type="Spread",
    selection="Team A -3.5",
    odds="-110",
    date="2024-09-09",
    result="win",
    units_risked=1.0,
    units_won=1.91
)
leaderboard.add_pick(pick)

# Display leaderboard
leaderboard.display_leaderboard(sort_by="win_percentage")
```

## 📁 Project Structure

```
tails-expert-leaderboard/
├── tails_leaderboard.py      # Core leaderboard system
├── scrape_experts.py         # Data population script
├── leaderboard_web.html      # Web interface
├── tails_leaderboard.db      # SQLite database (auto-created)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🏗️ Database Schema

### Picks Table
- `pick_id` (TEXT PRIMARY KEY): Unique identifier for each pick
- `expert_name` (TEXT): Name of the betting expert
- `sport` (TEXT): Sport category (NFL, MLB, etc.)
- `game` (TEXT): Game matchup details
- `bet_type` (TEXT): Type of bet (Spread, Total, Moneyline, etc.)
- `selection` (TEXT): Specific bet selection
- `odds` (TEXT): Betting odds
- `date` (TEXT): Date of the pick
- `result` (TEXT): Outcome (win/loss/push/pending)
- `units_risked` (REAL): Units risked on the bet
- `units_won` (REAL): Units won from the bet

### Experts Table
- `name` (TEXT PRIMARY KEY): Expert name
- `total_picks` (INTEGER): Total number of picks
- `wins/losses/pushes` (INTEGER): Win/loss/push counts
- `win_percentage` (REAL): Win percentage
- `units_profit` (REAL): Total units profit
- `roi` (REAL): Return on investment percentage
- `last_updated` (TEXT): Last update timestamp

## 📈 Metrics Explained

- **Win%**: Percentage of winning picks
- **Units**: Profit/loss in betting units (typically $100 each)
- **ROI**: Return on investment percentage
- **L10**: Record over last 10 picks
- **Streak**: Current winning or losing streak

## 🌐 Deployment to Render

This project is ready for deployment to Render:

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use Python environment
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python3 -m http.server 8000`

## 🔮 Future Enhancements

- [ ] Live data scraping from OddsHopper API
- [ ] Real-time bet result verification
- [ ] Email notifications for expert picks
- [ ] Advanced filtering by sport/date range
- [ ] Export functionality (CSV, JSON)
- [ ] Mobile app integration
- [ ] Social sharing features
- [ ] Betting bankroll management tools

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Data sourced from [OddsHopper Expert Picks](https://www.oddsshopper.com/expert-picks/free)
- Built with Python, SQLite, and modern web technologies
- Designed for the sports betting community

## 📞 Support

For questions or support, please open an issue on GitHub or contact the development team.

---

**Disclaimer**: This tool is for educational and entertainment purposes. Please gamble responsibly and within your means.