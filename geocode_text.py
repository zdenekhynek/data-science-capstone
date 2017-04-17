import geocoder


def geocode_text(text):
    g = geocoder.google(text)
    return g.latlng


if __name__ == '__main__':
    print geocode_text('Mountain View, CA')
