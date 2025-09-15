#Importing package
import pandas as pd

print("Dataset Split","1. KDDCUP99","2. NSL-KDD","3. Exit",sep='\n')
choice = int(input("Enter your choice: "))


#Importing the dataset
if choice == 1:
    dataset = pd.read_csv(".\\dataset\\kddcup99.csv")
    p=3723
    d=356691
    u=41
    r=1024
    nor=88515
elif choice == 2:
    dataset = pd.read_csv(".\\dataset\\nsl-kdd.csv")
    p=10422
    d=41407
    u=41
    r=896
    nor=61110
else:
    exit(0)

#Data-Preprocessing
protocol_type = {'icmp':1,
                 'tcp':2,
                 'udp':3}
service = {'domain_u':1,
           'ecr_i':2,
           'eco_i':3,
           'finger':4,
           'ftp_data':5,
           'ftp':6,
           'http':7,
           'hostnames':8,
           'imap':9,
           'login':10,
           'mtp':11,
           'netstat':12,
           'other':13,
           'private':14,
           'smtp':15,
           'systat':16,
           'telnet':17,
           'time':18,'uucp':19}
flag = {'REJ':1,
        'RSTO':2,
        'RSTR':3,
        'SO':4,
        'S3':5,
        'SF':6,
        'SH':7}

label = {'back': 'ddos','land': 'ddos','neptune': 'ddos','pod': 'ddos','smurf': 'ddos','teardrop': 'ddos',
         'satan': 'probe','ipsweep': 'probe','nmap': 'probe','portsweep': 'probe',
         'normal':'normal',
         'guess_passwd': 'r2l','ftp_write': 'r2l','imap': 'r2l','phf': 'r2l','multihop': 'r2l','warezmaster': 'r2l','warezclient': 'r2l','spy': 'r2l',
         'buffer_overflow': 'u2r','loadmodule': 'u2r','perl': 'u2r','rootkit': 'u2r'}

dataset['protocol_type'] = dataset.protocol_type.map(protocol_type)
dataset['service'] = dataset.service.map(service)
dataset['flag'] = dataset.flag.map(flag)
dataset['label'] = dataset.label.map(label)

dataset['protocol_type'].fillna(4,inplace=True)
dataset['service'].fillna(20,inplace=True)
dataset['flag'].fillna(8,inplace=True)

#Normalization
col_norm = list(dataset.columns)
col_norm = col_norm[:-1]
X = dataset[col_norm].values
from sklearn.preprocessing import MinMaxScaler
norm = MinMaxScaler()
X = norm.fit_transform(X)
df_temp = pd.DataFrame(X, columns=col_norm, index = dataset.index)
dataset[col_norm] = df_temp

#Seperating dataset into train and test as specified in the research paper
p_att = dataset[dataset["label"]=="probe"]
p_att_train=dataset[dataset["label"]=="probe"].sample(n=p)
p_att_test=p_att[~p_att.isin(p_att_train)].dropna()

d_att = dataset[dataset["label"]=="ddos"]
d_att_train=dataset[dataset["label"]=="ddos"].sample(n=d)
d_att_test=d_att[~d_att.isin(d_att_train)].dropna()

u_att = dataset[dataset["label"]=="u2r"]
u_att_train=dataset[dataset["label"]=="u2r"].sample(n=u)
u_att_test=u_att[~u_att.isin(u_att_train)].dropna()

r_att = dataset[dataset["label"]=="r2l"]
r_att_train=dataset[dataset["label"]=="r2l"].sample(n=r)
r_att_test=r_att[~r_att.isin(r_att_train)].dropna()

n_att = dataset[dataset["label"]=="normal"]
n_att_train=dataset[dataset["label"]=="normal"].sample(n=nor)
n_att_test=n_att[~n_att.isin(n_att_train)].dropna()


#Merging train sets and test sets together
train_set = pd.concat([p_att_train,d_att_train,u_att_train,r_att_train,n_att_train],ignore_index=True)
test_set = pd.concat([p_att_test,d_att_test,u_att_test,r_att_test,n_att_test],ignore_index=True)

train_set = train_set.sample(frac=1)
test_set = test_set.sample(frac=1)


#Saving the seperated sets in csv files
if choice == 1:
    train_set.to_csv(".\\dataset\\kddcup99-train.csv",index=False)
    test_set.to_csv(".\\dataset\\kddcup99-test.csv",index=False)
else:
    train_set.to_csv(".\\dataset\\nsl-train.csv",index=False)
    test_set.to_csv(".\\dataset\\nsl-test.csv",index=False)
        

