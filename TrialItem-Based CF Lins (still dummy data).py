
import random 
import math
import operator
import xlrd

class mySim(dict):

    def __init__(self):
        self = dict()

    def __getitem__(self, item):
        return self[item]

    def add(self, key, value):
        self[key] = value

    # def getKey(self):
    # 	return self.getKey

    def getValue (self, key):
    	return self.__getitem__(key)


def getData(filename):
	data = xlrd.open_workbook(filename)
	sheet = data.sheet_by_index(0)
	return sheet

DATA =getData("jester-data-1.xls")
SHEET_ROWS=DATA.nrows
SHEET_COLUMN=DATA.ncols


# load excel
# text_file1 = open("jester-data-1.xls","rl")
# # x= text_file1.readline()

# # A= array of user [1..11]
# # B= array of jokes [1..11]
# rand = random.randint(1,11)
# Data = [[0]*(6)*(6)]
Data = [[0 for x in range(6)] for x in range(6)] 

Data[0][0]=2
Data[0][3]=4
Data[0][4]=5

Data[1][0]=5
Data[1][2]=4
Data[1][5]=1

Data[2][2]=5
Data[2][4]=2

Data[3][1]=1
Data[3][3]=5
Data[3][5]=4

Data[4][2]=4
Data[4][5]=2

Data[5][0]=4
Data[5][1]=5
Data[5][3]=1

# print Data

def akses_rate (user,item):
	return DATA.row(user)[item].value

def akses_rate_tr (user,item):
	return Data[user][item]

# print akses_rate_tr(0,0)


# cell= []
# for row in range(0,9):
# 	cell.append([])
# 	for col in range (1,10):

# 		cell[row].append(DATA.row(row)[col].value)

# print cell
 
def user_rate_item(itemke):
	identify=[]
	for i in range (0,6) :
		if akses_rate_tr(i,itemke) != 0 :
			identify.append(i)
	return identify

def item_rate_user(userke):
	identify=[]
	for i in range (0,6) :
		if akses_rate_tr(userke,i) !=0:
			identify.append(i)
	return identify

# print user_rate_item(0)

# userrateitem=user_rate_item(rand)

def neighbor_formation (itemke):
	neighbor=[]
	neighbor_item= []
	x=itemke
	t=0
	
	for i in user_rate_item(itemke): 
		for j in range (0,6) :
			if (j != x) and akses_rate_tr(i,j)!=0:
				neighbor.append(j)		

	# print user_rate_item(x)
	for i in neighbor:
		if i not in neighbor_item:
			neighbor_item.append(i)
					
	return neighbor_item
	# for i in user_rate_item(itemke): 
	# 	for j in range (0,6) :
	# 		if (j != itemke) & (akses_rate_tr(i,j)!=0):
	# 			x.append(j)

	# for i in range (0,6):
	# 	a= x[i]
	# 	neighbor_item.append(a)	

	# print user_rate_item(itemke)	
	# return neighbor_item

# print neighbor_formation(5)
# neighbor_form= neighbor_formation(rand)

def average_rateitem(itemke):
	sum= 0.0
	n =0
	for i in range(0,6):
		rate=akses_rate_tr(i,itemke)
		if (rate !=0 ):
			n +=1
			sum+=rate

		# print rate
		# print sum
	average = sum/n

	return average

# print average_rateitem (0)
# print average_rateitem (1)
# print average_rateitem (2)
# print average_rateitem (3)



def average_rateuser(userke):
	sum= 0.0
	n =0
	for i in range(0,6):
		rate=akses_rate_tr(userke,i)
		if (rate != 0):
			n+= 1
			sum +=rate

	average = sum/n

	return average


# print average_rateuser (4)
# def nominator():
# 	sum =0
# 	for i in userrateitem:
# 		for j in neighbor_form:
# 			if 10 in Data[i][j]:
# 				sum += (Data[i][j]- average_rateuser(i))*(Data[i][rand]-average_rateuser(i))
# 	return sum
def nominator(item1,target):
	sum =0.0
	for i in user_rate_item(target):
			if akses_rate_tr(i,item1)!= 0:
				sum += (akses_rate_tr(i,item1)- average_rateitem(item1))*(akses_rate_tr(i,target) -average_rateitem(target))
				# print average_rateuser(i)
	return sum

# print average_rateuser(3)
# print 'lli'
# # print 1.67*0.67
# print nominator(0,5)
# def denominator(item1,item2):
# 	sum =0
# 	sam =0
# 	for i in userrateitem:
# 		for j in neighbor_form:
# 			if 10 in Data[i][j]:
# 				sum += (Data[i][j]- average_rateuser(i))^2
# 				sam += (Data[i][rand]-average_rateuser(i))^2

# 	den = math.sqrt(sum*sam)
# 	return den
def denominator(item1,target):
	sum =0.0
	sam =0.0
	for i in user_rate_item(target):
			if akses_rate_tr(i,item1) != 0:
				sum = sum + ((akses_rate_tr(i,item1)- average_rateitem(item1))**2)
				sam = sam + ((akses_rate_tr(i,target)-average_rateitem(target))**2)

		
	den = math.sqrt(sum*sam)
	return den


# print denominator(0,5)
	
def sim_calculate(item1,target):
	nom= nominator(item1,target)
	den= denominator(item1,target)
	sim= nom/den
	return sim


# print sim_calculate (0,5)

# print sim_calculate (1,5)
# print sim_calculate (2,5)

# print sim_calculate (3,5)


# myd = myDict()
# myd.add('apples',6)
# myd.add('bananas',3)
# print(myd)

def simNeighbor(target):
	neigh= neighbor_formation(target)
	sim_dict= mySim()
	for i in neigh:
		sim_val= sim_calculate(i,target)
		sim_dict.add(i,sim_val)

	sorted_x =sorted(myd.items(), key=lambda x: (-x[1], x[0]))
	return sorted_x

def totalSim(target):
	neigh= neighbor_formation(target)
	total=0.0
	for i in neigh:
		total += abs(sim_calculate(i,target))
	return total
print totalSim(5)

def Top10SimNeighbor (target):
	neigh= neighbor_formation(target)
	sim_dict= mySim()
	for i in neigh:
		sim_val= sim_calculate(i,target)
		sim_dict.add(i,sim_val)

	sorted_x =sorted(myd.items(), key=lambda x: (-x[1], x[0]))

	# topk
	listtop=[]
	for i in range (0,9):
		listtop.append(sorted_x[i])

	return listtop

def predictedRate(itemke):
	ave=average_rateitem(itemke)
	item_has_sim = neighbor_formation(itemke)
	denom = 0.0
	denom= totalSim(itemke)
	if denom==0:
		denom=0.1
	pred= mySim()
	sumini= 0.0
	user_non_target= user_rate_item(itemke)
	for i in range (0,6):
		# if i not in user_non_target:
			sumini = 0.0
			for x in item_has_sim:
				if(akses_rate_tr(i,x)!=0):
					# print x," lololo"
					sim_among = sim_calculate(x,itemke)
					item_ave= average_rateitem(x)
					sumini+=((sim_among*(akses_rate_tr(i,x)-item_ave)))
			predict_val=ave+(sumini/denom)
			# print predict_val," weeeeeeeeeeeeeee"
			pred.add(i,predict_val)
	return (pred)

# def evaluating():
# 	NewData = [[0 for x in range(6)] for x in range(6)] 
# 	for i in range(0,6):
# 		for j in range(0,6):
# 			NewData[j][i]=predictedRate(i).

a = predictedRate(3)
# print a

def getNewRate():
	A= [[0 for x in range(6)] for x in range(6)] 
	for i in range (0,6):
		predict=predictedRate(i)
		for j in range (0,6):
			A[i][j]=predict.get(j)
	return A

print getNewRate()


# {0: 2.7526550758215214, 2: 3.049151358849725, 5: 2.086200159812168}




		


	
			

