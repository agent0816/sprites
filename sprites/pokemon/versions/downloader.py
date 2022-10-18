import requests
from tqdm import tqdm
from apnggif import apnggif

female_lut = [3, 12, 19, 20, 25, 26, 41, 42, 44, 45, 64, 65, 84, 85, 97, 111, 112, 118, 119, 123, 129, 130, 154, 165, 166, 178, 185, 186, 190, 194, 195, 198, 202, 203, 207, 208, 212, 214, 215, 215, 217, 221, 224, 229, 232, 255, 256, 257, 267, 269, 272, 274, 275, 307, 308, 315, 316, 317, 322, 323, 332, 350, 369, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 407, 415, 417, 418, 419, 424, 443, 444, 445, 449, 450, 453, 454, 456, 457, 459, 460, 461, 464, 465, 473, 521, 592, 593, 668, 678, 876, 902]

female = 0
shiny = 0

forms = ['-sandy', '-trash', '-sandy', '-trash']
formmods = ['412G', '412S', '413G', '413S']
#gen = 'diamond-pearl'
#gen = 'platinum'
gen = 'heartgold-soulsilver'
mod = ''
if female:
	mod = 'female-'
if shiny:
	mod += 'shiny-'
if mod == '':
	mod = 'normal-'
folder = f'generation-iv/{gen}/{mod}animated/'
liste = female_lut if female else range(1,494)
liste = formmods
for id in tqdm(liste):
	url = f'https://bulbapedia.bulbagarden.net/wiki/File:Spr_4{gen[0]}_'
	print(url)
	ext = '.png'
	
	modifiers = ''
	if id in female_lut:
		modifiers += '_f' if female else '_m'
	if shiny:
		modifiers += '_s'

	num = str(id).rjust(3,'0') + modifiers
	site = (requests.get(url+num+ext))
	src_ind = site.content.index(b'src="//archives.bulbagarden.net/media/upload/')
	end = site.content[src_ind:].index(b'.png') +4
	url = 'https:' + str(site.content[src_ind+5:src_ind+end])[2:-1]
	response = requests.get(url)
	name = str(id)[:3] + forms[liste.index(id)]
	with open(folder + name +'.png', 'wb') as file:
		file.write(response.content)
	

	apnggif(folder + name +'.png')