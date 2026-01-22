stds = {
  
  'chandu':{
    'first_name' : 'Chandu',
    'last_name'  : 'Reddy',
    'dept' : 'MCA',
    'section' : 'A',
    'usn' : '19'
  },
  
  
  'mohan':{
    'first_name' : 'Mohan',
    'last_name'  : 'Babu',
    'dept' : 'MCA',
    'section' : 'A',
    'usn' : '58'
  },
  
  
  'raju':{
    'first_name' : 'Raju',
    'last_name'  : 'Reddy',
    'dept' : 'MCA',
    'section' : 'B',
    'usn' : '80'
  },
  
  'shahi':{
    'first_name' : 'Shashi',
    'last_name'  : 'Kumar',
    'dept' : 'MCA',
    'section' : 'B',
    'usn' : '90'
  },
  
  
}

for user_name, user_info in stds.items():
  print(f"Student Name: {user_name}")
  fullname = user_info['first_name'] + " " + user_info['last_name']
  dept = user_info['dept']
  section = user_info['section']
  usn = user_info['usn']
  
  
  print(f"Full Name: {fullname}")
  print(f"Department: {dept}")
  print(f"section: {section}")
  print(f"USN: {usn}")
  print("")