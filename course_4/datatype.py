s = 'abcdefg'
# always get numbers from left to right
print s[0]
print s[2]
print s[-1]

print s[0:2]

print s[2:5]

print s[:]         # print all

print s[:5]        # print  to 5
print s[5:]        # 5 t0 the end

print s[::2]       # step = 2
print s[1::]
print s[1:5:2]

print s[-3:]       # print last three

print s[-5:-1]

print s[::-1]

# check if "c" in s

print 'c' in s 
print 'c' not in s

# string add

s1 = '3'
s1 = '3'
print s1 + s1   # result is '33'
print s + s1

# string multiply

print "#"
print "#" * 20  # multiply string

# tuple
# tuple can't change values

hero_name = "borye"
hero_blood = 100
hero_act = 10

hero_info = '%s %d %d' % (hero_name, hero_blood, hero_act)
print hero_info

hero_info = (hero_name, hero_blood, hero_act)
print hero_info
print hero_info[1]

t = ('hello',)  # only one value in tuple t, must add ","
print t

# list
# similar to tuple, but can change value

l = [1, 2, 3]
print l

print l[0]
print l[2]

hero_info_list = [hero_name, hero_blood, hero_act]
print hero_info_list

l = ['a']    # only one value in list l, no need to add anything
print l

print hero_info_list
hero_info_list[1] -= 10
print hero_info_list[1]
hero_info_list[1] +=10
print hero_info_list[1]

# dict

hero_dict = {'name': hero_name, 'blood': hero_blood, 'act': hero_act}
print hero_dict
print hero_dict['name']
print hero_dict['blood']
hero_dict['blood'] -= 10
print hero_dict['blood']

# delete one feature in the dict

del hero_dict['act']
print hero_dict