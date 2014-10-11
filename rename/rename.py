import click

@click.command()
@click.option('-d', '--directory', default='.',
              type=click.Path(exists=True, writable=True, resolve_path=True),
              help='Directory to perform search')
@click.option('-p', '--pattern', default='.*',
              help='Regex pattern to match files with')
@click.option('-t', '--target', default='\(index)',
              help='Regex pattern to replace files with')
@click.option('-r', '--replace', default=False, type=click.BOOL,
              help='Boolean to replace files')
def rename(directory, pattern, target, replace):
    
    import os
    import re
    import shutil
    print 'Matching in directory: %s' % directory
    print 'Matching file pattern: %s' % pattern
    print 'Target file pattern: %s' % target
    print '------------------------'

    os.chdir(directory)
    all_files = os.listdir(directory)
    files = [f for f in all_files if re.search(pattern, f)]
    
    for i, filename in enumerate(files):
        tar = re.sub(r'\\\(index\)', str(i), target)
        replacement = re.sub(pattern, tar, filename)
        
        if replace:
            print 'Renaming %s to %s' % (filename, replacement)
            os.rename(filename, replacement)
        else:
            print 'Copying %s to %s' % (filename, replacement)
            shutil.copyfile(filename, replacement)
        

# import os
# import sys
# import datetime
# target = os.path.dirname(os.path.realpath(__file__))
# script_name = os.path.basename(sys.argv[0])
# os.chdir(target)
# allfiles = os.listdir(target)

# def getTempName(base, iter, ext):
#     return base + "_" + str(iter) + ext

# #allfiles.sort(key=lambda x: os.path.getmtime(x))
# for filename in allfiles:
#     if not os.path.isfile(filename):
#         continue
#     t = os.path.getmtime(filename)
#     # v= datetime.datetime.fromtimestamp(t)
#     # x = v.strftime('%Y%m%d')
#     x = 'collaboration_step'
#     ext = '.png'
#     loop = 1
#     iterator = 1

#     temp_name = getTempName(x, iterator, ext)

#     while filename != temp_name and filename != script_name:
#         if not os.path.exists(temp_name):
#             print 'Renaming %s to %s' % (filename, temp_name)
#             os.rename(filename, temp_name)
#             filename = temp_name
#         else:
#             iterator+=1
#             temp_name = getTempName(x, iterator, ext)