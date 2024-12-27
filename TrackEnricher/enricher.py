from TrackEnricher.utils import getTrackId, csv_to_dict

d = csv_to_dict(r'E:\Projects\SpotifyMetricsFetcher\downloads\regional-il-weekly-2022-01-06.csv')
print(getTrackId(d[0]))