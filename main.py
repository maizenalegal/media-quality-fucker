import os

for file in os.listdir('input'):

	print('Fuck ' + file + '? [Y/n]: ')

	yesorno = input().upper()

	while yesorno != 'Y' and 'N' and '':

		print('[Y/n]: ')

		yesorno = input().upper()

	if yesorno == 'Y' or yesorno == '':

		print('Fucking ' + file)

		split = os.path.splitext(file)

		filename = split[0]

		extension = split[len(split)-1]

		os.system('ffmpeg -y -i ' + '"input/' + file + '" -loglevel quiet -c:a ac3 -vf "scale=\'min(60,iw)\':\'min(60,ih)\'" -b:a 1k -b:v 30k ' + 'output/0' + extension)
		os.system('ffmpeg -y -i ' + '"output/0' + extension + '" -loglevel quiet -vf "scale=\'max(720,iw)\':\'max(720,ih)\'" -b:a 1k -b:v 30k ' + '"output/' + filename + ' fucked' + extension + '"')

		os.remove('output/0' + extension)

		print('Done fucking ' + file + '.\n')