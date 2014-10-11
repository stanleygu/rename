import click

@click.command()
def hello():
    click.echo('Hello World!')

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