import os

root_dir = os.path.dirname(__file__)
source = os.path.join(root_dir, 'lists')
destination = os.path.join(root_dir, 'merged-list.txt')

def banner(name):
    return '''! ########################
! List: {}
! ########################
'''.format(name)

def merge_file_content(dest_handle, filepath):
    print('> merging file: {}'.format(filepath))
    with open(filepath, 'r') as fh:
        dest_handle.write(
            banner(os.path.basename(filepath))
        )
        dest_handle.write(fh.read().strip())
        fh.close()
    dest_handle.write('\n\n')

def source_filelist():
    files = []
    for file in os.listdir(source):
        files.append(
            os.path.join(source, file)
        )
    return files

def truncate_destination():
    with open(destination, 'w') as fh:
        fh.truncate(0)
        fh.close()

def merge_files():
    with open(destination, 'a') as dh:
        for file in source_filelist():
            merge_file_content(dh, file)
        dh.close()

def main():
    print('Merging lists...')
    truncate_destination()
    merge_files()
    print('done.')

if __name__ == '__main__':
    main()
