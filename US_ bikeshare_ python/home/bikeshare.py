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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print(' ')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Enter the city you want to analyze the data from the following cities:')
    print('Chicago: 1')
    print('New York: 2')
    print('Washington: 3')
    print(' ')
    city = input('Please choose the city for which you would like to see the Statistics: ')
    city = city.lower()
    while True:
       if city == '1' or city == 'chicago':
          print("\n You have selected Chicago City! Okay Let's go further\n")
          city = 'chicago'
          break

       elif city == '2' or city == 'new york':
          print("\n You have selected New York City! Okay let's go further\n")
          city= 'new york city'
          break
       elif city == '3' or city == 'washington':
          print("\n You have selected Washington! Okay let's go further\n")
          city= 'washington'
          break
       else:
           print ('Enter the correct  city you want to analyze the data')
           city = input('Please choose the city for which you would like to see the Statistics: ')
           city = city.lower()
        #goto check


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month??  Please type the full month name.\n')
    while month.strip().lower() not in ['january', 'february', 'march', 'april', 'may', 'june','july','august',' september','october','november','december']:
        month = input('\nPlease choose between January, February, March, April, May, or June? Please type the full month name.\n')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day? Please enter an integer (e.g., 1=sunday) \n')
    while day.strip() not in ['1', '2', '3', '4', '5', '6', '7']:
        day = input('\nWhich day? Please enter an integer (e.g., 1=sunday) \n')


    print('-'*40)
    return city,  month.strip().lower(), day.lower().strip()


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
    print('\nLoading the data... .. .. ..\n')
    df = pd.read_csv(CITY_DATA[city])

    #extracting from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day

    print('Data loaded. Now computing statistics... \n')
    #Filter by Month
    if month == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august',' september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Filter by day of week
    if day == 'day_of_week':
        days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]

    if day == "day_of_month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = md[0]
        month = months.index(month) + 1
        df = df[df['month']==month]
        day = md[1]
        df = df[df['day_of_month'] == day]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\n Calculating the statistic.. most popular month ...')
    m = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august',' september','october','november','december']
    popular_month = months[m - 1].capitalize()
    print(popular_month)

    # TO DO: display the most common day of week
    print('\nCalculating the statistic.. most popular day of the week..')
    popular_day = df['day_of_week'].value_counts().reset_index()['index'][0]
    print(popular_day)

    # TO DO: display the most common start hour
    print('\n Calculating the statistic.. most popular hour of the day ..')
    df['hour'] = df['Start Time'].dt.hour
    print(df.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\n Calculating the statistic.. most popular start station..\n")
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]

    print (start_station)

    # TO DO: display most commonly used end station
    print("\n Calculating the statistic.. most popular end station..\n")
    end_station = df['End Station'].value_counts().reset_index()['index'][0]

    print(end_station)

    # TO DO: display most frequent combination of start station and end station trip
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\n Calculating the statistic..  most popular trip from start to end is {}'.format(result))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating the statistic.. Trip Duration...\n')
    start_time = time.time()
    print('\n What was the total traveling done  and what was the average time spent on each trip?')
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    # TO DO: display total travel time
    total_ride_time = np.sum(df['Travel Time'])
    total_days = str(total_ride_time).split()[0]

    print ("\nThe total travel time in 2017 upto June was " +str(total_ride_time) + "  \n")
    # TO DO: display mean travel time
    avg_ride_time = np.mean(df['Travel Time'])
    avg_days = str(avg_ride_time).split()[0]
    print("The average travel time in 2017 upto June was " + str(avg_ride_time) + "  \n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statistics...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n Types of users: subscribers, customers, others\n')
    print( df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('\n What is the breakdown of gender among users?\n')
        print( df['Gender'].value_counts())
    except:
        print('There is no gender data in the source.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\n What is the earliest, latest, and most frequent year of birth, respectively?')
        earliest = np.min(df['Birth Year'])
        print ("\n Earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("Latest year of birth is " + str(latest) + "\n")
        most_frequent= df['Birth Year'].mode()[0]
        print ("Most frequent year of birth is " + str(most_frequent) + "\n")

    except:
        print('No available birth date data for this period.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def disp_raw_data(df):
    '''
    Displays the data used to compute the stats
    Input:
        the df with all the bikeshare data
    Returns:
       none
    '''
    #omit irrelevant columns from visualization
    df = df.drop(['month', 'day_of_month'], axis = 1)
    row_index = 0

    see_data = input("\nYou like to see rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()