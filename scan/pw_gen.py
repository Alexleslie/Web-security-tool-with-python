import itertools

class User:
    def __init__(self, u_dic):
        self.u_dic = u_dic
        
        self.first_name = u_dic['first_name']
        self.last_name = u_dic['last_name']
        self.abb_name = u_dic['abb_name']
        
        self.day = u_dic['day'] 
        if len(self.day) == 1:
            self.day = '0' + self.day
        self.mouth = u_dic['mouth']
        if len(self.mouth) == 1:
            self.mouth = '0' + self.mouth
        self.year = u_dic['year']
  
        
        self.phone = u_dic['phone']
        
        self.qq = u_dic['qq']
        self.email = u_dic['email']
    
        self.old_account = u_dic['old_account']
            
    def combinations(self, tem_list, number):
        com_list = itertools.combinations(tem_list, number)
        value_list = []
        for i in com_list:
            combinations = ''
            for j in i:
                combinations += j
                value_list.append(combinations)
        return value_list
        
    
    def password_generate(self):
        name_list = [self.first_name, self.last_name, self.first_name+self.last_name, 
                     self.last_name+self.first_name]
        birthday_list = [self.year, self.day, self.mouth, self.year+self.mouth+self.day, 
                     self.mouth+self.day, self.year+self.mouth]
        if self.phone:
            phone_list = [self.phone, self.phone[-4:], self.phone[-5:], self.phone[-3:]]
        else:
            phone_list = []
        
        other_list  = [self.abb_name, self.qq, self.email,self.old_account]
        all_list = [i for i in other_list if len(i)> 0]
        all_list = all_list + name_list + birthday_list + phone_list 
        
        password_list = []
        for i in range(3):
            tem_list = self.combinations(all_list, i)
            password_list += tem_list
        
        self.password_list = set(password_list)
        print self.password_list
             

if __name__ == '__main__':
    User_dict = {'first_name':'san', 'last_name':'zhang', 'abb_name':'ZS', 'year':'2001', 
                 'mouth':'09', 'day':'01', 'phone':'13322200789', 'email':'drinkmorewater@qq.com', 
                 'qq':'666666', 'old_account':'leslie'}                                  
    user = User(User_dict)
    user.password_generate()