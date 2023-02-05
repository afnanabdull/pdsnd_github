import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#This script is used to to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    print('This will include only three major US cities: new_york_city, Chicago, and washington')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
       city = input("Please enter your desired city name: new york city, Chicago, or Washington\n").lower()
       if city not in ['chicago', 'new york city', 'washington']:
          print("We are only exploring the above 3 cities, we will explore more in the future.")
          continue
       else:
          break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Please enter your desired month between January and June, or simply enter all\n").lower() 
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
           print("Your input was not valid, we are only looking at months between Jan and June")
           continue
        else:
           break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Please enter your desired day of the week, or simply enter all\n ").lower() 
        if day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
           print("Your input was not valid")
           continue
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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    if month != 'all':
           months = ['january', 'february', 'march', 'april', 'may', 'june']
           month = months.index(month) + 1
           df = df[df['month'] == month]

    if day != 'all':
           days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
           day = days.index(day) + 1
           df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print('The most popular Month of the year is :', df['month'].mode()[0])

    # TO DO: display the most common day of week

    print('The most popular Day of the week is :', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    print('The Most popular Hour of the day is :', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    M_C_Start_Station = df['Start Station'].value_counts().idxmax()
    print('The most popular start station is :', M_C_Start_Station)


    # TO DO: display most commonly used end station

    M_C_End_Station = df['End Station'].value_counts().idxmax()
    print('The most popular end station is :', M_C_End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combo_Stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most popular combination of start station and end station is :', M_C_Start_Station, " and ", M_C_End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel = df['Trip Duration'].sum()
    print('The total trip time is :', Total_Travel / 3600)


    # TO DO: display mean travel time

    Mean_Travel = df['Trip Duration'].mean()
    print('The mean trip time is :', Mean_Travel / 3600)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('The counts of user types are : ', df['User Type'].value_counts())

    # TO DO: Display counts of gender

    try:
       print('The counts of gender is : ', df['Gender'].value_counts())
    except KeyError:
        print('No Data for your selection')

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
       print('The moset earliest year of birth is :', df['Birth Year'].min())
    except KeyError:
        print('No Data for your selection')
    
    try:
        print('The most recent year of birth is :', df['Birth Year'].max())
    except KeyError:
        print('No Data for your selection')
    
    try:
        print('\nMost Common Year:', df['Birth Year'].value_counts().idxmax())
    except KeyError:
        print('No Data for your selection')

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # To ask the user whether he wants to see 5 rows of data. This will keep showing the next 5 rows as long as the user says yes 
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    end_loc = 5
    while start_loc < len(df.index): 
        if view_data.lower() == 'yes':
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
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