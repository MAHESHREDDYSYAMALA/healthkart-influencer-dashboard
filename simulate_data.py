import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

def simulate_influencers(n=20):
    categories = ['Fitness', 'Nutrition', 'Lifestyle', 'Wellness']
    genders = ['Male', 'Female', 'Other']
    platforms = ['Instagram', 'YouTube', 'Twitter']
    data = []
    for i in range(1, n+1):
        data.append({
            'ID': i,
            'name': fake.name(),
            'category': random.choice(categories),
            'gender': random.choice(genders),
            'follower_count': random.randint(10000, 1000000),
            'platform': random.choice(platforms)
        })
    return pd.DataFrame(data)

def simulate_posts(influencers, n=100):
    data = []
    for _ in range(n):
        influencer = influencers.sample(1).iloc[0]
        date = fake.date_between(start_date='-90d', end_date='today')
        data.append({
            'influencer_id': influencer['ID'],
            'platform': influencer['platform'],
            'date': date,
            'URL': fake.url(),
            'caption': fake.sentence(),
            'reach': random.randint(5000, influencer['follower_count']),
            'likes': random.randint(100, 10000),
            'comments': random.randint(10, 1000)
        })
    return pd.DataFrame(data)

def simulate_tracking_data(influencers, n=200):
    brands = ['MuscleBlaze', 'HKVitals', 'Gritzo']
    products = ['Protein', 'Vitamins', 'Shaker', 'Mass Gainer']
    data = []
    for _ in range(n):
        influencer = influencers.sample(1).iloc[0]
        date = fake.date_between(start_date='-90d', end_date='today')
        orders = random.randint(1, 20)
        revenue = orders * random.uniform(500, 3000)
        data.append({
            'source': 'influencer',
            'campaign': random.choice(brands) + ' ' + random.choice(products),
            'influencer_id': influencer['ID'],
            'user_id': fake.uuid4(),
            'product': random.choice(products),
            'date': date,
            'orders': orders,
            'revenue': round(revenue, 2)
        })
    return pd.DataFrame(data)

def simulate_payouts(influencers, posts, tracking_data):
    data = []
    for _, influencer in influencers.iterrows():
        basis = random.choice(['post', 'order'])
        if basis == 'post':
            rate = random.randint(2000, 20000)
            n_posts = posts[posts['influencer_id'] == influencer['ID']].shape[0]
            total_payout = rate * n_posts
            orders = np.nan
        else:
            rate = random.randint(100, 1000)
            orders = tracking_data[tracking_data['influencer_id'] == influencer['ID']]['orders'].sum()
            total_payout = rate * orders
            n_posts = np.nan
        data.append({
            'influencer_id': influencer['ID'],
            'basis': basis,
            'rate': rate,
            'orders': orders,
            'total_payout': total_payout
        })
    return pd.DataFrame(data)

if __name__ == '__main__':
    data_dir = 'E:/PROJECCTS/healthkart-influencer-dashboard/data'
    os.makedirs(data_dir, exist_ok=True)
    influencers = simulate_influencers()
    posts = simulate_posts(influencers)
    tracking_data = simulate_tracking_data(influencers)
    payouts = simulate_payouts(influencers, posts, tracking_data)

    influencers.to_csv(os.path.join(data_dir, 'influencers.csv'), index=False)
    posts.to_csv(os.path.join(data_dir, 'posts.csv'), index=False)
    tracking_data.to_csv(os.path.join(data_dir, 'tracking_data.csv'), index=False)
    payouts.to_csv(os.path.join(data_dir, 'payouts.csv'), index=False)
    print('Simulated data saved to data/*.csv')

## How to Run the Dashboard

1. Clone the repository:
2. Install dependencies:
3. Generate sample data:
4. Run the dashboard:
5. Open the local URL (usually http://localhost:8501) in your browser to view the dashboard.

streamlit
pandas
faker
