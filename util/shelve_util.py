import shelve

'''
  object persistence
  object persistence / object serialization
  shelve
'''


def set_current_path(path):
    with shelve.open('don', writeback=True) as data:
        data['current_path'] = path
        return data['current_path']


def get_current_path():
    with shelve.open('don', writeback=True) as data:
        return data['current_path']
