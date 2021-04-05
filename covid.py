import requests
from lifxlan import Light


def get_covid_data(yesterday=False, two_days_ago=False):
    payload = {
        'yesterday': 'true' if yesterday else 'false',
        'twoDaysAgo': 'true' if two_days_ago else 'false',
    }

    r = requests.get('https://disease.sh/v3/covid-19/all', params=payload)
    data = r.json()
    return data


def main():
    blastoise = Light("d0:73:d5:64:f7:cf", "192.168.86.26")
    print(blastoise)

    yesterday_data = get_covid_data(yesterday=True)
    two_days_ago_data = get_covid_data(two_days_ago=True)
    yesterday_cases = yesterday_data['todayCases']
    two_days_ago_cases = two_days_ago_data['todayCases']

    print('yesterday:', yesterday_cases)
    print('two days ago:', two_days_ago_cases)

    blastoise.set_power('on')
    blastoise.set_brightness(3000)
    blastoise.set_saturation(55000)

    if yesterday_cases < two_days_ago_cases:
        print('green')
        blastoise.set_hue(16173, 1000)
    elif yesterday_cases > two_days_ago_cases:
        print('red')
        blastoise.set_hue(65535, 1000)
    else:
        print('blue')
        blastoise.set_hue(29814, 1000)


if __name__ == '__main__':
    main()
