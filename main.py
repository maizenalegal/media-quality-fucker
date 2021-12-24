import os

filesToFuck = []

for file in os.listdir('input'):

	print('Fuck ' + file + '? [Y/n]: ')

	yesOrNo = input().upper()

	while yesOrNo != 'Y' and 'N' and '':

		print('[Y/n]: ')

		yesOrNo = input().upper()

	if yesOrNo == 'Y' or yesOrNo == '':

		filesToFuck.append(file)

for file in filesToFuck:
	print('Fucking ' + file)

	split = os.path.splitext(file)

	filename = split[0]

	extension = split[len(split)-1]

	os.system('ffmpeg -y -i ' + '"input/' + file + '" -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 -loglevel quiet -c:a ac3 -vf "scale=\'min(60,iw)\':\'min(60,ih)\'" -b:a 8k -b:v 30k ' + 'output/0' + extension)
	os.system('ffmpeg -y -i ' + '"output/0' + extension + '" -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 -loglevel quiet -vf "scale=\'max(720,iw)\':\'max(720,ih)\'" -b:a 8k -b:v 30k ' + '"output/' + filename + ' fucked' + extension + '"')

	os.remove('output/0' + extension)

	print('Done fucking ' + file + '.\n')
