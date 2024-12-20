import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Ensuring using Agg backend to avoid Tkinter errors if running in environments without GUI support
matplotlib.use('Agg')

# Loading the dataset 
data = pd.read_csv('roulette_10000_rounds.csv')  # Replace with the correct path to your dataset

# Check if the dataset is loaded correctly
print(data.head())  # This will show the first few rows of the dataset
print(data.columns)  # This will print all column names

# Frequency of each Winning Number
outcome_counts = data['Winning Number'].value_counts()

# Plotting the frequency of each roulette number (Bar chart)
plt.figure(figsize=(10, 6))
sns.barplot(x=outcome_counts.index, y=outcome_counts.values, hue=outcome_counts.index)
plt.title('Frequency of Roulette Numbers')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.savefig('roulette_number_frequency.png')  # Save the plot as a PNG image
plt.close()

# Count of Red vs Black vs Green outcomes
color_counts = data['Winning Color'].value_counts()

# Plot the distribution of Red, Black and Green outcomes in Pie chart
plt.figure(figsize=(8, 8))
plt.pie(color_counts.values, labels=color_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Red and Black Outcomes')
plt.savefig('color_distribution.png')  # Save the plot as a PNG image
plt.close()


# Flat betting strategy simulation (Example: Flat bet $10 on Red for each round)
starting_balance = 1000  # Initial balance
bet_amount = 10
balance = starting_balance

# Simulated outcomes from Red Bet Win column
outcomes = data['Red Bet Win']

for outcome in outcomes:
    if outcome == 1:  # Win on Red
        balance += bet_amount
    else:  # Loss on Red
        balance -= bet_amount

print(f"Final Balance after Flat Betting on Red: ${balance}")

# Martingale strategy simulation (Doubling the bet after a loss, Red Bet)
starting_balance = 1000  # Initial balance
bet_amount = 10
balance = starting_balance

for outcome in outcomes:
    if outcome == 1:  # Win on Red
        balance += bet_amount
        bet_amount = 10  # Reset bet after win
    else:  # Loss on Red
        balance -= bet_amount
        bet_amount *= 2  # Double the bet after a loss

print(f"Final Balance after Martingale Strategy on Red: ${balance}")

# Plot the balance over time for Martingale strategy
balances = []
bet_amount = 10
balance = starting_balance

for outcome in outcomes:
    if outcome == 1:  # Win on Red
        balance += bet_amount
        bet_amount = 10  # Reset bet after win
    else:  # Loss on Red
        balance -= bet_amount
        bet_amount *= 2  # Double the bet after a loss
    balances.append(balance)

# Plotting the balance over time
plt.plot(balances)
plt.title('Balance Over Time (Martingale Strategy on Red)')
plt.xlabel('Round Number')
plt.ylabel('Balance')
plt.savefig('martingale_balance_over_time.png')  # Save the plot as a PNG image
plt.close()

# Inform user of saved files
print("Plots saved as 'roulette_number_frequency.png', 'color_distribution.png', and 'martingale_balance_over_time.png'")
