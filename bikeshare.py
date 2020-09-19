import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! This is the US Bikeshare Analytics Program.'')
    print('Let\'s explore some bikeshare data!')

    while True:
        city = input("Enter the name of the city you want to explore the bikeshare data from: ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("\nOoops. That is not a valid city name.\n")
            print("Please enter a valid city name.\n")
        else:
            break

    while True:
            month = input("Enter the month you would like to analyze. (January - June, or enter 'all' for all month with existing data): ").lower()
            if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                print("\nOoops. That is not a valid month.\n")
                print("Please enter a valid month.\n")
            else:
                break

    while True:
        day = input("Enter the weekday you would like to analyze. (Monday - Sunday, or enter 'all' for the whole week): ").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("\nOoops. That is not a weekday.\n")
            print("Please enter a weekday.\n")
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nThe most common day is', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\nThe most common hour is', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station is:', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start station and end station trip is:\n')
    print(df.groupby(['Start Station', 'End Station']).size().reset_index(name="Times").sort_values(by='Times',ascending=False).head(1).iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is:', df['Trip Duration'].max())

    # TO DO: display mean travel time
    print('\nThe mean travel time is:\n', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('List with counts of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nList with counts of gender:\n', df['Gender'].value_counts())
    else:
        print('\nNo data about gender in data set found.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nList of information about earlist, most recent and most common year of birth:\n')
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        print('Most common year of birth:', df['Birth Year'].mode())
    else:
        print('No data about birth year in data set found.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes for displaying data.\n').lower()
    start_loc = 0
    while view_data == "yes":
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? For exiting enter no: ").lower()
        if view_display == "no":
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
