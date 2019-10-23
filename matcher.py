from gmpy2 import *
from algeo import *
import numpy as np
import cv2
import _pickle as pickle
import os

# Inisiasi precision
get_context().precision = 100

# Variable Global
images_path = 'HUHU/'
uvDB_dir = 'UVDB/'
dirs = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

class Matcher(object):
	def __init__(self, path, db_path="features.pck"):
		try:
			print("Trying to read data from "+db_path+"....")
			self.data = pickle.load(open(db_path, "rb"))
			print("*SUCCESS*")
		except:
			print("*FAILED*")
			print("Creating data from "+path+" to "+db_path+"....")
			createDB(path, db_path)
			self.data = pickle.load(open(db_path, "rb"))
		self.names, self.db = map(np.array, zip(*self.data.items()))
		self.names = np.array(list(map(lambda x: os.path.join(path,x), self.names)))
		'''
		try:
			print("Trying to read data from "+uvDB_dir+db_path.split("/")[1].split(".")[0]+"....")
			self.uniqueVector = pickle.load(open(uvDB_dir+db_path.split("/")[1].split(".")[0]+".uv", "rb"))
			print("*SUCCESS*")
		except:
			print("*FAILED*")
			print("Creating data from "+path+" to "+uvDB_dir+db_path.split("/")[1].split(".")[0]+"....")
			self.uniqueVector = []
			self.findUniqueVector()
			pickle.dump(self.uniqueVector, open(uvDB_dir+db_path.split("/")[1].split(".")[0]+".uv", "wb"))
		print(self.uniqueVector)
		'''

	def cosineSim(self, vector):
		v = vector.reshape(1, -1)
		return CosineSimilarityMat(self.db, v).reshape(-1)
	'''
	def findUniqueVector(self):
		init = 1
		cvec = 30
		while (len(self.uniqueVector) < cvec):
			self.uniqueVector = []
			for i in range(len(self.db[0])):
				tc = self.db[0][i]
				unique = True
				j = 0
				val = 0
				while(j < len(self.db) and unique):
					unique = (init <= (self.db[j][i]/tc) <= (1/init))
					val += (self.db[j][i]/tc)
					j += 1
				if (unique):
					self.uniqueVector.append([i,val/len(self.db)])
			init -= 0.01
		self.uniqueVector = list(zip(*sorted(self.uniqueVector,key=lambda x: abs(1-x[1]))[:cvec]))[0]
	'''
	def matchCosine(self, image_path):
		features = extract(image_path)
		distanceRange = self.cosineSim(features)
		#similarIdx = np.argsort(distanceRange)
		#print(distanceRange)
		return self.names, distanceRange

def extract(image_path, vsize=16):
	img = cv2.imread(image_path, 1)
	#img = img[int(len(img)*0.05):int(len(img)*0.95), int(len(img[0])*0.05):int(len(img[0])*0.95)]
	kaze = cv2.KAZE_create()
	kps = kaze.detect(img)
	kps = sorted(kps, key=lambda x: -x.response)[:vsize]
	kps, dsc = kaze.compute(img, kps)
	dsc = dsc.flatten('K')
	needed_size = (vsize * 64)
	if dsc.size < needed_size:
		dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
	idxFilter = [636, 811, 786, 66, 204, 743, 875, 143, 345, 891, 819, 1006, 560, 314, 955, 859, 142, 726, 959, 431, 34, 926, 153, 50, 1019, 215, 579, 195, 899, 879, 290, 519, 667, 983, 166, 175, 337, 932, 642, 660, 18, 907, 138, 467, 263, 850, 515, 367, 307, 858, 598, 338, 500, 82, 615, 978, 363, 790, 782, 47, 1008, 687, 607, 150, 21, 771, 731, 154, 1010, 600, 789, 827, 994, 52, 995, 99, 23, 347, 68, 793, 675, 912, 478, 531, 736, 238, 27, 606, 511, 323, 1018, 450, 481, 58, 703, 871, 207, 894, 302, 719, 842, 86, 214, 583, 477, 986, 342, 653, 383, 691, 730, 274, 839, 12, 70, 19, 826, 962, 334, 222, 479, 177, 1004, 734, 228, 67, 903, 346, 958, 45, 98, 495, 1007, 809, 90, 852, 666, 271, 91, 587, 862, 95, 59, 310, 2, 382, 838, 586, 534, 547, 692, 351, 232, 319, 62, 81, 770, 657, 378, 155, 777, 25, 146, 109, 97, 725, 779, 392, 739, 549, 846, 218, 575, 36, 867, 282, 11, 223, 472, 108, 26, 571, 139, 78, 578, 686, 219, 130, 735, 528, 682, 797, 927, 917, 343, 605, 524, 502, 510, 135, 614, 379, 74, 79, 22, 278, 526, 258, 934, 349, 773, 350, 673, 51, 7, 591, 608, 825, 111, 806, 326, 963, 597, 835, 661, 187, 366, 61, 1013, 494, 374, 876, 695, 843, 75, 275, 913, 688, 630, 484, 10, 152, 975, 538, 847, 452, 85, 173, 813, 708, 938, 270, 1017, 469, 100, 553, 669, 822, 677, 357, 967, 63, 330, 681, 251, 489, 89, 331, 988, 69, 262, 104, 365, 131, 212, 953, 416, 970, 485, 884, 557, 286, 545, 473, 868, 590, 971, 358, 309, 665, 29, 929, 216, 335, 191, 288, 465, 24, 518, 748, 6, 527, 28, 523, 775, 694, 344, 504, 512, 20, 493, 148, 496, 266, 740, 414, 676, 714, 910, 635, 933, 592, 446, 525, 113, 462, 16, 522, 722, 33, 535, 685, 241, 193, 952, 46, 817, 197, 445, 384, 433, 179, 550, 508, 654, 1, 73, 716, 765, 744, 483, 430, 580, 324, 596, 388, 88, 125, 554, 706, 633, 836, 362, 203, 576, 781, 76, 897, 885, 128, 844, 84, 377, 720, 864, 612, 992, 961, 460, 133, 269, 901, 1021, 668, 1012, 546, 129, 521, 996, 820, 792, 92, 482, 911, 628, 336, 96, 700, 317, 573, 373, 712, 684, 181, 492, 48, 804, 185, 137, 856, 625, 513, 732, 908, 448, 965, 0, 724, 584, 889, 649, 369, 640, 845, 432, 860, 951, 780, 565, 721, 837, 136, 284, 924, 264, 710, 833, 909, 973, 561, 156, 841, 896, 132, 709, 624, 32, 412, 674, 325, 713, 969, 509, 57, 77, 428, 149, 328, 192, 848, 44, 768, 634, 947, 957, 715, 772, 569, 905, 503, 717, 656, 728, 468, 530, 516, 280, 123, 701, 53, 272, 260, 520, 501, 444, 329, 202, 589, 141, 893, 464, 189, 237, 689, 604, 320, 788, 796, 532, 261, 623, 208, 305, 220, 268, 916, 980, 247, 769, 892, 784, 110, 396, 476, 585, 984, 265, 340, 644, 54, 900, 256, 960, 376, 506, 4, 536, 497, 829, 321, 368, 461, 354, 753, 693, 641, 1016, 196, 400, 904, 429, 577, 243, 711, 454, 976, 252, 622, 921, 964, 652, 236, 705, 333, 882, 186, 257, 370, 588, 939, 815, 457, 936, 41, 312, 49, 745, 741, 9, 968, 404, 60, 993, 801, 229, 233, 273, 840, 101, 609, 645, 888, 556, 147, 931, 245, 372, 872, 80, 821, 940, 449, 648, 205, 776, 105, 144, 453, 942, 664, 276, 593, 188, 5, 227, 877, 949, 165, 581, 163, 55, 989, 733, 761, 680, 915, 122, 140, 830, 637, 120, 1001, 697, 707, 737, 832, 499, 296, 172, 124, 849, 540, 824, 463, 751, 865, 812, 805, 935, 56, 945, 873, 613, 304, 169, 426, 380, 413, 814, 831, 1020, 456, 985, 127, 943, 869, 566, 226, 997, 930, 552, 253, 424, 394, 655, 672, 558, 114, 749, 956, 572, 562, 1009, 381, 176, 639, 421, 390, 923, 441, 248, 184, 919, 221, 698, 696, 764, 944, 224, 455, 785, 281, 117, 883, 360, 162, 647, 1005, 914, 121, 40, 397, 119, 738, 629, 115, 480, 638, 699, 902, 507, 861, 458, 250, 145, 750, 646, 116, 616, 434, 200, 918, 168, 341, 308, 410, 898, 240, 37, 767, 920, 180, 548, 209, 853, 922, 759, 406, 568, 126, 399, 981, 1000, 880, 756, 766, 418, 13, 178, 249, 763, 632, 704, 118, 977, 182, 651, 440, 225, 402, 442, 650, 906, 403, 157, 488, 857, 356, 332, 427, 242, 285, 621, 754, 391, 758, 755, 459, 808, 246, 419, 529, 387, 386, 422, 353, 564, 533, 762, 393, 64, 300, 408, 517, 65, 411, 407, 425, 409, 423, 405, 389, 752, 301, 395, 292, 293, 438, 316, 435, 437, 160, 401, 443, 385, 417, 760, 436, 17, 928, 244, 439, 420, 925]
	dsc = np.delete(dsc, idxFilter)	
	return dsc

def createDB(path,db_path="features.pck"):
	result = {}
	files_db = [os.path.join(path, p) for p in sorted(os.listdir(path))]
	for f in files_db:
		name = f.split('/')[-1].lower()
		result[name] = extract(f)
	pickle.dump(result, open(db_path, 'wb'))


