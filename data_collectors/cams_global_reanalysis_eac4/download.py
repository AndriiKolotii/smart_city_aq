
import requests
import cdsapi

import datetime
import os

import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('--startdate', '-s', help='Start date in yyyy-mm-dd format')
parser.add_argument('--enddate', '-e', help='End date in yyyy-mm-dd format')

args=parser.parse_args()


sdate = list(map(int, args.startdate.split('-')))
edate = list(map(int, args.enddate.split('-')))


pollutants = ['carbon_monoxide', 'nitrogen_dioxide', 'nitrogen_monoxide', 'sulphur_dioxide',]

start_date = datetime.datetime(sdate[0],sdate[1],sdate[2])
end_date = datetime.datetime(edate[0],edate[1],edate[2])

c = cdsapi.Client()

while start_date != end_date+datetime.timedelta(days=1):
    date = start_date.strftime('%Y-%m-%d')
    print(str(start_date.strftime('%Y-%m-%d')))
    for pollutant in pollutants:
            c.retrieve(
                'cams-global-reanalysis-eac4',
                {
                'variable': pollutant,
                'model_level': '60',
                'date': '{}/{}'.format(str(start_date.strftime('%Y-%m-%d')), str(start_date.strftime('%Y-%m-%d'))),
                'time': [
                    '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00',
                ],
                'area': [
                    52.52, 21.84, 44.07, 40.52,],
                'format': 'netcdf',
                },
                '{}_{}.nc'.format(str(start_date.strftime('%Y-%m-%d')),pollutant))
    start_date += datetime.timedelta(days=1)
