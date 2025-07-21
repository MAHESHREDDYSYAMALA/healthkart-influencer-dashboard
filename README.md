**DASH BOARD LINK - http://localhost:8501/**
HealthKart Influencer Campaign Dashboard
Overview
This project is a data-driven dashboard to track and visualize the ROI of influencer marketing campaigns for HealthKart. It simulates influencer, post, tracking, and payout data, and provides an interactive dashboard for campaign analysis.

Features
Data Simulation:

Generates realistic sample data for influencers, posts, campaign tracking, and payouts using Python and Faker.
Outputs four CSV files: influencers.csv, posts.csv, tracking_data.csv, payouts.csv.
Modern Dashboard UI:

Built with Streamlit for a fast, interactive web experience.
Card-based summary metrics (Total Revenue, Payout, ROAS, Influencers).
Sidebar filters for platform and category.
Data tables for all entities.
Clean, modern styling.
Easy GitHub Integration:

Project structure and .gitignore ready for version control.
Data folder excluded from git to keep the repo clean.
Project Structure

healthkart-influencer-dashboard/
│
├── data/
│   ├── influencers.csv
│   ├── posts.csv
│   ├── tracking_data.csv
│   └── payouts.csv
│
├── app.py                # Streamlit dashboard
├── simulate_data.py      # Data simulation script
├── requirements.txt      # Python dependencies
├── .gitignore            # Excludes data/ from git
└── README.md             # Project instructions


How to Use
1. Clone the Repository
2. Install Dependencies
3. Generate Sample Data
This will create fresh CSVs in the data/ folder.
4. Run the Dashboard
Open http://localhost:8501 in your browser.
Data Files
influencers.csv:
ID, name, category, gender, follower_count, platform

posts.csv:
influencer_id, platform, date, URL, caption, reach, likes, comments

tracking_data.csv:
source, campaign, influencer_id, user_id, product, date, orders, revenue

payouts.csv:
influencer_id, basis, rate, orders, total_payout

Dashboard Highlights
Summary Cards:

Total Revenue, Total Payout, ROAS, Number of Influencers
Filters:

By platform (Instagram, YouTube, Twitter)
By category (Fitness, Nutrition, Lifestyle, Wellness)
Data Tables:

View and filter all influencer, post, tracking, and payout data
Sharing & Deployment
Share your dashboard locally via http://localhost:8501.
For public access, deploy to Streamlit Cloud or similar platforms.
Troubleshooting
Data not found?
Ensure you run simulate_data.py before starting the dashboard.
Dashboard not loading?
Make sure you run streamlit run app.py in the correct directory.
CSV/data issues?
Delete old CSVs and re-run the simulation script.
Credits
Built with Python, Streamlit, pandas, numpy, and Faker.
Designed for HealthKart influencer campaign analytics.
