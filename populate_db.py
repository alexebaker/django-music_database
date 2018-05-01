import os
import requests
import urllib3
import discogs_client
import dotenv
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dotenv.load_dotenv(os.path.join(BASE_DIR, 'auth', 'creds.env'))

username = 'musicdb'  # os.environ['DJANGO_DB_USERNAME']
password = 'changeme'  # os.environ['DJANGO_DB_PASSWORD']

api_url = "https://127.0.0.1:8000/api"


def main():
    sess = requests.session()
    sess.auth = (username, password)
    sess.verify = False
    #clear_db(sess); return
    dc = discogs_client.Client(requests.utils.default_user_agent(),
                               user_token=os.environ['DISCOGS_TOKEN'])
    artists = dc.search('', type='artist')
    for i in range(1, 190, 2):
        artist = artists.page(i)[0]
        artist_name = re.sub(r'[^\x00-\x7f]', r'_', artist.name)
        print(artist_name, i)
        artist_json = {'name': artist_name}
        artist_data = sess.post('%s/artist/' % api_url, json=artist_json).json()

        for release in artist.releases:
            release_title = re.sub(r'[^\x00-\x7f]', r'_', release.title)
            genre_ids = []
            api_genres = sess.get('%s/genre/' % api_url).json()
            if release.genres:
                for genre in release.genres:
                    genre_id = None
                    for g in api_genres:
                        if genre == g['name']:
                            genre_id = g['id']
                            break

                    if not genre_id:
                        genre_id = sess.post('%s/genre/' % api_url, json={'name': genre}).json()['id']

                    genre_ids.append(genre)

            style_ids = []
            api_styles = sess.get('%s/style/' % api_url).json()
            if release.styles:
                for style in release.styles:
                    style_id = None
                    for s in api_styles:
                        if style == s['name']:
                            style_id = s['id']
                            break

                    if not style_id:
                        style_id = sess.post('%s/style/' % api_url, json={'name': style}).json()['id']

                    style_ids.append(style)

            try:
                year = release.year
            except AttributeError:
                year = '0000'
            album_json = {'title': release_title,
                          'year': year,
                          'artist': artist_data['id'],
                          'genres': genre_ids,
                          'styles': style_ids}

            album_data = sess.post('%s/album/' % api_url, json=album_json).json()

            image_uri = ""
            if release.images:
                for image in release.images:
                    if image['type'] == 'primary':
                        image_uri = image['resource_url']
                        break

            if image_uri:
                with open('/tmp/art.jpg', 'wb') as f:
                    r = requests.get(image_uri, stream=True)
                    for chunk in r.iter_content():
                        f.write(chunk)
                with open('/tmp/art.jpg', 'rb') as f:
                    imgname = '%s-%s-albumart.jpg' % (re.sub(r'[\\/*?:"<>| ]', '', artist_name), re.sub(r'[\\/*?:"<>| ]', '', release_title))
                    sess.post('%s/albumart/' % api_url,
                              files={'image': (imgname, f, 'image/jpeg')},
                              headers={'Content-Disposition': 'attachment; filename=%s' % imgname},
                              data={'album': album_data['id']})

            for track in release.tracklist:
                track_title = re.sub(r'[^\x00-\x7f]', r'_', track.title)
                duration = track.duration
                if len(track.duration.split(":")) < 3:
                    duration = '00:' + duration
                track_json = {'title': track_title,
                              'duration': duration,
                              'position': track.position,
                              'album': album_data['id']}
                sess.post('%s/track/' % api_url, json=track_json)
    return


def clear_db(sess):
    artists = sess.get('%s/artist/' % api_url).json()
    for artist in artists:
        sess.delete('%s/artist/%s/' % (api_url, artist['id']))
    return


if __name__ == '__main__':
    main()
