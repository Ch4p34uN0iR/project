import requests, sys, re, gi
from datetime import datetime
gi.require_version('Notify', '0.7')
from gi.repository import Notify
try:
    # from twilio.rest import TwilioRestClient
    from bs4 import BeautifulSoup
except ImportError as error:
    print('[!] Uh-oh: {}'.format(error))

account_sid = ''
auth_token = ''

# mdKey from your email will go right hurr
mdKey = ''
dateList = ''
payload = {'md': mdKey}

def writingData(filename, datelist):
    with open(filename, 'w') as file:
        file.write(datelist)

def readingData(calenDateFile):
    with open(calenDateFile, 'r') as file:
        return set(file)

def desktopNotification(title, message):
    Notify.init('script')
    Notify.Notification.new(title, message).show()

def sendText(message):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to='',          # Your number
        from_='',       # Your Twilio number
        body='Good news! {} is now available! Book now before time runs out!')

def main():
    print('[+] Gathering dates')
    resp = requests.get('https://www.offensive-security.com/exam.php', params=payload)

    soup = BeautifulSoup(resp.content, 'lxml')
    print('[+] The following dates are available:')
    for link in soup.findAll('a', href=True):
        if 'exam' in link['href']:
            date = re.search(r'\d{4}-\d{2}-\d{2}', link['href']).group()
            date = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
            dateList += '{}\n'.format(date)
            print('\t{}'.format(date))

    firstCheck = os.path.isfile('available.txt')
    secondCheck = os.path.isfile('available2.txt')
    if firstCheck == True:
        if secondCheck == True:
            print 'is here'
            if available != available2:
                firstCheck2 = readingData('available.txt')
                secondCheck2 = readingData('available2.txt')
                newDates = ''
                for dates in secondCheck2:
                    if dates not in firstCheck2:
                        newDates += dates
                        print '{} is available. get while you can!'.format(dates)
                desktopNotification('New Dates Available!', newDates)
                writingData('available.txt', dateList)      # Will fix dateList later. Tired af
        else:
            print 'is not here'
            
        print 'second'
    else:
        writingData('available.txt', dateList)
        desktopNotification('Available', dateList)

if __name__ == '__main__':
    if len(mdKey) == 0:
        print('[!] You need to input your unique id! '
              '\n[!] You can find it in your personalized email')
        sys.exit()
    main()
